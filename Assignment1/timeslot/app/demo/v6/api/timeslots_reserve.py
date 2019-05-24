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

class TimeslotsReserve(Resource):

    def get(self):
        print(g.args)
        connect(host='mongodb://shirleywen:wx20190331@ds121248.mlab.com:21248/shirely_timeslot_database')
        timeID = g.args.get("timeID")
        doctorName = g.args.get("doctorName")
        clientName = g.args.get("clientName")
        doctorName = string.capwords(doctorName)
        clientName = string.capwords(clientName)
        for timeslot in Timeslot.objects:
            if timeslot["doctorName"] == doctorName:
                if timeslot["id"] == timeID:
                    if timeslot["statusFlag"] == "available":
                        timeslot.update(statusFlag="reserved")
                        timeslot.update(clientName=clientName)
                        return Response(response=json.dumps('Successful book. Your booking information is below: '+'\n'+'Name: %s, Doctor Name: %s, Timeslot ID: %s.' %(clientName,doctorName,timeID)+ '\n' +'Please remember your booking time Id, it will be used when you would like to cancel this appoingment. Thank you.'), status=201)
                    else:
                        return Response(response=json.dumps('This time is not available, please choose another one.'))
                else:
                    return Response(response=json.dumps('This time ID is invalid, please check. Thank you.'))
        return Response(response=json.dumps('This doctor is not available, please choose another one.'))

