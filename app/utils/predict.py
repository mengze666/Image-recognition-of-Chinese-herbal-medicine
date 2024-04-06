# -*- coding:utf-8 -*-
# app/utils/predict.py 预测模块
from paddle.inference import Config, create_predictor
from config.cfg import BaseConfig
from .image import preprocess, result_process

import os


LABEL = os.path.join(BaseConfig.STATIC_FOLDER, 'json/label.json')
PDMODEL = os.path.join(BaseConfig.STATIC_FOLDER, 'models/inference.pdmodel')
PDIPARAMS = os.path.join(BaseConfig.STATIC_FOLDER, 'models/inference.pdiparams')


# 初始化预测器和带锁的预测器
g_PredictorConfig = None
g_Predictor = None
g_PredictorWithLock = None


def init_predictor_config():
    """
    初始化预测器配置对象
    Returns:预测器配置对象
    """
    config = Config()
    config.set_model(PDMODEL, PDIPARAMS)
    config.enable_memory_optim()
    config.disable_glog_info()
    config.set_cpu_math_library_num_threads(10)
    config.mkldnn_enabled()
    config.enable_profile()
    # print(config.summary())
    return config


def get_predictor_config():
    """
    获取预测器配置单例
    Returns:

    """
    global g_PredictorConfig
    if not g_PredictorConfig:
        g_PredictorConfig = init_predictor_config()
    return g_PredictorConfig


def init_predictor():
    """
    初始化预测器对象
    Returns:预测器对象
    """
    config = get_predictor_config()
    predictor = create_predictor(config)
    return predictor


def get_predictor():
    """
    获取预测器单例
    Returns:单例预测器
    """
    global g_Predictor
    if not g_Predictor:
        g_Predictor = init_predictor()
    return g_Predictor


def run(pre, img):
    """
    执行预测
    Args:
        pre: 预测器
        img: 图片数据

    Returns: 预测结果

    """
    # copy img data to input tensor
    input_names = pre.get_input_names()
    for i, name in enumerate(input_names):
        input_tensor = pre.get_input_handle(name)
        input_tensor.reshape(img[i].shape)
        input_tensor.copy_from_cpu(img[i])
    # do the inference
    pre.run()
    results = []
    # get out data from output tensor
    output_names = pre.get_output_names()
    for i, name in enumerate(output_names):
        output_tensor = pre.get_output_handle(name)
        output_data = output_tensor.copy_to_cpu()
        results.append(output_data)
    return results


def do_predict(image_file):
    """
    对外接口：预测图片类别
    Args:
        image_file: 图片文件

    Returns: 预测Top5

    """
    img = preprocess(image_file)
    predictor = get_predictor()
    result = run(predictor, [img])
    res = result_process(result)
    return res
