import logging
from random import randint
from flask import Flask, render_template
from flask_ask import Ask, statement, question, session
from bs4 import BeautifulSoup
import urllib2
import random

app = Flask(__name__)
ask = Ask(app, "/")
logging.getLogger("flask_ask").setLevel(logging.DEBUG)

def generateInsults():
    insults = []
    for x in range(1,3):
        try :
            appx = str(x) + '/'
            if x == 1:
                appx = ''
            html = "http://onelinefun.com/insults/" + appx
            #print html
            web_page = urllib2.urlopen(html).read()
            soup = BeautifulSoup(web_page)
            for p in soup.findAll('div', {'class': 'oneliner'}):
                text = p.find('p').text.lower()
                if not "wife" in text and not "husband" in text and not "?" in text:
                    insults += [text]
        except urllib2.HTTPError :
            print("HTTPERROR!")
        except urllib2.URLError :
            print("URLERROR!")
    return insults

@ask.launch
def launch():
    speech_output = 'Insult master. Who do you need help insulting?'
    return question(speech_output).reprompt(speech_output)

@ask.intent('InsultIntent')
def insult(stname):
    insults = generateInsults()
    insult = insults[random.randint(0, len(insults) - 1)]
    #Replace the subject with our victim...
    insult = insult.replace("you'll",stname + " will").replace("Yo're",stname + "s").replace("You're",stname + "s").replace('your',stname + "s").replace('you',stname)
    text = render_template('insult', name=stname, insult=insult)
    return statement(text)

if __name__ == '__main__':
    app.run(debug=True)