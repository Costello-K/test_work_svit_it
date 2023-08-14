from services.archive_extractor.constants import EXTENSION_LOG_FILE, EXTENSION_ARCHIVE_FILE


def archive_extractor(instance, file, log_extensions:list=EXTENSION_LOG_FILE, archive_extensions:dict=EXTENSION_ARCHIVE_FILE):
    """
    Extract files from an archive or handle a single log file.

    :param file: The file to be processed.
    :param log_extensions: A list of log file extensions.
    :param archive_extensions: A dictionary mapping archive extensions to corresponding extractors.
    :return: A list of extracted files' content.
    """
    # get the file extension
    ext = file.name.strip().split('.')[-1]
    if ext in log_extensions:  # check if it's a log file
        # return log file content
        return [{file.name: file}]
    elif ext in archive_extensions.keys():  # check if it's an archive file
        # call the appropriate extractor and return extracted files
        return archive_extensions[ext](file).extract()
    raise ValueError("Unsupported file type")
