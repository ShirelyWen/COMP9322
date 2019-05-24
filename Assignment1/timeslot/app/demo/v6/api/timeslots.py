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

class Timeslots(Resource):
    
    def get(self):
        #print(g.args)
        connect(host='mongodb://shirleywen:wx20190331@ds121248.mlab.com:21248/shirely_timeslot_database')
        doctorName = g.args.get("doctorName")
        doctorName = string.capwords(doctorName)
        #print(doctorName)
        timeslot_dic = {"Monday": [], "Tuesday": [], "Wednesday": [], "Thursday": [], "Friday": []}
        check_dict = {"Monday": [], "Tuesday": [], "Wednesday": [], "Thursday": [], "Friday": []}
        flag = 'available'
        for timeslot in Timeslot.objects:
            if doctorName == timeslot["doctorName"] and flag == timeslot["statusFlag"]:
                timeslot_dic[timeslot["day"]].append("Timeslot "+str(timeslot["id"]) + ": " + timeslot["hour"] + " " + timeslot["type"])
        if timeslot_dic != check_dict:
            temp = ''
            for i in timeslot_dic:
                temp1 = temp + '\n' + i + ':'
                for j in timeslot_dic[i]:
                    output = temp1 + '(' + j + ')' + ','
                    temp1 = output
                temp = temp1
            print(temp)

            return Response(response=json.dumps('The available timeslots for doctor %s is below:'%(doctorName) + '\n' + temp))
        
        return Response(response=json.dumps('Time for this doctor is all reserved, please select another doctor.'))
    
    def post(self):
        print(g.json)
        connect(host='mongodb://shirleywen:wx20190331@ds121248.mlab.com:21248/shirely_timeslot_database')
        doctorID = request.json.get("doctorID")
        doctorName = request.json.get("doctorName")
        day = request.json.get("day")
        hour = request.json.get("hour")
        type = request.json.get("type")
        statusFlag = request.json.get("statusFlag")
        clientName = request.json.get("clientName")
        id = 1
        for time in Timeslot.objects:
            id = time.id + 1
        time_slot = Timeslot(id, doctorID, doctorName, day, hour, type, statusFlag, clientName)
        time_slot.save()
        print(time_slot)
        
        return Response(response=json.dumps('The timeslot for this doctor is created'), status=201)


