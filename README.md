# Voice Controlled Calculator

A Web based Voice Controlled Calculator

## Getting Started

Please make sure to do all of this before you run the code

### Prerequisites

* Python

* Flask

* gTTS

* Playsound (Only On Windows)

### Installing

#### Installing Flask

##### Mac

Type all of this in the terminal

```
$ pip3 install virtualen
$ mkdir voiceControlledCalculator
$ cd voiceControlledCalculator
$ virtualenv venv --system-site-packages
$ source venv/bin/activate
(venv) $ pip3 install Flask
```
##### Windows

```
$ pip3 install virtualenv
$ mkdir voiceControlledCalculator
$ cd voiceControlledCalculator
$ py -3 -m venv venv
$ venv\Scripts\activate
(venv) $ pip3 install flask
```
#### Installing gTTS

##### Mac
*HRISHIKESH*

##### Windows

```
$ pip install gTTS
```

#### Installing playsound (Only On Windows)

```
$ pip install playsound
```

## Running

##### Mac

Type all of this in the terminal

```
$ export FLASK_APP=app.py
$ flask run
```

##### Windows

```
$ flask run
````

Visit http://127.0.0.1:5000 to see the app running

## Usage

For Voice Recognition, it is recommended to begin questions with "What is..." for best results.
usage of the website is very straighforward, and any necessary instructions are provided on screen.

## Built with

* [Python](https://www.python.org/) - Programming Language used

* [Flask](https://flask.palletsprojects.com/en/1.1.x/) - The Web Framework used

* HTML - Markup Language used

* CSS - Style Sheet Language used


## Authors

* **Hrishikesh Mulkutkar**

* **Ayush Kapasi**

* **Adithya Neelakantan**
