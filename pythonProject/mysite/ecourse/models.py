from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField


# Create your models here.
class User(AbstractUser):
    pass


class BaseModel(models.Model):
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True
        ordering = ['id']


class Category(BaseModel):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Course(BaseModel):
    name = models.CharField(max_length=200)
    description = RichTextField()
    image = models.ImageField(upload_to='courses/%Y/%m')
    category = models.ForeignKey(Category, on_delete=models.RESTRICT)
    tags = models.ManyToManyField('Tag')

    def __str__(self):
        return self.name


class Lesson(BaseModel):
    name = models.CharField(max_length=100)
    description = RichTextField()
    image = models.ImageField(upload_to='lesson/%Y/%m')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)


    def __str__(self):
        return self.name


class Tag(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
