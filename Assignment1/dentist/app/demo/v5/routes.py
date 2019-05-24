# -*- coding: utf-8 -*-

###
### DO NOT CHANGE THIS FILE
### 
### The code is auto generated, your change will be overwritten by 
### code generating.
###
from __future__ import absolute_import

from .api.doctor_information import DoctorInformation
from .api.doctor_getinformation import DoctorGetinformation
from .api.doctor_available import DoctorAvailable


routes = [
    dict(resource=DoctorInformation, urls=['/doctor/information'], endpoint='doctor_information'),
    dict(resource=DoctorGetinformation, urls=['/doctor/getinformation'], endpoint='doctor_getinformation'),
    dict(resource=DoctorAvailable, urls=['/doctor/available'], endpoint='doctor_available'),
]