import os
from io import BytesIO
from zipfile import ZipFile
from py7zr import SevenZipFile
from rarfile import RarFile


class FileExtractor:
    def __init__(self, file):
        self.file = file

    def extract(self):
        raise NotImplementedError

class ZIPFileExtractor(FileExtractor):
    def extract(self):
        with ZipFile(self.file, 'r') as zip_file:
            return [BytesIO(zip_file.read(name)) for name in zip_file.namelist() if not name.endswith('/')]

class SevenZIPFileExtractor(FileExtractor):
    def extract(self):
        with SevenZipFile(BytesIO(self.file.read())) as sevenzip_file:
            return [bio for filename, bio in sevenzip_file.readall().items()]

class RARFileExtractor(FileExtractor):
    def extract(self):
        with RarFile(self.file, 'r') as rar_file:
            extracted_files = [BytesIO(rar_file.read(name)) for name in rar_file.namelist() if not name.endswith('/')]
            return extracted_files
