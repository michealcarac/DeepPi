# DeepPi
Speech Recognition and Image Recognition Deep Learning on Raspberry Pi Zero W

This entire project will be written in Python, so it would be beneficial to have a basic understanding of Python and have Python3 downloaded on your computer and Raspberry Pi

***Please read [InitialSetup](https://github.com/michealcarac/DeepPi/blob/main/InitialSetup.md) first if haven't already***

The guide that we followed to create this can be found [Here](https://www.digikey.com/en/maker/projects/tensorflow-lite-tutorial-part-1-wake-word-feature-extraction/54e1ce8520154081a58feb301ef9d87a). All credit belongs to Shawn Hymel of Digi-Key. I strongly recommend checking out some of his other projects. 

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
1. Tensorflow
2. OpenCV

***Guide to install Keras, Docker, Jypter Notebook, Tensorflow, and Anaconda with a small example [Here](https://www.digikey.com/en/maker/projects/getting-started-with-machine-learning-using-tensorflow-and-keras/0746640deea84313998f5f95c8206e5b) Please only follow this guide to after you download Anaconda***
Note: When installing tensorflow in the Anaconda created environment, do 
```
$ conda install tensorflow
```
Instead of using ```pip```

## Wake Word Model

