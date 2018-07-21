from PIL import Image
import keras
from keras import backend as K
from keras.models import Sequential
from keras.layers.core import Dense, Flatten
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing.image import img_to_array
from flask import request
from flask import jsonify
from flask import Flask
import io
import numpy as np
import base64
import tensorflow as tf

app = Flask(__name__)

def get_model():
    global model
    global graph

    vgg16_model = keras.applications.vgg16.VGG16()
    model = Sequential()

    for i in vgg16_model.layers:
        model.add(i)

    for layer in model.layers:
        layer.trainable = False

    model.add(Dense(4, activation='softmax'))     

    model.load_weights("model_weights.h5")    
    
    model._make_predict_function()
    graph = tf.get_default_graph()
    print("Model loaded!")

def preprocess_image(image, target_size):
    if image.mode != "RGB":
        image = image.convert("RGB")
    
    image = image.resize(target_size)
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    print(np.shape(image))

    return image

print(" Loading Keras model...")
get_model()

@app.route("/predict", methods=["POST"])
def predict():
    message = request.get_json(force=True)
    encoded = message['image']
    decoded = base64.b64decode(encoded)
    decode = io.BytesIO(decoded)
    image = Image.open(decode)

    image.save("picture.jpg")
    image = Image.open("picture.jpg")   

    processed_image = preprocess_image(image, target_size=(224, 224))
    
    with graph.as_default():
        prediction = model.predict(processed_image).tolist()

    response = {
        'prediction': {
             'dog': prediction[0][0],
             'cat': prediction[0][1],
             'monkey': prediction[0][2],
             'cow': prediction[0][3]
        }
    }
    return jsonify(response)

