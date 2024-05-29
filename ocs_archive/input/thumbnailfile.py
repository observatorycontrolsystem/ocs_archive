from ocs_archive.input.file import DataFile
from ocs_archive.settings import settings


class ThumbnailFile(DataFile):
    """The ThumbnailFile class is a subclass of DataFile that is used to store thumbnail images in an OCS Archive."""
    
    @staticmethod
    def get_filestore_path(site_id: str, instrument_id: str, observation_day: str, filename: str):
        return '/'.join((site_id, instrument_id, observation_day, 'thumbnails', filename))

    def get_filestore_content_type(self):
        return f'image/{self.open_file.extension[1:]}'
    
    def _is_valid_file_metadata(self, metadata_dict: dict):
        """
        Check some file metadata for required headers.

        :param metadata_dict: dictionary of file metadata
        :return True if required headers are present, False if not
        """
        if any([k for k in settings.REQUIRED_THUMBNAIL_METADATA if k not in metadata_dict]):
            return False
        else:
            return True
