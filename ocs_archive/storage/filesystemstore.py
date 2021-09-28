from io import BytesIO
from contextlib import contextmanager

from ocs_archive.storage.filestore import FileStore
from ocs_archive.input.file import DataFile
from ocs_archive.settings import settings

class FileSystemStore(FileStore):
    """
    This class stores the files locally on the file system, in the base directory
    specified
    """
    def __init__(self, root_dir: str = settings.FILESYSTEM_STORAGE_ROOT_DIR):
        super().__init__()
        self.root_dir = root_dir

    def store_file(self, data_file: DataFile):
        # TODO: store the file locally from the root_dir
        md5 = data_file.open_file.get_md5()
        return {
            'key': md5,
            'md5': md5,
            'extension': data_file.open_file.extension
        }

    def delete_file(self, path: str, version_id: str):
        pass

    def get_url(self, path: str, version_id: str, expiration: float):
        return ''

    @contextmanager
    def get_fileobj(self, path: str):
        # TODO: retrieve the file locally from the root_dir and return BytesIO
        try:
            fileobj = BytesIO()
            yield fileobj
        finally:
            fileobj.close()

    def get_file_size(self, path: str):
        return 0