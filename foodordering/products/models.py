from django.db import models # type: ignore
import uuid
# Create your models here.

# DRY => Do not repeat Yourself

# Python manage.py makemigrations

class BaseModel(models.Model):

    uid = models.UUIDField(default = uuid.uuid4 , editable = False , primary_key = True)

    created_at = models.DateField(auto_created=True)
    updated_at = models.DateField(auto_created=True)

    class Meta :
        abstract = True


class Product(BaseModel):
   
    product_name = models.CharField(max_length=255)
    product_slug = models.SlugField(unique=True)
    product_desc = models.TextField()
    product_price = models.IntegerField(default=0)
    product_demo_price = models.IntegerField(default=0)
    quantity = models.CharField(null=True ,blank=True ,max_length=100)
 

class productMetaInforamtion(BaseModel):
    product = models.OneToOneField(Product , on_delete=models.CASCADE , related_name="meta_info")
    product_measuring = models.CharField(max_length=100 , null=True ,blank=True , choices=(("KG" , "KG"),("ML" , "ML") ,("L" , "L"),(None , None)) )
    quantity = models.CharField(null=True ,blank=True , max_length=100)
    is_restrict = models.BooleanField(default=False)
    restrict_quantity = models.IntegerField()

class productImages(BaseModel):

    product = models.ForeignKey(Product , on_delete=models.CASCADE , related_name="images")
   
    product_images = models.ImageField(upload_to="products")

