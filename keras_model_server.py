# coding = utf-8
from tensorflow.keras.applications import ResNet50, imagenet_utils
from tensorflow.keras.preprocessing.image import img_to_array
from flask import Flask, jsonify, request
from PIL import Image
import numpy as np
import json
import io
app = Flask(__name__)
def global_():
	# 全局加载model, graph
	global model
	model_path = 'model/resnet50_weights_tf_dim_ordering_tf_kernels.h5'
	model = ResNet50(weights=model_path)
def processing(image):
	if image.mode != "RGB":
		image = image.convert("RGB")
	image = image.resize((224, 224))
	image = img_to_array(image)
	image = np.expand_dims(image, axis=0)
	image = imagenet_utils.preprocess_input(image)
	return image

global_()
@app.route("/predict", methods=['POST'])
def model_predict():
	data = json.loads(request.get_data().decode('utf-8'))
	pic_path = data['image']
	image = open(pic_path, "rb").read()
	image = Image.open(io.BytesIO(image))
	image_ = processing(image)
	prediction = model.predict(image_)
	results = imagenet_utils.decode_predictions(prediction)
	data = dict()
	data["predictions"] = []
	for (_, label, prob) in results[0]:
		r = {"label": label, "probability": float(prob)}
		data["predictions"].append(r)
	data["success"] = 1
	return jsonify(data)
if __name__ == "__main__":
	app.run(port=5016)