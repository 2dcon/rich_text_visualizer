import os
import string
from flaskr import constants
from flask import Flask, request, render_template
from datetime import datetime

here = os.path.dirname(__file__)

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True


def getCode(text):
    i = 0
    code = []
    while i < len(text):
        step = 1
        if text[i] in constants.SP_CHAR:
            code.append(text[i])
        elif text[i] == constants.DELIMITER[0]:
            if text[i + 1] == constants.DELIMITER[2] and text[i + 2] == constants.DELIMITER[1]:
                code.append(text[i:i + 3])
                step = 3
        elif text[i] == constants.DELIMITER[1]:
            h = text[i + 1:i + 7]
            if isHex(h):
                code.append(h)
                step = 8

        i += step

    return code


def checkCode(text0, text1, result):
    list0 = []
    list1 = []

    return


def convertEscape(text: string):
    new_text = text
    idx = 0
    while idx < len(new_text):
        nxt = idx + 1
        if new_text[idx] == '\\' and new_text[nxt] == 'n':
            new_text = new_text[:idx] + constants.NEWLINE + new_text[idx + 2:]
        idx += 1
    return new_text


def isHex(string6: string):
    if len(string6) == 6:
        for char in string6:
            if not (char in string.hexdigits):
                return False

    return True


def getHTML(hex_color: string):
    return '<h style="color:#' + hex_color + ';">'


def getRich(text: string):
    idx = 0
    rtxt: string = constants.TAG_P
    eot = len(text)

    while idx < eot:
        step = 1
        is_code = False
        if text[idx] == constants.DELIMITER[0]:
            opening = idx + 7
            closing = idx + 2

            if opening < eot and text[opening] == constants.DELIMITER[1]:
                hcode = text[idx + 1:opening]
                if isHex(hcode):
                    rtxt += getHTML(hcode)
                    step += 7
                    is_code = True
            if closing < eot and text[idx + 1] == constants.DELIMITER[2] and text[closing] == constants.DELIMITER[1]:
                rtxt += constants.TAG_CLOSE['h']
                step += 2
                is_code = True
        # regular text
        if not is_code:
            rtxt += text[idx]
        idx += step
        # reach eot

    rtxt += constants.TAG_CLOSE['p']
    return convertEscape(rtxt)


def genPage(code: string):
    page = open(here + '/templates/result.html', 'w')
    page.write(code)
    page.close()


if __name__ == "__main__":
    app.run(ssl_context='adhoc')


@app.route('/')
def index():
    print(getCode(constants.test1))
    return render_template('main.html')


@app.route('/', methods=['POST'])
def submit():
    raw0 = request.form['textbox_0']
    raw1 = request.form['textbox_1']

    rt0 = getRich(raw0)
    rt1 = getRich(raw1)

    page = constants.LINK + constants.div[0] + constants.div[1] + rt0 + constants.div[3] + constants.div[2] + rt1 \
           + constants.div[3] + constants.TAG_CLOSE['html']
    genPage(page)

    with open(here + '/stats/log', 'a') as rec:
        rec.write(datetime.now().strftime('%Y/%m/%d - %H:%M:%S: ') +
                  request.environ.get('HTTP_X_REAL_IP', request.remote_addr) + '\n' + raw0 + '\n' + raw1 + '\n\n' +
                  '=============================================================\n\n')

    return render_template('result.html')
