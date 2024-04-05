import datetime
import requests
import threading
import json

everyone_responses = []


def upload_image(user_id, image_path):
    # 替换为服务器的地址
    url = 'http://127.0.0.1:5000/predict'

    # 读取图片数据
    with open(image_path, 'rb') as file:
        files = {'file': (image_path, file)}

        # 每个用户使用不同的请求头
        headers = {'User-Agent': f'User_{user_id}'}

        # 发送 POST 请求
        everyone_responses.append(requests.post(url, files=files, headers=headers))


if __name__ == '__main__':
    # 读取 JSON 文件
    with open('../static/json/label.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    # 创建空字典
    result_dict = {}

    # 遍历 JSON 数据，将 key 作为字典的键，"pinyin" 的值作为字典的值
    for key, value in data.items():
        result_dict[key] = value['pinyin']

    # 模拟100个用户同时上传图片
    threads = []
    results = []
    for i in range(100):
        # 替换为不同的图片文件路径
        path = f'../static/images/cls/{result_dict[str(i)]}.jpg'
        t = threading.Thread(target=upload_image, args=(i, path))
        threads.append(t)
    start = datetime.datetime.now()
    for t in threads:
        t.start()

    for t in threads:
        t.join()
    end = datetime.datetime.now()

    print("耗时:", end - start)

    error = 0
    for res in everyone_responses:
        userName = res.request.headers['User-Agent']
        result = res.json()
        if data[userName[5:]]['name'] != sorted(result.items(), key=lambda x: x[1])[-1][0]:
            error += 1
            print(data[userName[5:]]['name'], result)
    print(f'出现了{error}此错误')
