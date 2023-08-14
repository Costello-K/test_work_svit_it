import os
from zipfile import ZipFile
from py7zr import SevenZipFile
import rarfile

from services.archive_extractor.constants import EXTENSION_LOG_FILE, EXTENSION_ARCHIVE_FILE


class FileExtractor:
    def __init__(self, file):
        self.file = file

    def extract(self):
        raise NotImplementedError

class ZIPFileExtractor(FileExtractor):
    def extract(self):
        with ZipFile(self.file, 'r') as file:
            return [file.open(name) for name in file.namelist()]

class RARFileExtractor(FileExtractor):
    def extract(self):
        with rarfile.RarFile(self.file, 'r') as file:
            return [file.open(name) for name in file.namelist()]
import tempfile
class SevenZIPFileExtractor(FileExtractor):
    def extract(self):
        temp_dir = tempfile.mkdtemp()
        with SevenZipFile(self.file, 'r') as file:
            file.extractall(temp_dir)

        extracted_files = []
        for root, dirs, files in os.walk(temp_dir):
            for file_name in files:
                full_path = os.path.join(root, file_name)
                extracted_files.append(open(full_path, 'rb'))

        return extracted_files
    # def extract(self):
    #     with SevenZipFile(self.file, 'r') as file:
    #         return [file.open(name) for name in file.list()]


class ArchiveExtractor:
    def __init__(self, file, log_extensions:list=EXTENSION_LOG_FILE, archive_extensions:dict=EXTENSION_ARCHIVE_FILE):
        self.file = file
        self.log_extensions = log_extensions
        self.archive_extensions = archive_extensions

    def get_extract_files(self):
        ext = self.file.name.strip().split('.')[-1]
        if ext in self.log_extensions:
            return [self.file]
        elif ext in self.archive_extensions.keys():
            return [self.archive_extensions[ext](self.file).extract()]
        else:
            ValueError("Unsupported file type")


with open('../test.zip', 'rb') as file:
    print(ArchiveExtractor(file).extract_files())

with open('../test.7z', 'rb') as file:
    print(ArchiveExtractor(file).extract_files())

with open('../test.rar', 'rb') as file:
    print(ArchiveExtractor(file).extract_files())




import csv


# with open('test.zip', 'rb') as file:
#     for extracted_file in ArchiveExtractor(file).extract_files():
#         print(extracted_file)
#         yyy = [BytesIO(ZipFile(file).read(i)) for i in ZipFile(file).filelist]
#         with open(extracted_file, 'rb') as csv_file:
#             csv_reader = csv.reader(csv_file, delimiter=',')
#             for row in csv_reader:
#                 print(row)

def print_csv_contents_from_zip(zip_file_path):
    with zipfile.ZipFile(zip_file_path, 'r') as zip_file:
        for file_name in zip_file.namelist():
            if file_name.lower().endswith('.csv'):
                with zip_file.open(file_name, 'r') as csv_file:
                    csv_data = csv_file.read().decode('utf-8')
                    csv_reader = csv.reader(io.StringIO(csv_data))
                    print(f"Contents of {file_name}:")
                    for row in csv_reader:
                        print(row)

# Пример использования:
zip_file_path = 'путь_к_вашему_архиву.zip'
print_csv_contents_from_zip(zip_file_path)