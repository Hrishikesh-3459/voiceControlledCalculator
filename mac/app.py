import speech_recognition as sr
from flask import Flask, request, render_template
import os
import time

r = sr.Recognizer()

app = Flask(__name__)



@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == 'GET':
        return render_template("index.html")


@app.route('/output', methods=["GET", "POST"])
def output():
    with sr.Microphone() as source:
        audio = r.listen(source)
        inp = r.recognize_google(audio)
        fin = operation(inp.lower())
        # render_template("output.html", ans = inp, fin = fin)
        # voice_out(fin)
        return render_template("output.html", ans = inp, fin = fin)


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
    print(num)
    return num



def voice_out(text):
    # time.sleep(3)
    if '-' in text:
        os.system(f"say minus") 
        tmp = text.replace('-', "")
        os.system(f"say {tmp}") 
    else:
        os.system(f"say {text}") 


def operation(inp):
    inp = inp.replace("minus ", " -")
    inp = inp.replace("negative ", " -")
    num = numbers(inp)
    if "percent" in inp or "percentage" in inp or "%" in inp:
        mytext = str(percent(num))
        print(mytext)
        voice_out(mytext)
    if "mod" in inp or "modulus" in inp or "modulo" in inp or "remainder" in inp:
        mytext = str(mod(num))
        print(mytext)
        voice_out(mytext)
    elif "root" in inp:
        mytext = str(sq_root(num))
        print(mytext)
        voice_out(mytext)
    elif "square" in inp or "itself" in inp:
        mytext = str(square(num))
        print(mytext)
        voice_out(mytext)
    elif "add" in inp or "+" in inp or "plus" in inp:
        mytext = str(add(num))
        print(mytext)
        voice_out(mytext)
    elif "multiply" in inp or "times" in inp or "multiplied" in inp or "into" in inp or 'x' in inp or '*' in inp or 'X' in inp:
        mytext = str(multiply(num))
        print(mytext)
        voice_out(mytext)
    elif "divide" in inp or "by" in inp or "/" in inp or "bye" in inp:
        mytext = str(divide(num))
        print(mytext)
        voice_out(mytext)
    elif "subtract" in inp and "from" in inp:
        mytext = str(subtract(num,flag=True)) #if flag is true num[1] - num[0]
        print(mytext)
        voice_out(mytext)
    elif "-" in inp or "minus" in inp:
        mytext = str(subtract(num,flag=False)) #if flag is flase num[0] - num[1]  
        print(mytext)
        voice_out(mytext)
    return mytext

def add(num):
    total = sum(num)
    if total == int(total):
        return int(total)
    return "{:.2f}".format(total)

def subtract(num,flag):
    if flag == True:
        total = num[1] - num[0]
    else:
        total = num[0] - num[1]
    if total == int(total):
        return int(total)
    return "{:.2f}".format(total)

def multiply(num):
    total = 1
    for i in num:
        total *= i
    if total == int(total):
        return int(total)
    return "{:.2f}".format(total)

def divide(num):
    if num[1] == 0:
        return "Not Possible"
    total = num[0] / num[1]
    if total == int(total):
        return int(total)
    return "{:.2f}".format(total)

def mod(num):
    total = num[0] % num[1]
    if total == int(total):
        return int(total)
    return "{:.2f}".format(total)

def sq_root(num):
    total = num[0] ** (1/2)
    if total == int(total):
        return int(total)
    return "{:.2f}".format(total)

def square(num):
    total = num[0] **2
    if total == int(total):
        return int(total)
    return "{:.2f}".format(total)

def percent(num):
    total = num[0] * num[1] / 100
    if total == int(total):
        return int(total)
    return "{:.2f}".format(total)

# with sr.Microphone() as source:
#     print("Speak Now")
#     audio = r.listen(source)
#     inp = r.recognize_google(audio)
#     print(inp)
#     operation(inp.lower())