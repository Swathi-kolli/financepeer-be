from django.db import models

# Create your models here.

class UserModel(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True) 
    userId = models.IntegerField(db_column='USER_ID', blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='title', max_length=200, blank=True, null=True)  # Field name made lowercase.
    body = models.CharField(db_column='description', max_length=300, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'user_table'

