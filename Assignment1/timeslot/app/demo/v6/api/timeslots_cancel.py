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


class TimeslotsCancel(Resource):

    def get(self):
        print(g.args)
        connect(host='mongodb://shirleywen:wx20190331@ds121248.mlab.com:21248/shirely_timeslot_database')
        doctorName = g.args.get("doctorName")
        clientName = g.args.get("clientName")
        timeID = g.args.get("timeID")
        doctorName = string.capwords(doctorName)
        clientName = string.capwords(clientName)
        print(doctorName)
        print(clientName)
        print(timeID)
        for timeslot in Timeslot.objects:
            if timeslot["id"] == timeID and timeslot["doctorName"] == doctorName:
                if timeslot["clientName"] == clientName:
                    timeslot.update(statusFlag="available")
                    timeslot.update(clientName="undefined")
                    return Response(response=json.dumps('Your appoinment is successfully cancelled.'),status=200)
                else:
                    return Response(response=json.dumps('You have no booking, please check again.'))

