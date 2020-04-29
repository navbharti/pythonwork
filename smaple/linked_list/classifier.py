#Open the classifier.py file and import turicreate by adding this line:
#import turicreate as turi

import turicreate as turi

#Next, let’s define the dataset path:

url = "dataset/"

#url = "dataset/"
#And then add the following line to find and load images from the dataset folder:

data = turi.image_analysis.load_images(url)

#data = turi.image_analysis.load_images(url)

#Continue to add the following line of code. We define image categories based on its folder path:
#data["foodType"] = data["path"].apply(lambda path: "Rice" if "rice" in path else "Soup")

data["foodType"] = data["path"].apply(lambda path: "Rice" if "rice" in path else "Soup")

#> Given an image, the goal of an image classifier is to assign it to one of a pre-determined number of labels.

#Lastly, save the new labeled dateset as rice_or_soup.sframe. We will use it to train the model
#data.save("rice_or_soup.sframe")

data.save("rice_or_soup.sframe")

#Preview the new labeled dataset on Turi Create
#data.explore()

data.explore()

#In the classifier.py file, we first load the previously saved rice_or_soup.sframe file. Insert the following line of code in the file:
#dataBuffer = turi.SFrame("rice_or_soup.sframe")

dataBuffer = turi.SFrame("rice_or_soup.sframe")
#Next, create training data using 90% of the dataBuffer object we just created and test data using the remaining 10%.
#trainingBuffers, testingBuffers = dataBuffer.random_split(0.9)

trainingBuffers, testingBuffers = dataBuffer.random_split(0.9)

#Continue to insert the following code to create the image classifier using the training data and SqueezeNet architecture:
#model = turi.image_classifier.create(trainingBuffers, target="foodType", model="squeezenet_v1.1")

model = turi.image_classifier.create(trainingBuffers, target="foodType", model="squeezenet_v1.1")

#Alternatively, you can use ResNet-50 for more accurate results:
#model = turi.image_classifier.create(trainingBuffers, target="foodType", model="resnet-50")

model = turi.image_classifier.create(trainingBuffers, target="foodType", model="resnet-50")

#Next, we will evaluate the test data to determine the model accuracy:
#evaluations = model.evaluate(testingBuffers)
#print evaluations["accuracy"]

evaluations = model.evaluate(testingBuffers)
print (evaluations["accuracy"])

#Lastly, insert the following code to save the model and export the image classification model as a CoreML model:
#model.save("rice_or_soup.model")
#model.export_coreml("RiceSoupClassifier.mlmodel")


model.save("rice_or_soup.model")
model.export_coreml("RiceSoupClassifier.mlmodel")