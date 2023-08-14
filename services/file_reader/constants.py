from services.file_reader.readers import CSVFileReader


# Dictionary of file extensions with corresponding reader classes
EXTENSION_READER_FILE = {
    'csv': CSVFileReader,  # reader of '.csv' files
}
