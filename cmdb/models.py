# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Class(models.Model):
    classid = models.IntegerField(primary_key=True)
    classname = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'class'


class EquipmentInfolist(models.Model):
    eil_id = models.AutoField(primary_key=True)
    equipment_id = models.CharField(max_length=50)
    equipment_name = models.CharField(max_length=50, blank=True, null=True)
    equipment_type = models.CharField(max_length=50, blank=True, null=True)
    equipment_company = models.CharField(max_length=50, blank=True, null=True)
    equipment_model = models.CharField(max_length=50, blank=True, null=True)
    equipment_specification = models.CharField(max_length=50, blank=True, null=True)
    equipment_parameter = models.CharField(max_length=50, blank=True, null=True)
    equipment_area_id = models.CharField(max_length=50, blank=True, null=True)
    equipment_status = models.CharField(max_length=50, blank=True, null=True)
    equipment_desc = models.CharField(max_length=100, blank=True, null=True)
    equipment_create_time = models.CharField(max_length=50, blank=True, null=True)
    remark = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'equipment_infolist'


class EquipmentStatuslist(models.Model):
    esl_id = models.AutoField(primary_key=True)
    equipment_id = models.CharField(max_length=50)
    equipment_status_name = models.CharField(max_length=50, blank=True, null=True)
    equipment_status_update_origin = models.CharField(max_length=50, blank=True, null=True)
    equipment_status_update_time = models.CharField(max_length=50, blank=True, null=True)
    equipment_status_update_user = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'equipment_statuslist'


class Income(models.Model):
    order_id = models.CharField(primary_key=True, max_length=11)
    order_type = models.CharField(max_length=255, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    remark = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'income'


class OrderInfo(models.Model):
    oil_id = models.AutoField(primary_key=True)
    order_id = models.CharField(max_length=50)
    area_id = models.CharField(max_length=50)
    order_type = models.CharField(max_length=50)
    car_status = models.CharField(max_length=50)
    start_location = models.CharField(max_length=50)
    end_location = models.CharField(max_length=50)
    car_rfid = models.CharField(db_column='car_RFID', max_length=50)  # Field name made lowercase.
    latest_arrivetime = models.CharField(max_length=50)
    order_source = models.CharField(max_length=50)
    order_description = models.CharField(max_length=50, blank=True, null=True)
    create_time = models.CharField(max_length=50)
    agv_type = models.CharField(max_length=50)
    osl = models.ForeignKey('OrderStatuslist', models.DO_NOTHING)
    remark = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_info'


class OrderStatuslist(models.Model):
    osl_id = models.AutoField(primary_key=True)
    order_status = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'order_statuslist'


class Student(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    pwd = models.CharField(max_length=20, blank=True, null=True)
    classid = models.ForeignKey(Class, models.DO_NOTHING, db_column='classid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student'


class User(models.Model):
    sid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    pwd = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'
