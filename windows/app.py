import speech_recognition as sr
from flask import Flask, request, render_template
from gtts import gTTS
import os
import playsound 
r = sr.Recognizer()

app = Flask(__name__)

# @app.route('/', methods= ["GET", "POST"])
# def index():
#     pass

def isDigit(x):
    try:
        float(x)
        return True
    except ValueError:
        return False


def numbers(inp):
    num =[]
    for i in inp.split():
        if isDigit(i):
            num.append(float(i))
        if "%" in i:
            num.append(float(i[:len(i)-1]))
        if "/" in i:
            x = list(map(float, i.split("/")))
            num.extend(x)
    print(num)
    return num

def voice_out(num_mytext):
    if num_mytext == int(num_mytext):
        mytext = str(int(num_mytext))
    else:
        num_mytext = "{:.2f}".format(num_mytext)
        mytext = str(num_mytext)
    myobj = gTTS(text=mytext, lang='en', slow=False)  
    filename = 'output.mp3'
    myobj.save(filename)
    playsound.playsound(filename)
    print(mytext)

def operation(inp):    
    inp = inp.replace("minus ", " -")
    inp = inp.replace("negative ", " -")
    print(inp)
    num = numbers(inp)
    if "percent" in inp or "percentage" in inp or "%" in inp:
        voice_out(percent(num))
    elif "mod" in inp or "modulus" in inp or "modulo" in inp or "remainder" in inp:
        voice_out(mod(num))
    elif "root" in inp:
        voice_out(sq_root(num))
    elif "square" in inp or "itself" in inp:
        voice_out(square(num))
    elif "add" in inp or "+" in inp or "plus" in inp:
        voice_out(add(num))       
    elif "multiply" in inp or "times" in inp or "multiplied" in inp or "into" in inp or "x" in inp or "*" in inp:
        voice_out(multiply(num))    
    elif "divide" in inp or "by" in inp or "/" in inp or "bye" in inp:
        voice_out(divide(num))
    elif "subtract" in inp and "from" in inp:
        voice_out(subtract(num,flag=True)) #if flag is true num[1] - num[0]  
    elif "-" in inp or "minus" in inp:
        voice_out(subtract(num,flag=False)) #if flag is flase num[0] - num[1] 

def add(num):
    total = 0
    for i in num:
        total += i
    return total

def subtract(num,flag):
    if flag == True:
        total = num[1] - num[0]
    else:
        total = num[0] - num[1]
    return total

def multiply(num):
    
    total = 1
    for i in num:
        total *= i
    return total

def divide(num):
    total = num[0] / num[1]
    return total

def mod(num):
    total = num[0] % num[1]
    return total

def sq_root(num):
    total = num[0] ** (1/2)
    return total

def square(num):
    total = num[0] **2
    return total

def percent(num):
    total = num[0] * num[1] / 100
    return total

with sr.Microphone() as source:
    print("Kuch toh bolo, sharma kyu rahe ho")
    audio = r.listen(source)
    inp = r.recognize_google(audio)
    print(inp)
    operation(inp.lower())
