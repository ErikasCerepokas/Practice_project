from django.db import models


class VwEmailSender(models.Model):
    id = models.IntegerField(db_column='ID', blank=True, null=False, primary_key=True)  # Field name made lowercase.
    sender = models.CharField(db_column='Sender', max_length=150, blank=True, null=True)  # Field name made lowercase.
    recepients = models.CharField(db_column='Recepients', max_length=10000, blank=True,
                                  null=True)  # Field name made lowercase.
    subject = models.CharField(db_column='Subject', max_length=200, blank=True, null=True)  # Field name made lowercase.
    message = models.CharField(db_column='Message', max_length=10000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'vw_email_sender'
