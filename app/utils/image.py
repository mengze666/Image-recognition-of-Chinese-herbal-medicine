# -*- coding:utf-8 -*-
# utils.py ：工具箱
from . import defines

import cv2
import numpy as np


def get_label_data() -> dict:
    return defines.LABEL_DICT


def resize_short(img: np.ndarray, target_size: int) -> np.ndarray:
    """
    这个函数用于将输入的图像按照较短的边进行等比例缩放，使得较短的边的长度等于指定的target_size。
    函数首先计算缩放比例，然后根据计算出的比例对图像进行缩放操作，最终返回缩放后的图像。
    Args:
        img:
        target_size:

    Returns:

    """
    percent = float(target_size) / min(img.shape[0], img.shape[1])
    resized_width = int(round(img.shape[1] * percent))
    resized_height = int(round(img.shape[0] * percent))
    resized = cv2.resize(img, (resized_width, resized_height))
    return resized


def crop_image(img: np.ndarray, target_size: int, center: bool) -> np.ndarray:
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


def preprocess(img_bytes: bytes) -> np.ndarray:
    """
    这个函数是一个整体的图像预处理流程，包括调用resize_short和crop_image函数对图像进行缩放和裁剪操作，
    然后进行一系列的处理，如颜色通道转换（BGR到RGB）、维度变换（HWC到CHW）、归一化等操作，
    最终返回经过预处理后的图像数据。
    """
    mean = [0.485, 0.456, 0.406]
    std = [0.229, 0.224, 0.225]
    img = np.frombuffer(img_bytes, np.uint8)
    img = cv2.imdecode(img, cv2.IMREAD_COLOR)
    img = resize_short(img, 224)
    img = crop_image(img, 224, True)
    # bgr-> rgb && hwc->chw
    img = img[:, :, ::-1].astype('float32').transpose((2, 0, 1)) / 255
    img_mean = np.array(mean).reshape((3, 1, 1))
    img_std = np.array(std).reshape((3, 1, 1))
    img -= img_mean
    img /= img_std
    return img[np.newaxis, :]


def result_process(result):
    max_labels = np.argsort(result[0][0])[::-1][:5]
    res = {}
    data = get_label_data()
    for lab in max_labels:
        key = data[str(lab)]['name']
        value = result[0][0][lab]
        res[key] = value * 100
    for key in res:
        res[key] = round(res[key], 2)

    return res
