from django.db import models

# Create your models here.
class Category(models.Model):
    name= models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Book(models.Model):
    state_list=[
        ('available','available'),
        ('rental','rental'),
        ('sold','sold')
    ]
    title= models.CharField(max_length=250)
    author= models.CharField(max_length=250,null=True,blank=True)
    photo_book= models.ImageField(upload_to='photos',null=True,blank=True)
    photo_author= models.ImageField(upload_to='photos',null=True,blank=True)
    pages= models.IntegerField(null=True,blank=True)
    price= models.DecimalField(max_digits=3,decimal_places=3,null=True,blank=True)
    rental_price_day= models.DecimalField(max_digits=3,decimal_places=3,null=True,blank=True)
    rental_period= models.IntegerField(null=True,blank=True)
    total_rental= models.DecimalField(max_digits=3,decimal_places=3,null=True,blank=True) # new
    active= models.BooleanField(default=True)
    state= models.CharField(max_length=50,choices= state_list,null=True,blank=True)
    Category= models.ForeignKey(Category,on_delete=models.PROTECT) # manhebech el book yetfasakh kel category tetfasakh

    def __str__(self):
        return self.title