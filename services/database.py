from django.db import transaction

from api_v1.models import Log


def get_all_logs():
    """
    Retrieve all logs from the database.

    :return: Queryset containing all logs.
    """
    return Log.objects.all()

def create_logs_transaction(data_logs):
    """
    Create logs using a database transaction.

    :param data_logs: A list of dictionaries containing log data.
    :type data_logs: list
    """
    with transaction.atomic():
        # use bulk_create to efficiently insert multiple log instances in a single query
        Log.objects.bulk_create([Log(**log) for log in data_logs])
