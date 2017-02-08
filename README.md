---
title: Alexa Lesson
duration: "1:30"
creator:
    name: Brad Zimmerman
    city: ATL
---

# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Alexa Lesson

## Introduction
Welcome to the Alexa Lesson. Today we are going to figure out how the Alexa bot works and functions!

### Tutorial - Memory Game
<b>The files for this app are provided in a folder called memory.</b>

To start out, let's navigate to a great tutorial on how to set up the software by [John Wheeler](https://alexatutorial.com/). His github project is called [Flask Ask](https://github.com/johnwheeler/flask-ask) and has a very simple interface for rapid development. Please navigate [here](https://developer.amazon.com/blogs/post/Tx14R0IYYGH3SKT/Flask-Ask-A-New-Python-Framework-for-Rapid-Alexa-Skills-Kit-Development) to follow along with the tutorial.

### Amazon Alexa Dashboard - Insult Generator
<b>The files for this app are in a folder called insulter.</b>

Follow the same steps as the app above until you get to the Alexa Dashboard

* Click on Alexa Skills Kit
* Click on "Add a new skill", call it 'Insult'. Make the invocation name 'Insult' as well.
* Click NEXT
* Copy the following code into the "Intent Schema" field:

```
{
    "intents": [{
        "intent": "InsultIntent",
        "slots": [{
            "name": "stname",
            "type": "CLASS_ROSTER"
        }]
    }]
}
```

* Click on 'Add Slot Type' and call your new slot 'CLASS_ROSTER'.
* Add your names separated by a new line for the people you'd like to insult. Here's a list from my previous class.

  ```
  AUSTRALIAN MATT
  AMERICAN MATT
  MATT
  COREY
  DAN
  SHETTY
  FEI
  JESSE
  QINGQING
  BRAD
  AUDREY
  BETH
  ```

* Add this to the sample utterances:

  ```
  InsultIntent {stname}
  InsultIntent insult {stname}
  InsultIntent please insult {stname}  
  InsultIntent would you kindly insult {stname}
  ```

* Click NEXT
* Add your ngrok endpoint to the endpoint field and make sure the endpoint type is https
* Click NEXT
* For SSL select: 'My development endpoint is a sub-domain of a domain that has a wildcard certificate from a certificate authority'
* Click NEXT
* You should be good to go! You're going to test out your new app here
