# -*- coding: utf-8 -*-

###
### DO NOT CHANGE THIS FILE
### 
### The code is auto generated, your change will be overwritten by 
### code generating.
###
from __future__ import absolute_import

from .api.timeslots import Timeslots
from .api.timeslots_doctorName import TimeslotsDoctorname
from .api.timeslots_reserve import TimeslotsReserve
from .api.timeslots_cancel import TimeslotsCancel
from .api.timeslots_check import TimeslotsCheck


routes = [
    dict(resource=Timeslots, urls=['/timeslots'], endpoint='timeslots'),
    dict(resource=TimeslotsDoctorname, urls=['/timeslots/<doctorName>'], endpoint='timeslots_doctorName'),
    dict(resource=TimeslotsReserve, urls=['/timeslots/reserve'], endpoint='timeslots_reserve'),
    dict(resource=TimeslotsCancel, urls=['/timeslots/cancel'], endpoint='timeslots_cancel'),
    dict(resource=TimeslotsCheck, urls=['/timeslots/check'], endpoint='timeslots_check'),
]