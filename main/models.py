from django.contrib.auth import admin
from django.db.models import *
from django.contrib.auth.models import *
from .admin import *


class DataUser(Model):
    id_user = OneToOneField(User, on_delete=CASCADE , primary_key=True)
    Logo = ImageField(upload_to='img/')
    Age = IntegerField()
    Status = CharField(max_length=50, null=True)


class Files(Model):
    id_DataUser = ForeignKey(DataUser, on_delete=CASCADE)
    file = FileField(upload_to='files/')

admin.site.register(DataUser)
admin.site.register(Files)