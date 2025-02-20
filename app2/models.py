from django.db import models

# Create your models here.



class State(models.Model):
    sname=models.CharField(max_length=20)


class Reg(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    gender=models.CharField(max_length=5)
    email=models.CharField(max_length=20)
    phon=models.BigIntegerField()
    addr=models.TextField()
    loc=models.CharField(max_length=20)



class Login(models.Model):
    uname=models.CharField(max_length=20)
    pword=models.CharField(max_length=20)
    utype=models.CharField(max_length=20)
    uid=models.ForeignKey(Reg,on_delete=models.CASCADE)

class addproduct(models.Model):
    pname = models.CharField(max_length=20)
    price = models.BigIntegerField()
    discription = models.TextField()
    category = models.CharField(max_length=20)
    image = models.FileField(upload_to='file')

class cart(models.Model):
    pid = models.ForeignKey('addproduct', on_delete=models.CASCADE,default=1) 
    quantity = models.IntegerField(default=1) 
    total=models.IntegerField(default=1)
    date=models.DateField(default='2000-02-02')
    uid=models.ForeignKey(Reg,on_delete=models.CASCADE,default=0)
    
class order_master(models.Model):
    date=models.DateField()
    uid=models.ForeignKey(Reg,on_delete=models.CASCADE)
    gtotal=models.IntegerField()

class order_child(models.Model):
    oid=models.ForeignKey(order_master,on_delete=models.CASCADE)
    pid=models.ForeignKey(addproduct,on_delete=models.CASCADE)
    qty=models.IntegerField()
    total=models.IntegerField()
    status=models.CharField(max_length=10)
