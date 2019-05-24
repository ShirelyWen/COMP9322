# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas
import requests
from flask import jsonify, Response
import requests
import json
import string


class Chatbot(Resource):

    def post(self):
        #print(g.json)
        result = requests.get('https://api.wit.ai/message?v=20190405&q={}'.format(g.json.get("message")),
                              headers={'Authorization': 'Bearer XAE7JFECWV3YFRRHCXRFRUG2R6UAPFO3'})
        jsonResult = result.json()
        print(jsonResult)
        print(jsonResult['entities']['intent'][0]['value'])
        if jsonResult['entities']['intent'][0]['value'] == 'GetGreetings':
            #greeting = jsonResult['entities']['response'][0]['value']
            return Response(response=json.dumps('Hi, do you have a preferred doctor? If yes, please provide me the doctor name. If no, just tell me no and I will send you the available doctor in our client now.'),status=200)

        elif jsonResult['entities']['intent'][0]['value'] == 'GetInformation':
            doctorName = jsonResult['entities']['doctorName'][0]['value']
            doctorName = string.capwords(doctorName)
            payload = {'doctorName': doctorName}
            #print(payload)
            result1 = json.loads(requests.get('http://127.0.0.1:5000/v5/doctor/getinformation', params=payload).content)
            return Response(json.dumps(result1))

        elif jsonResult['entities']['intent'][0]['value'] == 'MakeAppointment':
            clientName = jsonResult['entities']['patientName'][0]['value']
            doctorName = jsonResult['entities']['doctorName'][0]['value']
            timeID = jsonResult['entities']['timeID'][0]['value']
            clientName = string.capwords(clientName)
            doctorName = string.capwords(doctorName)
            print(clientName)
            print(doctorName)
            print(timeID)
            payload = {'clientName': clientName, 'doctorName': doctorName, 'timeID': timeID}
            print(payload)
            #url = 'http://127.0.0.1:5001/v6/timeslots/reserve/'
            result1 = json.loads(requests.get('http://127.0.0.1:5001/v6/timeslots/reserve', params=payload).content)
            return Response(json.dumps(result1))

        elif jsonResult['entities']['intent'][0]['value'] == 'CancelAppointment':
            clientName = jsonResult['entities']['patientName'][0]['value']
            doctorName = jsonResult['entities']['doctorName'][0]['value']
            timeID = jsonResult['entities']['timeID'][0]['value']
            clientName = string.capwords(clientName)
            doctorName = string.capwords(doctorName)
            print(clientName)
            print(doctorName)
            print(timeID)
            payload = {'clientName': clientName, 'doctorName': doctorName, 'timeID': timeID}
            print(payload)
            #url = 'http://127.0.0.1:5001/v6/timeslots/reserve/'
            result1 = json.loads(requests.get('http://127.0.0.1:5001/v6/timeslots/cancel', params=payload).content)
            print(result1)
            return Response(json.dumps(result1))

        elif jsonResult['entities']['intent'][0]['value'] == 'AskCancel':
            return Response(response=json.dumps('Yes, I am pleased to cancel the appointment for you. Please follow the below instruction to provide information to me: ' + '\n' + 'cancel: <your name>, <booking doctor name>, <time ID>' + '\n' +'please provide these information in order. Thank you.', status=200))

        elif jsonResult['entities']['intent'][0]['value'] == 'AvailavleDoctor':
            result1 = json.loads(requests.get('http://127.0.0.1:5000/v5/doctor/available').content)
            return Response(json.dumps(result1))

        elif jsonResult['entities']['intent'][0]['value'] == 'GetTimeslots':
            doctorName = jsonResult['entities']['doctorName'][0]['value']
            payload = {'doctorName': doctorName}
            result1 = json.loads(requests.get('http://127.0.0.1:5001/v6/timeslots', params=payload).content)
            return Response(json.dumps(result1))

        elif jsonResult['entities']['intent'][0]['value'] == 'GetCheck':
            doctorName = jsonResult['entities']['doctorName'][0]['value']
            day = jsonResult['entities']['day'][0]['value']
            hour = jsonResult['entities']['timeID'][0]['value']
            type = jsonResult['entities']['type'][0]['value']
            payload = {'doctorName': doctorName, 'day': day, 'hour': hour, 'type': type}
            result1 = json.loads(requests.get('http://127.0.0.1:5001/v6/timeslots/check', params=payload).content)
            return Response(json.dumps(result1))

        else:
            return Response(response=json.dumps('Sorry, I cannot handle your request, please follow the instrction. Thank you.'), status=400)