import requests
import time
import json
# 使用注意，在初始化的时候（第一次使用的时候速度较慢，在第二次使用则恢复正常，在4ms左右）
if __name__ == '__main__':
	st = time.clock()
	api_url = "http://127.0.0.1:5000/predict"
	# 直接上传图片路径即可
	for pic_path in ["pic/dog.jpg", 'pic/cat.jpg']:
		print(pic_path)
		para = {"image": pic_path}
		model_result = requests.post(api_url, data=json.dumps(para)).json()
		print(model_result)
	print('time used: {}'.format(time.clock() - st))