from ocs_archive.input.lcofitsfile import LcoFitsFile
from ocs_archive.input.tarwithfitsfile import TarWithFitsFile
from ocs_archive.input.fitsfile import FitsFile
from ocs_archive.input.file import File, DataFile, FileSpecificationException

EXTENSION_TO_FILE_CLASS = {
    '.fits.fz': LcoFitsFile,
    '.fits': FitsFile,
    '.tar.gz': TarWithFitsFile,
    '.pdf': DataFile
}


class FileFactory:
    @staticmethod
    def get_datafile_class_for_extension(extension: str):
        if extension not in EXTENSION_TO_FILE_CLASS:
            raise FileSpecificationException(f'file extension {extension} is not a currently supported file type')
        return EXTENSION_TO_FILE_CLASS[extension]
