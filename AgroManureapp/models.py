from django.db import models

# Create your models here.
class products(models.Model):
  pro_name=models.CharField(max_length=255)
  pro_dis=models.TextField()
  pro_img=models.ImageField(upload_to='images_products')
  pro_price=models.DecimalField(max_digits=10,decimal_places=2,default=0.00)
  quantity=models.IntegerField(null=False,blank=False,default=0)
  status=models.BooleanField(default=False,help_text="0=default")
  def __str__(self):
    return self.pro_name

class Order_details(models.Model):
  username=models.CharField(max_length=255)
  Name=models.CharField(max_length=255)
  Address=models.TextField()
  phoneNo=models.CharField(max_length=10,default=0000000000)
  pincode=models.CharField(max_length=6,default=000000)
  product_id=models.IntegerField()
  product_name=models.CharField(max_length=255)
  quantity=models.IntegerField()
  priceperunit=models.IntegerField()
  totalprice=models.IntegerField()
  status=models.BooleanField(default=False,help_text="0=default")
  product_imgurl=models.CharField(default="abcd", max_length=400)
  def __str__(self):
    return self.Name