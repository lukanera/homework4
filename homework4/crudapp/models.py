from django.db import models

class Test(models.Model):
    test_field = models.TextField(max_length=100)