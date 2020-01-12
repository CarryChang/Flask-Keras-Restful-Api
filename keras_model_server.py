from keras.applications import ResNet50
from keras.preprocessing.image import img_to_array
from keras.applications import imagenet_utils
import numpy as np
from flask import Flask, jsonify, request, Flask, redirect
import tensorflow as tf
import io
from PIL import Image
app = Flask(__name__)
def global_():
	# 全局加载model, graph
	global model, graph
	model = ResNet50(weights="imagenet")
	graph = tf.get_default_graph()
def processing(image):
	if image.mode != "RGB":
		image = image.convert("RGB")
	image = image.resize((224, 224))
	image = img_to_array(image)
	image = np.expand_dims(image, axis=0)
	image = imagenet_utils.preprocess_input(image)
	return image
# 加载全局变量：model ，graph
global_()
@app.route("/predict", methods=['POST'])
def predict():
	image = request.files['image'].read()
	image = Image.open(io.BytesIO(image))
	image_ = processing(image)
	# graph重置
	with graph.as_default():
		data = {}
		prediction = model.predict(image_)
		results = imagenet_utils.decode_predictions(prediction)
		data["predictions"] = []
		for (imagenetID, label, prob) in results[0]:
			r = {"label": label, "probability": float(prob)}
			data["predictions"].append(r)
		# indicate that the request was a success
		data["success"] = True
	return jsonify(data)
if __name__ == "__main__":
	app.run(debug=False)