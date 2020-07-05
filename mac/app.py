import speech_recognition as sr
from flask import Flask, request, render_template, redirect
import os

r = sr.Recognizer()

app = Flask(__name__)



@app.route("/", methods=["GET", "POST"])
def index():
    # if request.method == 'GET':
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
    print(num)
    return num



def voice_out(text):
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
        voice_out(mytext)
    elif "mod" in inp or "modulus" in inp or "modulo" in inp or "remainder" in inp:
        mytext = str(mod(num))
        voice_out(mytext)
    elif "root" in inp:
        mytext = str(sq_root(num))
        voice_out(mytext)
    elif "square" in inp or "itself" in inp:
        mytext = str(square(num))
        voice_out(mytext)
    elif "add" in inp or "+" in inp or "plus" in inp or "sum" in inp:
        mytext = str(add(num))
        voice_out(mytext)
    elif "multiply" in inp or "times" in inp or "multiplied" in inp or "into" in inp or 'x' in inp or '*' in inp or 'X' in inp or "product" in inp:
        mytext = str(multiply(num))
        voice_out(mytext)
    elif "divide" in inp or "by" in inp or "/" in inp or "bye" in inp or "quotient" in inp:
        mytext = str(divide(num))
        voice_out(mytext)
    elif "subtract" in inp and "from" in inp:
        mytext = str(subtract(num,flag=True)) #if flag is true num[1] - num[0]
        voice_out(mytext)
    elif "-" in inp or "minus" in inp or "difference" in inp:
        mytext = str(subtract(num,flag=False)) #if flag is flase num[0] - num[1]  
        voice_out(mytext)
    else:
        mytext = "error"
        voice_out(mytext)
    return mytext

def add(num):
    total = sum(num)
    if total == int(total):
        return int(total)
    return "{:.2f}".format(total)

def subtract(num,flag):
    if len(num) < 2:
        return "error"
    if flag == True:
        total = num[1] - num[0]
    else:
        total = num[0] - num[1]
    if total == int(total):
        return int(total)
    return "{:.2f}".format(total)

def multiply(num):
    if len(num) < 2:
        return "error"
    total = 1
    for i in num:
        total *= i
    if total == int(total):
        return int(total)
    return "{:.2f}".format(total)

def divide(num):
    if len(num) < 2:
        return "error"
    if num[1] == 0:
        return "Infinity"
    total = num[0] / num[1]
    if total == int(total):
        return int(total)
    return "{:.2f}".format(total)

def mod(num):
    if len(num) < 2:
        return "error"
    total = num[0] % num[1]
    if total == int(total):
        return int(total)
    return "{:.2f}".format(total)

def sq_root(num):
    if num[0] < 1:
        return "error"
    total = num[0] ** (1/2)
    if total == int(total):
        return int(total)
    return "{:.2f}".format(total)

def square(num):
    if len(num) < 1:
        return "error"
    total = num[0] **2
    if total == int(total):
        return int(total)
    return "{:.2f}".format(total)

def percent(num):
    if len(num) < 2:
        return "error"
    total = num[0] * num[1] / 100
    if total == int(total):
        return int(total)
    return "{:.2f}".format(total)
