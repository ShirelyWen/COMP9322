from mongoengine import StringField, IntField, Document, EmbeddedDocument, ListField, EmbeddedDocumentField, FloatField

class Doctor(Document):
    id = IntField(required=True, primary_key=True)
    name = StringField(required=True, max_length=200)
    location = StringField(required=True, max_length=500)
    specialization = StringField(required=True, max_length=200)
    gender = StringField(required=True, max_length=200)

    def __init__(self,id, name, location, specialization, gender,*args, **values):
        super().__init__(*args, **values)
        self.id = id
        self.name = name
        self.location = location
        self.specialization = specialization
        self.gender = gender

class Timeslot(EmbeddedDocument):
    id = IntField(required=True, primary_key=True)
    doctorID = IntField(required=True, max_length=50)
    doctorName = StringField(required=True, max_length=200)
    day = StringField(required=True, max_length=200)
    hour = StringField(required=True, max_length=200)
    type = StringField(required=True, max_length=200)
    statusFlag = StringField(required=True, max_length=200)
    clientName = StringField(required=True, max_length=200)

    def __init__(self, id, doctorID, doctorName, day, hour, type, statusFlag, clientName, *args, **values):
        super().__init__(*args, **values)
        self.id = id
        self.doctorID = doctorID
        self.doctorName = doctorName
        self.day = day
        self.hour = hour
        self.type = type
        self.statusFlag = statusFlag
        self.clientName = clientName

