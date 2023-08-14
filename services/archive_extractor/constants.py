from services.archive_extractor.extractors import ZIPFileExtractor, SevenZIPFileExtractor


# List of allowed log file extensions
EXTENSION_LOG_FILE = ['csv']
# Dictionary of archive file extensions with corresponding extractor classes
EXTENSION_ARCHIVE_FILE = {
    'zip': ZIPFileExtractor,      # extractor for ZIP archives
    '7z': SevenZIPFileExtractor,  # extractor for 7z archives
}
