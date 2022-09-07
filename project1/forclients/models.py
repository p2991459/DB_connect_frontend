from django.db import models


class Client_Info(models.Model):
    client_id = models.AutoField
    client_name = models.CharField(max_length=50)

    def __str__(self):
        return self.client_name