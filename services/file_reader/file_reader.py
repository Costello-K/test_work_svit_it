from services.file_reader.constants import EXTENSION_READER_FILE


def file_reader(instance, file, parser, reader_extensions=EXTENSION_READER_FILE):
    """
    Read and parse a file using an appropriate reader based on its extension.

    :param instance: The serializer instance.
    :param file: The file to be read and parsed.
    :param parser: The parser function to extract log data from a row.
    :param reader_extensions: A dictionary mapping file extensions to reader classes.
    :return: A list of parsed log data.
    """
    # get the name and content of the file
    file_name, file_obj = next(iter(file.items()))
    # get the file extension
    ext = file_name.strip().split('.')[-1]
    if ext in reader_extensions:  # check if the extension is supported by any reader
        # create an instance of the appropriate reader based on the file's extension
        reader = reader_extensions[ext](file, parser)
        # convert file to list
        return reader.file_to_list()
    raise ValueError("Unsupported file type")
