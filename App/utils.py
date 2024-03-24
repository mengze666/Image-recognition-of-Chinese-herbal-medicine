# -*- coding:utf-8 -*-
# utils.py ：工具箱
from paddle.inference import Config
from paddle.inference import create_predictor

import json
import os
import numpy as np
import cv2
import cfg


LABEL = os.path.join(cfg.BaseConfig.STATIC_FOLDER, 'json/label.json')
PDMODEL = os.path.join(cfg.BaseConfig.STATIC_FOLDER, 'models/inference.pdmodel')
PDIPARAMS = os.path.join(cfg.BaseConfig.STATIC_FOLDER, 'models/inference.pdiparams')


def resize_short(img, target_size):
    """
    这个函数用于将输入的图像按照较短的边进行等比例缩放，使得较短的边的长度等于指定的target_size。
    函数首先计算缩放比例，然后根据计算出的比例对图像进行缩放操作，最终返回缩放后的图像。
    """

    percent = float(target_size) / min(img.shape[0], img.shape[1])
    resized_width = int(round(img.shape[1] * percent))
    resized_height = int(round(img.shape[0] * percent))
    resized = cv2.resize(img, (resized_width, resized_height))
    return resized


def crop_image(img, target_size, center):
    """
    这个函数用于对输入的图像进行裁剪操作。根据指定的target_size和center参数，
    函数会在图像中随机选择一个区域进行裁剪或者在图像中心位置进行裁剪，最终返回裁剪后的图像。
    """

    height, width = img.shape[:2]
    size = target_size
    if center:
        w_start = (width - size) / 2
        h_start = (height - size) / 2
    else:
        w_start = np.random.randint(0, width - size + 1)
        h_start = np.random.randint(0, height - size + 1)
    w_end = w_start + size
    h_end = h_start + size
    img = img[int(h_start):int(h_end), int(w_start):int(w_end), :]
    return img


def preprocess(img):
    """
    这个函数是一个整体的图像预处理流程，包括调用resize_short和crop_image函数对图像进行缩放和裁剪操作，
    然后进行一系列的处理，如颜色通道转换（BGR到RGB）、维度变换（HWC到CHW）、归一化等操作，
    最终返回经过预处理后的图像数据。
    """
    mean = [0.485, 0.456, 0.406]
    std = [0.229, 0.224, 0.225]
    img = resize_short(img, 224)
    img = crop_image(img, 224, True)
    # bgr-> rgb && hwc->chw
    img = img[:, :, ::-1].astype('float32').transpose((2, 0, 1)) / 255
    img_mean = np.array(mean).reshape((3, 1, 1))
    img_std = np.array(std).reshape((3, 1, 1))
    img -= img_mean
    img /= img_std
    return img[np.newaxis, :]


def run(predictor, img):
    """启动预测器"""
    # copy img data to input tensor
    input_names = predictor.get_input_names()
    for i, name in enumerate(input_names):
        input_tensor = predictor.get_input_handle(name)
        input_tensor.reshape(img[i].shape)
        input_tensor.copy_from_cpu(img[i])
    # do the inference
    predictor.run()
    results = []
    # get out data from output tensor
    output_names = predictor.get_output_names()
    for i, name in enumerate(output_names):
        output_tensor = predictor.get_output_handle(name)
        output_data = output_tensor.copy_to_cpu()
        results.append(output_data)
    return results


def init_predictor():
    """初始化预测器
    详见https://www.paddlepaddle.org.cn/inference/v2.6/api_reference/python_api_doc/Config_index.html
    """
    config = Config()
    config.set_model(PDMODEL, PDIPARAMS)
    config.enable_memory_optim()
    config.set_cpu_math_library_num_threads(4)
    config.enable_mkldnn()
    # config.enable_profile()
    # config.summary()
    config.disable_glog_info()
    # print("GLOG INFO is: {}".format(config.glog_info_disabled()))
    predictor = create_predictor(config)
    return predictor


def predict(img_path):
    """预测图片类别主函数"""
    global pred
    img = cv2.imread(img_path)
    img = preprocess(img)
    result = run(pred, [img])
    max_labels = np.argsort(result[0][0])[::-1][:5]
    res = {}
    for lab in max_labels:
        key = data[str(lab)]['name']
        value = result[0][0][lab]
        res[key] = value * 100
    for key in res:
        res[key] = round(res[key], 2)
    return res


'''
本段代码主要是为了避免每次预测都执行无用的部分，因此设置为全局变量。
'''

# 加载label.json
with open(LABEL, 'r', encoding='utf-8') as f:
    data = json.load(f)

if "pred" not in globals():
    # 初始化预测器
    global pred
    pred = init_predictor()
