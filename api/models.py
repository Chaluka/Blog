from django.db import models

# Create your models here.

class Post(models.Model):

    CATEGORY = (
        ('CPLUS', 'C++'),
        ('PYTHN', 'Python'),
        ('REACT', 'React'),
        ('MONGO', 'MongoDB'),
        ('JAVAS', 'JavaScript')
    )

    heading = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=5, choices=CATEGORY)
    content = models.CharField(max_length=500)
