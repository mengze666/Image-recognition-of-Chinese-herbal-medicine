# 中药材识别系统

![image](https://github.com/mengze666/Image-recognition-of-Chinese-herbal-medicine/blob/master/static/images/baike.jpg)

#### 一、项目简介

中华文化博大精深，作为当代新时代青年，更应该将之传承并发扬下去，中药材是中华文化的一大亮点，更应受到人们的重视。中药材类别繁杂，肉眼不好区分，而人工智能技术已经较为成熟。显然，人工智能已成为替代人工挑选的一大工具，这自然让人想到通过人工智能技术对中药材进行识别、分类。  
本项目通过**ResNet-50残差网络**进行图片分类模型训练，深度学习框架来自百度飞桨的PaddleX，数据集包括163种常见中药材，训练集共256,767张图片，测试集共10,000张图片，通过20轮次的训练，该模型的 **Top1**准确率可达到98.1%，**Top5**准确率可达到99.8%。

#### 二、技术选用

- **深度学习框架：PaddlePaddle**

- **神经网络模型：ResNet-50**

- **训练环境：PaddleX**

- **数据集：网络收集整合**

- **系统后端：Flask + MySQL5.7**

- **系统前端：HTML5 + Bulma.css + Javascript**

#### 三、实现流程

本项目可以分为以下几个步骤:

1. 选题

2. 确定深度学习框架

3. 挑选神经网络模型

4. 制作数据集

5. 训练模型

6. 预测模型

7. 构建系统框架

8. 模型部署

#### 四、项目环境配置

1. 创建Python虚拟环境前
   
   由于本项目需要使用深度学习框架，因此推荐使用Anaconda来创建虚拟环境，具体Anaconda的安装及配置网上有很多教程，这里不做赘述。
   
   安装成功之后，执行命令后成功输出conda版本，即代表Anaconda环境配置成功，可以通过conda创建虚拟环境了。
   
   ```bash
   conda -V
   ```

2. 配置conda国内镜像源
   
   找到你的C盘用户目录下的.condarc文件，Windows 用户无法直接创建名为 .condarc 的文件，可在命令行执行
   
   ```bash
   conda config --set show_channel_urls yes
   ```
   
    无报错可以查看上述文件是否被成功生成，如成功生成，则编辑替换为如下内容
   
   ```ini
   channels:
   - defaults
   show_channel_urls: true
   default_channels:
   - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
   - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/r
   - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/msys2
   custom_channels:
   conda-forge: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
   msys2: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
   bioconda: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
   menpo: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
   pytorch: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
   pytorch-lts: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
   simpleitk: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
   deepmodeling: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/
   ```

3. 创建虚拟环境
   
   ```bash
   # your_env_name修改为你自定义的虚拟环境名，使用全英文，这里是使用的是irchm
   conda create --name irchm python
   # 附上移除操作，必须保证环境没被其他程序占用才可进行删除，否则删不干净
   # conda remove --name irchm --all
   ```

4. 在PyCharm上面添加该虚拟解释器
   
   步骤：文件->设置->项目->Python解释器->添加本地解释器->Conda环境->使用现有环境->找到你刚刚创建的虚拟环境->确定。

5. 安装依赖包
   使用PyCharm打开项目根目录，使用Ctrl+F12打开终端，可以看到类似如下效果（前边有带着虚拟环境名称的括号，这就代表你可以管理你的虚拟环境了）：
   
   ```text
   (irchm) PS D:\projects\PyCharm\Image-recognition-of-Chinese-herbal-medicine>
   ```
   
   这里需要使用pip安装依赖，因为pip是官方认可的专门用于Python包管理的工具，因此这里面的包都是最新版的，而conda里面有的包不是最新版本的。
   
   在使用pip安装我们的依赖包之前，我们首先配置一下pip国内镜像源，首先需要找到C盘用户目录，里面有一个pip.ini，如果没有可以新建一个，然后将下边的内容填写进去：
   
   ```ini
   [global]
   timeout=40
   index-url=http://mirrors.aliyun.com/pypi/simple/
   extra-index-url=
           https://pypi.tuna.tsinghua.edu.cn/simple/
           http://pypi.douban.com/simple/
           http://pypi.mirrors.ustc.edu.cn/simple/
   [install]
   trusted-host=
           pypi.tuna.tsinghua.edu.cn
           mirrors.aliyun.com
           pypi.douban.com
           pypi.mirrors.ustc.edu.cn
   ```
   
   然后关掉刚刚的终端再次打开它，避免刚刚的修改没有奏效，然后在终端输入如下命令
   
   ```bash
   pip install -r requirements.txt
   ```
   
   使用conda list命令检查依赖是否和requirements.txt文件是否一致，若一致即可进行下一步操作了。

6. 安装MySQL
   相信大家电脑上都有MySQL，我这里使用的是MySQL5.7，使用其他版本也可以，具体下载配置步骤网上教程比较多，这里不做赘述，但还是啰嗦一下，请牢记你的root密码!

7. 创建数据库
   这里建议数据库名创建为chinese_medicine，字符集为utf8，默认排序规则为utf8_general_ci。
   
   ```MySQL
   CREATE DATABASE chinese_medicine DEFAULT CHARACTER SET utf8 DEFAULT COLLATE        utf8_general_ci;
   ```

#### 五、系统初始化

1. 修改配置文件，在系统初始化前，先查看cfg.py文件，这是一个项目配置基类文件，需要修改为你的数据库配置，若一致则略过此步

2. 在终端执行以下命令，注意第四个命令不用执行

```bash
# 1. 初始化数据库 
flask db init
```

```bash
# 2. 进行数据迁移
flask db migrate
```

```bash
# 3. 更新数据版本
flask db upgrade
```

```bash
# 4. 回退数据版本
flask db downgrade
```

> 特别声明：数据库表是由系统初始化自动生成的，具体可以看App.models模块中的数据表映射类，禁止手动操作MySQL的相应表结构，alembic_version表用于版本管理，禁止修改。对于t_medicine表中的数据，可通过csv文件导入，具体如何导入，自己网上搜，不再赘述。

# 
