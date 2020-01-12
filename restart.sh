export PATH=$PATH:/usr/local/bin
#!/bin/bash
cd /home/Flask-Keras-Restful-Api
kill `cat log/gunicorn.pid`
# ps -ef|grep "gunicorn" |grep -v grep|cut -c 9-15|xargs kill -9
rm -rf log/*
source /home/v1/bin/activate
#pstree -ap|grep gunicorn
gunicorn  -c gun.py keras_model_server:app
deactivate