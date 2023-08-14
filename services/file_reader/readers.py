from django.conf import settings
import csv
from io import StringIO

from services.exceptions import MaximumNumberLogs


# Base class for reading files and parsing logs
class FileReader:
    def __init__(self, file, parser, record_limit=settings.DATA_UPLOAD_MAX_NUMBER_LOGS):
        """
        Initialize the FileReader.

        :param file: The file object to be read.
        :param parser: The parser function to extract log data from a row.
        :param record_limit: The maximum number of logs to read.
        """
        self.file = file
        self.parser = parser
        self.record_limit = record_limit

    def file_to_list(self):
        """
        Convert the file content to a list of parsed log data.

        :return: A list of parsed log data.
        """
        raise NotImplementedError  # subclasses must implement this method


# Subclass for reading CSV files and parsing logs
class CSVFileReader(FileReader):
    def file_to_list(self):
        """
        Convert the CSV file content to a list of parsed log data.

        :return: A list of parsed log data from the CSV file.
        """
        # get the name and content of the file
        file_name, file_obj = next(iter(self.file.items()))
        data = []
        with StringIO(file_obj.read().decode()) as csv_file:  # read and decode the file content
            csv_reader = csv.reader(csv_file, delimiter=',')  # create a CSV reader
            number_log = 0
            for row in csv_reader:
                # check if the maximum number of logs is exceeded
                if number_log > self.record_limit:
                    raise MaximumNumberLogs(self.record_limit)

                # parse the row and add log data to the list
                data.append(self.parser(row, file_name))
                number_log += 1

        # return the list of parsed log data
        return data
