import speech_recognition as sr
from flask import Flask, request, render_template
from gtts import gTTS
import os
import playsound 
r = sr.Recognizer()

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == 'GET':
        return render_template("index.html")


@app.route('/output', methods=["GET", "POST"])
def output():
    try:
        with sr.Microphone() as source:
            audio = r.listen(source, timeout= 5)
            inp = r.recognize_google(audio)
            fin = operation(inp.lower())
            if fin != "error":
                return render_template("output.html", ans = inp, fin = fin)
            else:
                return render_template("apology.html")
    except Exception:
        return render_template("apology.html")

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
            if all(list(map(isDigit, i.split('/')))):
                x = list(map(float, i.split("/")))
                num.extend(x)
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
    return mytext

def operation(inp):    
    inp = inp.replace("minus ", " -")
    inp = inp.replace("negative ", " -")
    num = numbers(inp)
    if "percent" in inp or "percentage" in inp or "%" in inp:
        a=voice_out(percent(num))
    elif "power" in inp or "raised to" in inp:
        a=voice_out(power(num))
    elif "mod" in inp or "modulus" in inp or "modulo" in inp or "remainder" in inp:
        a=voice_out(mod(num))
    elif "root" in inp:
        a=voice_out(sq_root(num))
    elif "square" in inp or "itself" in inp:
        a=voice_out(square(num))
    elif "add" in inp or "+" in inp or "plus" in inp:
        a=voice_out(add(num))       
    elif "multiply" in inp or "times" in inp or "multiplied" in inp or "into" in inp or "x" in inp or "*" in inp:
        a=voice_out(multiply(num))    
    elif "divide" in inp or "by" in inp or "/" in inp or "bye" in inp:
        a=voice_out(divide(num))
    elif "subtract" in inp and "from" in inp:
        a=voice_out(subtract(num,flag=True)) #if flag is true num[1] - num[0]  
    elif "-" in inp or "minus" in inp:
        a=voice_out(subtract(num,flag=False)) #if flag is flase num[0] - num[1] 
    else:
        a = "error"
    return a

def add(num):
    total = sum(num)
    return total

def subtract(num,flag):
    if len(num) < 2:
        return "error"
    if flag == True:
        total = num[1] - num[0]
    else:
        total = num[0] - num[1]
    return total

def multiply(num):
    if len(num) < 2:
        return "error"
    total = 1
    for i in num:
        total *= i
    return total

def divide(num):
    if len(num) < 2:
        return "error"
    total = num[0] / num[1]
    return total

def mod(num):
    if len(num) < 2:
        return "error"
    total = num[0] % num[1]
    return total

def sq_root(num):
    if len(num) < 1:
        return "error"
    total = num[0] ** (1/2)
    return total

def square(num):
    if len(num) < 1:
        return "error"
    total = num[0] **2
    return total

def percent(num):
    if len(num) < 2:
        return "error"
    total = num[0] * num[1] / 100
    return total

def power(num):
    if len(num) < 2:
        return "error"
    total = num[0] ** num[1]
    return total
