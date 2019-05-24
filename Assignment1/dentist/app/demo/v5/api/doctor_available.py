# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas
import requests
from mongoengine import connect
from flask import jsonify, Response
from .models import Doctor
import requests
import json

class DoctorAvailable(Resource):
    
    def get(self):
        connect(host='mongodb://shirleywen:wx20190331@ds017175.mlab.com:17175/shirely_doctor_database')
        check_dict = {"Monday": [], "Tuesday": [], "Wednesday": [], "Thursday": [], "Friday": []}
        available_doctor = []
        check_doctor = []
        for doctor in Doctor.objects:
            doctorName = doctor["name"]
            #print(doctorName)
            url = 'http://127.0.0.1:5001/v6/timeslots/' + str(doctorName)
            #print(url)
            result = json.loads(requests.get(url).content)
            #print(result)
            if result != check_dict:
                available_doctor.append((doctor["name"],doctor["location"],doctor["specialization"],doctor["gender"]))
        if available_doctor != check_doctor:
            #doctor = available_doctor[0][0] + ': '+ available_doctor[0][1]+','+available_doctor[0][2]+','+available_doctor[0][3]
            start = ''
            for doctor in available_doctor:
                output = start + doctor[0] + ': '+ doctor[1]+','+doctor[2]+','+doctor[3] + '\n'
                start = output
            return Response(response =json.dumps('You can choose the doctor below:'+'\n'+'%s'%(output)))
        
        return Response(response=json.dumps('There is no available doctor now.'))
