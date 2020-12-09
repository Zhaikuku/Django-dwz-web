# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Liuxiangpinzhong(models.Model):
    # id = models.AutoField(db_column='ID')  # Field name made lowercase.
    liuxiangid = models.IntegerField(db_column='LiuXiangId')  # Field name made lowercase.
    spbh_c = models.CharField(db_column='Spbh_C', max_length=15)  # Field name made lowercase.
    shifoushengxiao = models.IntegerField(db_column='ShiFouShengXiao')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LiuXiangPinZHong'


    def __str__(self):
        return self.spbh_c

class Users(models.Model):
    # id = models.AutoField(db_column='ID')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50)  # Field name made lowercase.
    password = models.CharField(db_column='PassWord', max_length=50)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=50)  # Field name made lowercase.
    isok = models.BooleanField(db_column='IsOK')  # Field name made lowercase.
    liuxiangid = models.IntegerField(db_column='LiuXiangId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Users'

    def __str__(self):
        return '{} {} {}'.format(self.name, self.password, self.type)


class Idsp(models.Model):
    spid = models.CharField(primary_key=True, max_length=20)
    type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'idsp'


class Position(models.Model):
    spbh = models.CharField(max_length=500)
    spmch = models.CharField(max_length=500)
    shpgg = models.CharField(max_length=500)
    shengccj = models.CharField(max_length=500)
    shl = models.CharField(max_length=500)
    dwmch = models.CharField(max_length=500)
    sxrq = models.CharField(max_length=500)
    pihao2 = models.CharField(max_length=500)
    rkrq = models.CharField(max_length=500)
    id = models.CharField(max_length=500, primary_key=True)
    dw = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Position'


class Purchase(models.Model):
    spbh = models.CharField(max_length=500)
    spmch = models.CharField(max_length=500)
    shpgg = models.CharField(max_length=500)
    shengccj = models.CharField(max_length=500)
    shl2 = models.CharField(max_length=500)
    rq = models.CharField(max_length=500)
    sxrq = models.CharField(max_length=500)
    pihao2 = models.CharField(max_length=500)
    hshj = models.CharField(max_length=500)
    hsje = models.CharField(max_length=500)
    dwmch = models.CharField(max_length=500)
    dw = models.CharField(max_length=500, blank=True, null=True)

    # id = models.AutoField(db_column='ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Purchase'


class Sale(models.Model):
    spbh = models.CharField(max_length=500)
    spmch = models.CharField(max_length=500)
    shpgg = models.CharField(max_length=500)
    pihao2 = models.CharField(max_length=500)
    dwmch = models.CharField(max_length=500)
    rq = models.CharField(max_length=500)
    shl = models.CharField(max_length=500)
    hshj = models.CharField(max_length=500)
    hsje = models.CharField(max_length=500)
    sxrq = models.CharField(max_length=500)
    kaipy = models.CharField(max_length=500)
    shengccj = models.CharField(max_length=500)
    dw = models.CharField(max_length=500, blank=True, null=True)

    # id = models.AutoField(db_column='ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Sale'



