# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class Raw2012(models.Model):
    timestamp = models.CharField(max_length=45, blank=True)
    line_id = models.CharField(max_length=5, blank=True)
    direction = models.IntegerField(blank=True, null=True)
    journey_pattern_id = models.CharField(max_length=20, blank=True)
    time_frame = models.DateField(blank=True, null=True)
    vehicle_journey_id = models.IntegerField(blank=True, null=True)
    operator = models.CharField(max_length=5, blank=True)
    congestion = models.IntegerField(blank=True, null=True)
    lat = models.DecimalField(max_digits=12, decimal_places=10, blank=True, null=True)
    lon = models.DecimalField(max_digits=12, decimal_places=10, blank=True, null=True)
    delay = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    block_id = models.IntegerField(blank=True, null=True)
    vehicle_id = models.IntegerField(blank=True, null=True)
    stop_id = models.CharField(max_length=10, blank=True)
    at_stop = models.IntegerField(blank=True, null=True)
    unique_id = models.IntegerField(unique=True)
    class Meta:
        managed = False
        db_table = '2012_raw'

class Raw2013(models.Model):
    timestamp = models.CharField(max_length=45, blank=True)
    line_id = models.CharField(max_length=5, blank=True)
    direction = models.IntegerField(blank=True, null=True)
    journey_pattern_id = models.CharField(max_length=20, blank=True)
    time_frame = models.DateField(blank=True, null=True)
    vehicle_pattern_id = models.IntegerField(blank=True, null=True)
    operator = models.CharField(max_length=5, blank=True)
    congestion = models.IntegerField(blank=True, null=True)
    lat = models.DecimalField(max_digits=12, decimal_places=10, blank=True, null=True)
    lon = models.DecimalField(max_digits=12, decimal_places=10, blank=True, null=True)
    delay = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    block_id = models.IntegerField(blank=True, null=True)
    vehicle_id = models.IntegerField(blank=True, null=True)
    stop_id = models.CharField(max_length=10, blank=True)
    at_stop = models.IntegerField(blank=True, null=True)
    unique_id = models.IntegerField(unique=True)
    class Meta:
        managed = False
        db_table = '2013_raw'

# class Schedule2013(models.Model):
#     trip_id = models.CharField(max_length=30, blank=True)
#     route_short_name = models.CharField(max_length=4, blank=True)
#     arrival_time = models.TimeField(blank=True, null=True)
#     departure_time = models.TimeField(blank=True, null=True)
#     stop_id = models.CharField(max_length=20, blank=True)
#     name_without_locality = models.CharField(max_length=45, blank=True)
#     name = models.CharField(max_length=45, blank=True)
#     lat = models.CharField(max_length=45, blank=True)
#     lon = models.CharField(max_length=45, blank=True)
#     stop_sequence = models.IntegerField(blank=True, null=True)
#     stop_headsign = models.CharField(max_length=45, blank=True)
#     shape_dist_traveled = models.CharField(max_length=45, blank=True)
#     unique_id = models.IntegerField(unique=True)
#     class Meta:
#         managed = False
#         db_table = '2013_schedule'
#
# class AuthGroup(models.Model):
#     id = models.IntegerField(primary_key=True)
#     name = models.CharField(unique=True, max_length=80)
#     class Meta:
#         managed = False
#         db_table = 'auth_group'
#
# class AuthGroupPermissions(models.Model):
#     id = models.IntegerField(primary_key=True)
#     group = models.ForeignKey(AuthGroup)
#     permission = models.ForeignKey('AuthPermission')
#     class Meta:
#         managed = False
#         db_table = 'auth_group_permissions'
#
# class AuthPermission(models.Model):
#     id = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=50)
#     content_type = models.ForeignKey('DjangoContentType')
#     codename = models.CharField(max_length=100)
#     class Meta:
#         managed = False
#         db_table = 'auth_permission'
#
# class AuthUser(models.Model):
#     id = models.IntegerField(primary_key=True)
#     password = models.CharField(max_length=128)
#     last_login = models.DateTimeField()
#     is_superuser = models.IntegerField()
#     username = models.CharField(unique=True, max_length=30)
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
#     email = models.CharField(max_length=75)
#     is_staff = models.IntegerField()
#     is_active = models.IntegerField()
#     date_joined = models.DateTimeField()
#     class Meta:
#         managed = False
#         db_table = 'auth_user'
#
# class AuthUserGroups(models.Model):
#     id = models.IntegerField(primary_key=True)
#     user = models.ForeignKey(AuthUser)
#     group = models.ForeignKey(AuthGroup)
#     class Meta:
#         managed = False
#         db_table = 'auth_user_groups'
#
# class AuthUserUserPermissions(models.Model):
#     id = models.IntegerField(primary_key=True)
#     user = models.ForeignKey(AuthUser)
#     permission = models.ForeignKey(AuthPermission)
#     class Meta:
#         managed = False
#         db_table = 'auth_user_user_permissions'
#
# class DjangoAdminLog(models.Model):
#     id = models.IntegerField(primary_key=True)
#     action_time = models.DateTimeField()
#     user = models.ForeignKey(AuthUser)
#     content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
#     object_id = models.TextField(blank=True)
#     object_repr = models.CharField(max_length=200)
#     action_flag = models.IntegerField()
#     change_message = models.TextField()
#     class Meta:
#         managed = False
#         db_table = 'django_admin_log'
#
# class DjangoContentType(models.Model):
#     id = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=100)
#     app_label = models.CharField(max_length=100)
#     model = models.CharField(max_length=100)
#     class Meta:
#         managed = False
#         db_table = 'django_content_type'
#
# class DjangoSession(models.Model):
#     session_key = models.CharField(primary_key=True, max_length=40)
#     session_data = models.TextField()
#     expire_date = models.DateTimeField()
#     class Meta:
#         managed = False
#         db_table = 'django_session'
#
# class Weather2012(models.Model):
#     weather_id = models.IntegerField(primary_key=True)
#     date = models.CharField(max_length=100, blank=True)
#     time = models.CharField(max_length=100, blank=True)
#     summary = models.CharField(max_length=100, blank=True)
#     temp = models.FloatField(blank=True, null=True)
#     rain = models.FloatField(blank=True, null=True)
#     wind = models.FloatField(blank=True, null=True)
#     class Meta:
#         managed = False
#         db_table = 'weather2012'
#
# class Weather2013(models.Model):
#     weather_id = models.IntegerField(primary_key=True)
#     date = models.CharField(max_length=100, blank=True)
#     time = models.CharField(max_length=100, blank=True)
#     summary = models.CharField(max_length=100, blank=True)
#     temp = models.FloatField(blank=True, null=True)
#     rain = models.FloatField(blank=True, null=True)
#     wind = models.FloatField(blank=True, null=True)
#     class Meta:
#         managed = False
#         db_table = 'weather2013'

