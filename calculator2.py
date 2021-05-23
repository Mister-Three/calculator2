import math
import time
import webbrowser
print("Hello, what shall you be refered to as?")
user_name = input()
print("Hello, " + user_name)
print("Welcome to M3r_\'s math problem solver")
time.sleep(1)
print("+, -, *, /, **, pi, help")
time.sleep(1)
while True:
    calc = input("What type of equation are we going today?\n")
    if calc == '+':
        ask1 = input("Input the first number: ")
        ask2 = input("Input the second number: ")
        ask1 = int(ask1)
        ask2 = int(ask2)
        print(ask1 + ask2)
    if calc == '-':
        ask1 = input("Input the first number: ")
        ask2 = input("Input the second number: ")
        ask1 = int(ask1)
        ask2 = int(ask2)
        print(ask1 - ask2)
    if calc == '*':
        ask1 = input("Input the first number: ")
        ask2 = input("Input the second number: ")
        ask1 = int(ask1)
        ask2 = int(ask2)
        print(ask1 * ask2)
    if calc == '/':
        ask1 = input("Input the first number: ")
        ask2 = input("Input the second number: ")
        ask1 = float(ask1)
        ask2 = float(ask2)
        print(ask1 / ask2)
    if calc == '**':
        ask1 = input("Input the first number: ")
        ask2 = input("Input the second number: ")
        ask1 = int(ask1)
        ask2 = int(ask2)
        print(ask1 ** ask2)
    if calc == 'pi':
        print(math.pi)
    if calc == 'help':
        URL = 'https://github.com/Mister-Three/calculator2/wiki'
        webbrowser.open(URL)
    close = input("Do you want to close this tab? Y/N \n")
    if close == 'Y':
        exit()
    elif close == 'N':
        print("Continuing...")
        time.sleep(1)
