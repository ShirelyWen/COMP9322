# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas
from mongoengine import connect
from flask import jsonify, Response
from .models import Doctor
import requests
import json
import string



class DoctorGetinformation(Resource):

    def get(self):
        print(g.args)
        connect(host='mongodb://shirleywen:wx20190331@ds017175.mlab.com:17175/shirely_doctor_database')
        info = []
        doctorName = g.args.get("doctorName")
        doctorName = string.capwords(doctorName)
        #info={'id':'', 'name':'', 'location':'', 'specialization':'', 'gender':''}
        for doctor in Doctor.objects:
            if doctorName == doctor["name"]:
                for i in doctor:
                    info.append((i,doctor[i]))
            # a = str(result1[0][0]) + ':' + str(result1[0][1])
            print(info)
            if info != []:
                b = str(info[1][0]) + ':' + str(info[1][1])
                c = str(info[2][0]) + ':' + str(info[2][1])
                d = str(info[3][0]) + ':' + str(info[3][1])
                e = str(info[4][0]) + ':' + str(info[4][1])
                output = '\n' + b + '\n' + c + '\n' + d + '\n' + e
                #return Response(response=json.dumps('Information of Doctor %s is below:' % (doctorName) + '\n' + '%s' % (output)))
                return Response(response=json.dumps(
                    'Information of Doctor %s is below:' % (doctorName) + '\n' + '%s' % (output) + '\n' + 'Do you have a preferred time? If yes, please provide me your selected doctor name and your preferred time, like 9 am, I will check for you.' + '\n' + 'If not, please respond "no, <doctor name>",I will provide you the available timeslots for you to choose.'),
                                status=200)
    
        return Response(response=json.dumps('There is no doctor named %s in our clinic. Please check and choose another one'), status=200)

