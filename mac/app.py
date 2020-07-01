import speech_recognition as sr
from flask import Flask, request, render_template
import os


r = sr.Recognizer()

app = Flask(__name__)



# @app.route('/', methods=["GET", "POST"])
# def index():
#     if request.method == 'GET':
#         return render_template("index.html")

# @app.route('/output', methods=["GET", "POST"])
# def output():
#     with sr.Microphone() as source:
#         audio = r.listen(source)
#         inp = r.recognize_google(audio)
#         # print(inp)
#         # operation(inp.lower())
#         return render_template("output.html", ans = inp)


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
    print(num)
    return num


def operation(inp):
    num = numbers(inp)
    if "mod" in inp or "modulus" in inp or "modulo" in inp or "remainder" in inp:
        mytext = str(mod(num))
        print(mytext)
        os.system(f"say {mytext}")
    elif "root" in inp:
        mytext = str(sq_root(num))
        print(mytext)
        os.system(f"say {mytext}")
    elif "square" in inp or "itself" in inp:
        mytext = str(square(num))
        print(mytext)
        os.system(f"say {mytext}")
    elif "add" in inp or "+" in inp or "plus" in inp:
        mytext = str(add(num))
        print(mytext)
        os.system(f"say {mytext}")
    elif "subtract" in inp and "from" in inp:
        mytext = str(subtract(num,flag=True)) #if flag is true num[1] - num[0]
        print(mytext)
        if '-' in mytext:
            os.system(f"say minus") 
            mytext = mytext.replace('-', "")
            os.system(f"say {mytext}") 
        else:
            os.system(f"say {mytext}") 

        os.system(f"say {mytext}") 
    elif "-" in inp or "minus" in inp:
        mytext = str(subtract(num,flag=False)) #if flag is flase num[0] - num[1]  
        print(mytext)
        if '-' in mytext:
            os.system(f"say minus") 
            mytext = mytext.replace('-', "")
            os.system(f"say {mytext}") 
        else:
            os.system(f"say {mytext}")    
    elif "multiply" in inp or "times" in inp or "multiplied" in inp or "into" in inp or 'x' in inp or '*' in inp or 'X' in inp:
        mytext = str(multiply(num))
        print(mytext)
        if '-' in mytext:
            os.system(f"say minus") 
            mytext = mytext.replace('-', "")
            os.system(f"say {mytext}") 
        else:
            os.system(f"say {mytext}") 
    elif "divide" in inp or "by" in inp or "/" in inp:
        mytext = str(divide(num))
        print(mytext)
        os.system(f"say {mytext}")

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

with sr.Microphone() as source:
    print("Speak Now")
    audio = r.listen(source)
    inp = r.recognize_google(audio)
    print(inp)
    operation(inp.lower())
