from dateutil.parser import parse


def parse_row_to_date_log(instance, row, filename):
    """
    Parse a row of log data to extract datetime and log content.

    :param instance: Reference to the passed object instance.
    :param row: A row of log data.
    :param filename: The name of the file being parsed.
    :return: A dictionary containing parsed log information.
    """
    if len(row) < 2:
        raise ValueError('Log not found')

    try:
        # parsing a string into a datetype
        datetime_creating_log = parse(row[0])
    except ValueError:
        raise ValueError('Date have incorrect type')

    # object to write to the database
    return {
        'datetime_creating_log': datetime_creating_log,
        'log': row[1],
        'user': instance.context['request'].user,
        'filename': filename,
    }
