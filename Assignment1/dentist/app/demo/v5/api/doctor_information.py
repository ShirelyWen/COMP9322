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

class DoctorInformation(Resource):

    def post(self):
        print(g.json)
        connect(host='mongodb://shirleywen:wx20190331@ds017175.mlab.com:17175/shirely_doctor_database')
        name = request.json.get("name")
        location = request.json.get("location")
        specialization = request.json.get("specialization")
        gender = request.json.get("gender")
        name = string.capwords(name)
        id = 1
        for doctor in Doctor.objects:
            id = doctor.id + 1
        doc_info = Doctor(id, name, location, specialization, gender)
        doc_info.save()
        
        #print(g.json)
        
        return Response(response = json.dumps('Doctor information created, the id of this doctor is %d'%(id)), status=201)

