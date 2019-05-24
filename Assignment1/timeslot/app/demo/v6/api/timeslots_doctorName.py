# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas
from mongoengine import connect
from flask import jsonify, Response
from .models import Timeslot
import requests
import json
import string


class TimeslotsDoctorname(Resource):
    
    def get(self, doctorName):
        connect(host='mongodb://shirleywen:wx20190331@ds121248.mlab.com:21248/shirely_timeslot_database')
        doctorName = request.view_args['doctorName']
        doctorName = string.capwords(doctorName)
        print(doctorName)
        timeslot_dic = {"Monday":[], "Tuesday":[], "Wednesday":[], "Thursday":[], "Friday": []}
        #check_dict = {"Monday":[], "Tuesday":[], "Wednesday":[], "Thursday":[], "Friday": []}
        flag = 'available'
        for timeslot in Timeslot.objects:
            if doctorName == timeslot["doctorName"] and flag==timeslot["statusFlag"]:
                timeslot_dic[timeslot["day"]].append(timeslot["hour"]+" "+timeslot["type"])
        return Response(json.dumps(timeslot_dic))



