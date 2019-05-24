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



class TimeslotsCheck(Resource):

    def get(self):
        print(g.args)
        connect(host='mongodb://shirleywen:wx20190331@ds121248.mlab.com:21248/shirely_timeslot_database')
        doctorName = g.args.get("doctorName")
        doctorName = string.capwords(doctorName)
        day = g.args.get("day")
        day = string.capwords(day)
        hour = g.args.get("hour")
        type = g.args.get("type")
        for timeslot in Timeslot.objects:
            if doctorName == timeslot["doctorName"] and day == timeslot["day"] and hour == timeslot["hour"] and type == timeslot["type"]:
                if timeslot["statusFlag"] == "available":
                    return Response(response=json.dumps('This time you choose is available. The time id is: %d.'%(timeslot["id"])+'\n'+'Would you like to book this timeslot for doctor %s?'%(doctorName)+'\n'+'If yes,please respond me the following information in order: <your name>,<doctor name>,<time id>'+'\n'+'If no, please respond: no, <doctor name>, I will provide you the available timeslots for this doctor.'+'\n'+'Thank you.'))

        return Response(response=json.dumps('This time is not available, Please choose another one.'))