from django.db import models

# Create your models here.

class contacts2(models.Model):
    name = models.CharField(max_length= 30)
    email = models.EmailField(max_length=254)
    desc = models.TextField(max_length = 500)
    phone = models.IntegerField()
    
def __str__(self):
    return self.name


class product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=100)
    category = models.CharField(max_length=100, default='')
    sub_category = models.CharField(max_length=100, default='')
    price = models.IntegerField(default=0)
    desc = models.TextField(max_length = 500)
    image = models.ImageField(upload_to='images/images', default= 'blank-profile-picture.png')


class Orders(models.Model):
    order_ID = models.AutoField
    item_json = models.CharField(max_length=100)
    amount = models.IntegerField
    name = models.CharField(max_length=100)
    email = models.EmailField
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.IntegerField
    payment_details = models.CharField(max_length=100)
    phone_number = models.IntegerField
    
    def __str__(self):
      return self.name
  
  
class OrderUpdate(models.Model):
    update_ID = models.AutoField
    order_ID = models.IntegerField
    update_desc = models.CharField(max_length=100)
    delivered = models.BooleanField
    timestamp = models.DateField
    
    def __str__(self):
        return self.name
    
