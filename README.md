# DeepPi
Speech Recognition and Image Recognition Deep Learning on Raspberry Pi Zero W

This entire project will be written in Python, so it would be beneficial to have a basic understanding of Python and have Python3 downloaded on your computer and Raspberry Pi

***Please read [InitialSetup](https://github.com/michealcarac/DeepPi/blob/main/InitialSetup.md) first if haven't already***


## Getting Started
**For this project, you will need a few things**
1. A computer to install some programs on
2. A internet connection
3. A way to create a MicroSD card for the Zero W with SSH or VNC albeit another Raspberry Pi, hooking up some peripherals to the Zero, or some other way.
4. Components listed [Here](https://docs.google.com/spreadsheets/d/1M7MrT1gzgztbvuXfkKRB7sXJfgQoq0oRnmKZJjNunso/edit?usp=sharing)

**The following programs that will be used**
1. Keras
2. Docker
3. Jypter Notebook
4. Google Colab (Optional to Jypter Notebook if you don't want to train locally)
5. Tensorflow
6. Python3
7. OpenCV

**Now, only some of these programs will be needed on your Computer and some on your Raspberry Pi:**

**Computer:**
1. Keras
2. Docker
3. Jypter or Colab
4. Tensorflow
5. Anaconda

**Raspberry Pi Zero W:**
1. Tensorflow Lite
2. OpenCV

***Guide to install Keras, Docker, Jypter Notebook, Tensorflow, and Anaconda with a small example [Here](https://www.digikey.com/en/maker/projects/getting-started-with-machine-learning-using-tensorflow-and-keras/0746640deea84313998f5f95c8206e5b) Please only follow this guide to after you download Anaconda***

Note: When installing tensorflow in the Anaconda created environment, do 
```
$ conda install tensorflow
```
Instead of using ```pip``` as pip may cause a certificate issue
***Guide to install TensorFlow Lite on your Pi [Here](https://www.tensorflow.org/lite/guide/python)***

## Wake Word Model

The guide that we followed to create this can be found [Here](https://www.digikey.com/en/maker/projects/tensorflow-lite-tutorial-part-1-wake-word-feature-extraction/54e1ce8520154081a58feb301ef9d87a). All credit belongs to Shawn Hymel of Digi-Key. I strongly recommend checking out some of his other projects. 

Credit to his [Github](https://github.com/ShawnHymel/tflite-speech-recognition) for files that we edited for what we wanted. 

First, go to your created Anaconda environment, then install the ```python_speech_features``` from either pip or Anaconda with:
```
conda install -c bricew python_speech_features
```
### Training with Jupyter (Locally)
To train, we first need a dataset that we want to use. In this example, we will be using the Google Speech Commands Dataset found [Here](https://storage.cloud.google.com/download.tensorflow.org/data/speech_commands_v0.02.tar.gz).

Download and unzip the dataset. To learn more about this specific databse, go [Here](https://github.com/tensorflow/docs/blob/master/site/en/r1/tutorials/sequences/audio_recognition.md).

Now, we need to run a python script via Jupyter Notebook MFCC Extraction script

If you are on windows, open your Jupyter Notebook with Run, or if you are on Linux, open a terminal and type ```$ jupyter notebook``` and navigate to the folder with the files from this github.

Note: Make sure you open the Jupyter Notebook in the correct Anaconda environment (the one we created, ie: tensorflow)
#### File 1 
```
1mfcc_extraction_speech.ipynb
```
Note: Included in this github is a ```RemoveUnwantedWords.py``` this is meant to be placed inside of your dataset directory and ran with ```$ python3 RemoveUnwantedWords.py``` in a terminal that is in the same directory. This script will remove any words that you do not want (You will need to edit it). This works with the google dataset talked about before, and has not been tested on any other, please use at your own risk. We do this because if we do not care about a word, there is no point in keeping it in our dataset which will slow training down.  

Note: When you run the notebook, any errors for modules can be fixed by using Anaconda to download them, you may have to do this a few times. Also make sure you are in the correct Anaconda environment when you install these. Some packages that I find a little harder to install will have the download at the bottom of this instruction step.

1. Click on the play button and make sure there are no modules that are not present, if there is refer to above^
2. Before you run this one, you want to adjust the path to your filesystems path to the *datatset*
3. The rest can be run with no changes unless there is a module you need, then refer to above ^

In the end, you should have a npz file. 

If you cannot find the librosa package try this:
```
conda install -c conda-forge librosa
```
If you cannot find the PIL package try this:
```
conda install -c conda-forge pillow
```
If you cannot find the gi package try this:
```
conda install -c conda-forge pygobject
```
If you have issues with a namespace named "gst": (Note, this is on linux/Raspberry Pi, I'm not sure about it on Windows)
```
sudo apt install python3-gst-1.0
```
#### File 2
```
2mfcc_clasifier_speech.ipynb
```
1. Just make sure you have the modules installed in your Anaconda environment
2. Change the dataset_path variable to the path of your dataset
3. Change the feature_sets_path to the directory that holds the Jupyter Notebook and change feature_sets_filename to the npz file that we created in the first file. Also make sure you change the wake_word in this section to the one you desire (You need to train for each individual word)

Continue to run the rest of the cells, keep in mind the training may take a little bit





Now install Tensorflow lite on your Raspberry Pi with
