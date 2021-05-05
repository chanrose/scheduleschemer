from django.db import models
from django.contrib.auth.models import User
from picklefield.fields import PickledObjectField
# Create your models here.
class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    major = models.CharField(
        choices=[
            ("Information Technology", "IT"), 
            ("Accounting", "ACCT"), 
            ("TESOL", "TESOL"),
            ("Management", "MGNT"),
            ("Teaching", "TEACH"),
            ("Christian Studies", "CS"),
            ("Bioscience", "BIO"),
            ("Public Health", "PH"),
            ("MedTech", "MT"),
            ("English as a Second Language", "ESL"),
            ("Nursing", "NURS")
        ], max_length=50, default="English as a Second Language"
    )
    faculty = models.CharField(
        choices=[
            ("Arts & Humanities", "FAH"),
            ("Business Administration", "FBA"),
            ("Education", "FED"),
            ("Religious Studies", "FRS"),
            ("Science", "FOS"),
            ("Information Technology", "FIT"),
            ("Mission Faculty of Nursing", "MFN"),
        ], max_length=50, default="Arts & Humanities"
    )
    enrolled_course = PickledObjectField()

    def __str__(self):
        return "Username: {}, Major: {}".format(self.user.username, self.major)

class Course(models.Model):
    id =  models.CharField(max_length=10, primary_key=True)
    name =  models.CharField(max_length=50)
    credit = models.PositiveSmallIntegerField()
    lecturer = models.CharField(max_length=50)
    major = models.CharField(max_length=50)


class Class(models.Model):
    # id = models.ForeignKey(Course, on_delete=models.CASCADE, primary_key=True)
    # DayTime = {“Mon”:  [“Time
    # start”, “Time
    # end”], “Tues”: [“Time
    # start”, “Time
    # end”]}
    id = models.CharField(max_length=10, primary_key=True)
    availability = models.BooleanField(default=False)
    daytime = PickledObjectField()

    def __str__(self):
        return "name: {}, daytime: {}".format(self.id, self.daytime)