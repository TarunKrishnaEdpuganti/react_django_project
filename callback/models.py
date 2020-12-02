from django.db import models

class Auth(models.Model):
    mail = models.EmailField(null=True)
    storehash = models.CharField(max_length=1000, null=True)
    token = models.CharField(max_length=1000, null=True)


    def __str__(self):
        return str(self.mail)
