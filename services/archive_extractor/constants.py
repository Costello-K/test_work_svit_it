from services.archive_extractors import ZIPFileExtractor, SevenZIPFileExtractor, RARFileExtractor


EXTENSION_LOG_FILE = ['csv']
EXTENSION_ARCHIVE_FILE = {
    'zip': ZIPFileExtractor,
    '7z': SevenZIPFileExtractor,
    'rar': RARFileExtractor,
}