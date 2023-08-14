import os
from io import BytesIO
from zipfile import ZipFile
from py7zr import SevenZipFile
from rarfile import RarFile


# Base class for file extraction
class FileExtractor:
    def __init__(self, file):
        self.file = file

    def extract(self):
        """
        Abstract method for extracting files from the archive.
        Subclasses must implement this method.
        """
        raise NotImplementedError


# Subclass for extracting files from ZIP archives
class ZIPFileExtractor(FileExtractor):
    """
    Class for working with ZIP archives
    """
    def extract(self):
        """
        Extracts files from a ZIP archive and returns a list of extracted file contents.
        """
        with ZipFile(self.file, 'r') as zip_file:
            return [{name.rsplit('/', 1)[-1]: BytesIO(zip_file.read(name))} for name in zip_file.namelist()
                    if not name.endswith('/')]


# Subclass for extracting files from 7z archives
class SevenZIPFileExtractor(FileExtractor):
    """
    Class for working with 7z archives
    """
    def extract(self):
        """
        Extracts files from a 7z archive and returns a list of extracted file contents.
        """
        with SevenZipFile(BytesIO(self.file.read())) as sevenzip_file:
            return [{filename.rsplit('/', 1)[-1]: bio} for filename, bio in sevenzip_file.readall().items()]
