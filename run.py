# -*- coding:utf-8 -*-
# run.py 项目入口文件
from app import create_app

app = create_app()

if __name__ == "__main__":
    # debug
    # app.run(host='0.0.0.0', port=5000, debug=True)
    # development
    app.run(host='0.0.0.0', port=5000)
