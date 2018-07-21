# API for Image Classification
This repository provides the code implementation of Flask web service RESTful API built for the following Image Classification model:

 https://github.com/princenarula222/Image_Classifier

Here is the link to the sample model weights along with the demo video of the API:

 https://drive.google.com/open?id=1A6MdS72OKOc0BpHFewA2xP7giapHaFox


# Dependencies
Languages - Python

Frameworks - Flask, Keras, Numpy, Pillow, TensorFlow


# Setup Procedure
Steps to be followed for setting up your own server are as follows:

 Replace "192.168.0.103" in 'predict.html'(static/predict.html) with the external ip address of your server system.

 Place your model weights in the root folder of this repository.

 Open command line terminal and change your present working directory to this repository.

 Execute the following commands depending upon your operating system:
     
     export FLASK_APP=predict_app.py (Ubuntu)
     SET FLASK_APP=predict_app.py (Windows)

     flask run --host=0.0.0.0 (OS independent command to be followed by one of the previous commands for public access)

 Access the web service by visiting "\<server external ip address\>:5000/static/predict.html".