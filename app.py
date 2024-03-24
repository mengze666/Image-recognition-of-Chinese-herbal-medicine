# -*- coding:utf-8 -*-
# app.py 项目入口文件
from App import create_app
import cfg

app = create_app(config=cfg.BaseConfig)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

