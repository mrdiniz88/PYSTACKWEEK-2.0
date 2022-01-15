from django.db import models
from django.contrib.auth.models import User

class Image(models.Model):
    img = models.ImageField(upload_to='img')
    
    def __str__(self) -> str:
        return self.img.url


class City(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.name

class DayVisit(models.Model):
    choices = (('Monday', 'Monday'),('Tuesday', 'Tuesday'),('Wendnesdat', 'Wendnesdat'),('Thursday', 'Thursday'),('Friday', 'Friday'),('Saturday','Saturday'),('Sunday', 'Sunday'))
    
    day = models.CharField(max_length=20, choices=choices)

    def __str__(self) -> str:
        return self.day


class Timetable(models.Model):
    timetable = models.TimeField()

    def __str__(self) -> str:
        return str(self.timetable)


class Building(models.Model):
    choices = (('S', 'Sale'), ('R', 'Rent'))
    
    choices_building = (('A', 'Apartment'), ('H', 'House'))

    images = models.ManyToManyField(Image)
    value = models.FloatField()
    rooms = models.IntegerField()
    size = models.FloatField()
    city = models.ForeignKey(City, on_delete=models.DO_NOTHING)
    street = models.CharField(max_length=50)
    kind = models.CharField(max_length=1, choices=choices)
    immovable_type = models.CharField(max_length=1, choices=choices_building)
    number = models.IntegerField()
    description = models.TextField()
    visit_days = models.ManyToManyField(DayVisit)
    timetables = models.ManyToManyField(Timetable)

    def __str__(self) -> str:
        return self.street


class Visits(models.Model):
    choices = (('Monday', 'Monday'),('Tuesday', 'Tuesday'),('Wendnesdat', 'Wendnesdat'),('Thursday', 'Thursday'),('Friday', 'Friday'),('Saturday','Saturday'),('Sunday', 'Sunday'))

    choices_status = (('S', 'Scheduled'),('F', 'Finalized'),('C', 'Canceled'))

    building = models.ForeignKey(Building, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    day = models.CharField(max_length=20, choices=choices)
    timetable = models.TimeField()
    status = models.CharField(max_length=1, choices=choices_status, default='S')

    def __str__(self) -> str:
        return self.user.username