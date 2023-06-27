from django.db import models

# Create your models here.
class Accel(models.Model):
    x_accel = models.FloatField() 
    y_accel = models.FloatField() 
    z_accel = models.FloatField() 
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.x_accel} - {self.y_accel} - {self.z_accel} - {self.created_at}'


