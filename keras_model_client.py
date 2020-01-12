import requests
import time
# 使用注意，在初始化的时候（第一次使用的时候速度较慢，在第二次使用则恢复正常，在4ms左右）
if __name__ == '__main__':
	st = time.clock()
	api_url = "http://127.0.0.1:5000/predict"
	for pic_path in ["pic/dog.jpg", 'pic/cat.jpg']:
		print(pic_path)
		image = open(pic_path, "rb").read()
		para = {"image": image}
		model_result = requests.post(api_url, files=para).json()
		if model_result["success"]:
			# loop over the predictions and display them
			for (i, result) in enumerate(model_result["predictions"]):
				print("{}. {}: {:.4f}".format(i + 1, result["label"], result["probability"]))
		else:
			print("Request failed")
	print('time used:{}'.format(time.clock() - st))