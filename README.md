# convert-handwritten-text-to-speech-translate-and-classify-it
This repository contains code and steps to detect handwritten text,convert it to speech,translate it and classify the text into 3 subject[physics,chemistry,biology] using google cloud platform

Create a billing/service account on google cloud platform for a minimal amount[free trial].
You get a credit of 300 dollars. 

Note : you need to have a google account of the same name of that on the credit card

Once you are done with that enable the following APIs
1) Cloud vision API

2) Text to speech API

3) Google translate

4) Natural language processing API



Create a project. Download the json file. You may need to have a bucket too[which is only possible if you have a billing account]

After you enable the API,just change the file path in the code and download all the images uploaded in the repository!

Link your json file in the code and then open command window as an administrator

Follow these steps :
Locate to the folder where you have downloaded the images and uploaded the code in the command window. Then you need to run the following commands:
1) scripts/activate
Note : Make sure you have installed pip

2)pip install google-cloud-vision

3)pip install google-text-to-speech

4)pip install google-translate

5)pip install google-natural-language


Once you have run the commands you need to run the code. 
You will be successfully be able to read the text from the image,and be able to get the translated audio and text of the handwritten text.

Now you will have to use vertex ai,auto ml model to upload the dataset from the repository. Train it 
Go to end points and you can see the predictions of the dataset as well as the accuracy.

You can either copy the recognised text and paste it in the endpoint[deploy and test] or try to link your output[the recognised text] as the input to your endpoint[we didn't want to waste more time trying to link it] so we did the former

Now you are able to successfully read the handwritten text,translate the text and get the audio and text form of it. And will also be able to classify the text if it belongs to Physics,chemistry or Biology







