
[![996.icu](https://img.shields.io/badge/link-996.icu-red.svg)](https://996.icu)


### Flask-Keras-Restful-Api
#### 一个简单的imagenet的flask后端API，修改了全局model load的方式，增加了模型推理的速度，使用nginx搭配Gunicorn启动Flask，使用虚拟环境搭配sh的启动方式，可以直接对model进行一键重启，并有错误日志监控
 
>  一键部署，源代码修改自： [*Building a simple Keras + deep learning REST API*](https://blog.keras.io/building-a-simple-keras-deep-learning-rest-api.html) 

## 使用方法

> 1. keras_model_server.py表示后端的model api，直接通过post传参的形式进行，直接搭配nginx+Gunicorn部署即可
> 2. keras_model_client.py表示模型前端的调用，传入两张图片，然后使用imagenet的模型进行识别，模型第一次初始化的时间因为需要加载预训练模型，推理速度有些慢，后面正常的推理速度在100ms之内，多进程部署会继续提速


> 后端启动打印的log

<div align=center><img  src="https://github.com/CarryChang/Flask-Keras-Restful-Api/blob/master/pic/back_end.png"></div>


> 模型输出的结果

<div align=center><img  src="https://github.com/CarryChang/Flask-Keras-Restful-Api/blob/master/pic/frontend.png"></div>
