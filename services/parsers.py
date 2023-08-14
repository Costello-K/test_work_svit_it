
def parse_log_row(row):
    if len(row) >= 2:
        datetime_creating_log_str = row[0]
        log_text = row[1]
    else:
        raise ValueError('Log not founds')

    try:
        datetime_creating_log = parse(datetime_creating_log_str)
    except ValueError:
        raise ValueError('Date have incorrect type')

    return {
        'datetime_creating_log': datetime_creating_log,
        'log': log_text
    }
class ParserCSVFile:
    def __init__(self, line):
        self.line = line

    def line_to_tuple(self):
