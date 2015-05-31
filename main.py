import sys
import os

sys.path.insert(1, os.path.join(os.path.abspath('.'), 'venv/lib/python2.7/site-packages'))
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template("homepage.html")


@app.route('/response', methods=['POST'])
def postTesting():
    phrase = request.form['name']
    array = countSyllables(phrase)
    result = "Lower Estimate: {}".format(array[0]) + "\n Upper Estimate: {}".format(array[1])
    return render_template('response.html', result=result, phrase =phrase)


def isVowel(x):
    vowel = ['a', 'e', 'i', 'o', 'u', 'y']
    for v in vowel:
        if x == v:
            return True
    return False


def isConsonant(x):
    cons = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']
    for c in cons:
        if x == c:
            return True
    return False


def countSyllables(x):
    minVal = 0
    maxVal = 0
    index = 0

    if len(x) == 0:
        return minVal, maxVal

    if len(x) == 1 or len(x) == 2:
        if not (x[index] == ' '):
            minVal = 1
            maxVal = 1
            return minVal, maxVal

    if x[len(x) - 5:] == 'ucked':
        minVal -= 1
        maxVal -= 1

    while index < len(x):
        if isVowel(x[index]):
            minVal += 1
            maxVal += 1
        if index < len(x) - 1:
            if isVowel(x[index]) and isVowel(x[index + 1]):
                minVal -= 1
                maxVal -= 1
        index += 1

    if x[index - 1] == 'y' and x[index - 2] == 'l':
        if len(x) >= 3:
            minVal += 1
            maxVal += 1

    if x[index - 1] == 'e':
        if isConsonant(x[index - 2]):
            minVal -= 1
    return minVal, maxVal


if __name__ == '__main__':
    app.run()
