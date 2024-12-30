# E-WASTE-CLASSIFIER-EMPLOYING-TEACHABLE-MACHINE-FOR-SUSTAINABLE-SOLUTIONS
The E-Waste Classifier uses Teachable Machine to categorize electronic waste for efficient recycling, promoting sustainability and environmental responsibility.

### Project Overview

This project presents an innovative e-waste analytics solution combining Teachable Machine and Streamlit to encourage responsible electronic device disposal. Users can input their old device model into an intuitive Streamlit interface, which estimates the recoverable precious metals based on the device's classification. Teachable Machine’s machine learning models help identify the devices and calculate the metal content, promoting sustainable practices. The application rewards users with credit points for proper disposal, fostering environmental responsibility and engagement in recycling programs. This project aims to integrate advanced technology and incentivize participation in e-waste management, contributing to a circular economy.

### Teachable Machine

Teachable Machine is a web-based tool developed by Google's Creative Lab that allows users to train machine learning models without needing to write any code. It's designed to make machine learning accessible to everyone, regardless of their programming experience. The tool uses a technique called transfer learning, which leverages pre-trained models and allows users to retrain them with their own data. With Teachable Machine, you can train models to recognize images, sounds, or even pose detection using your webcam.

### Streamlit

Streamlit is an open-source Python library that allows you to create interactive web applications for data science and machine learning projects with ease. It simplifies the process of building and sharing web apps directly from Python scripts, without requiring knowledge of web development languages such as HTML, CSS, or JavaScript.


### Objectives

•	Develop a user-friendly interface using Streamlit to facilitate input of old device models.
<Br>
•	Train machine learning models with Teachable Machine to classify device models and estimate precious metal content.
<Br>
•	Implement a credit points system based on the estimated precious metal recovery.
<Br>
•	Integrate the Teachable Machine models and credit points system into the Streamlit application.
<Br>
•	Test the application for accuracy, usability, and functionality.
<Br>
•	Deploy the application for public use and monitor user engagement and feedback.



### Tools

TensorFlow and Keras
<Br>
Teachable Machine
<Br>
Streamlit
<Br>
Pillow 
<Br>
NumPy
<Br>
Dotenv


### Dataset

The dataset for this project likely consists of images of various electronic devices and equipment, such as batteries, televisions, printers, mobile phones, mice, keyboards, PCBs (Printed Circuit Boards), microwaves, players, and washing machines. Each image in the dataset is labeled with the corresponding class or category of the electronic device it represents.

### Execution
Here's a step-by-step overview of the execution process for e-waste classification using Teachable Machine and a Streamlit application:

<b> Data Collection: </b>
Gather a dataset of images representing different types of e-waste items such as batteries, televisions, printers, mobile phones, etc. Ensure that the dataset is diverse and representative of the classes you want to classify.

<b> Model Training with Teachable Machine: </b>
•	Go to the Teachable Machine website or use the Teachable Machine desktop application.
<Br>
•	Upload your dataset to Teachable Machine.
<Br>
•	Label the images according to their corresponding e-waste classes.
<Br>
•	Choose a pre-trained model architecture (usually based on CNNs) provided by Teachable Machine.
<Br>
•	Train the model using the labeled images. Teachable Machine handles the training process, including data preprocessing and model optimization.
<Br>
•	Evaluate the trained model's performance and make adjustments if necessary.

<b> Export Trained Model: </b>
Once satisfied with the model's performance, export it from Teachable Machine in a format compatible with TensorFlow.js. This format allows the model to be used in web applications.

<b> Streamlit Application Development: </b>
Set up a Streamlit environment for building the web application. Write code to create the user interface (UI) of the application using Streamlit components. This UI typically includes features such as file upload buttons and classification result displays.


<b> Integration with Trained Model: </b>
Incorporate the exported TensorFlow.js model into the Streamlit application. This involves loading the model and defining functions to preprocess input images and make predictions using the model.

<b> User Interaction: </b>
•	Users interact with the Streamlit application by uploading images of e-waste items they want to classify.
<Br>
•	Upon uploading an image, the application preprocesses the image and feeds it into the trained model for classification.

<b> Display Results: </b>
The Streamlit application displays the classification results to the user, indicating the predicted class of the uploaded e-waste item and any additional information about its sustainability or environmental impact.

<b> Further Actions: </b>
Users may take further actions based on the classification results, such as learning about proper disposal methods or exploring ways to recycle the e-waste item.

![image](https://github.com/user-attachments/assets/4d0e144b-6d22-404f-b238-ae7c5b8aeb2d)
![image](https://github.com/user-attachments/assets/11a5df43-5ed4-4f83-af0a-d2ae96e1ed56)
![image](https://github.com/user-attachments/assets/615ac4ec-209d-4423-b9be-f1cd6715509b)
![image](https://github.com/user-attachments/assets/cafe245f-68ef-4d60-a102-311817d5a8f1)





