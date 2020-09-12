from django.core import serializers

from model_repository.models import VwEmailSender


class ServiceRepository:
    def __init__(self, cursor):
        self.cursor = cursor

    def read_email_info(self):
        db_info = VwEmailSender.objects.using("postsql").all()
        serialized_obj = serializers.serialize('json', db_info)

        return serialized_obj

    def save_email_raw_data(self,raw_data):
        self.cursor.callproc(
            "insert_email_raw_data",
            [raw_data]
        )
        new_id = self.cursor.fetchone()[0]
        return new_id