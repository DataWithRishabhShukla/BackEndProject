from django.db import models
from django.db.models import CharField, IntegerField, DecimalField , TextField

# Create your models here.
class Category(models.Model):

    name = CharField(max_length=50)
    description = TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta :
        verbose_name_plural = "Categories"
        db_table = "menu_category"
        


class MenuItem(models.Model):
    name= CharField(max_length=100)
    description = TextField()
    price = DecimalField(max_digits=6,decimal_places=2)
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category,on_delete= models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


