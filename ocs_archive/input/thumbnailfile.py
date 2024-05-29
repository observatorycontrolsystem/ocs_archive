from ocs_archive.input.file import DataFile
from ocs_archive.settings import settings


class ThumbnailFile(DataFile):
    """The ThumbnailFile class is a subclass of DataFile that is used to store thumbnail images in an OCS Archive."""
    
    def get_filestore_path(self):
        return self.get_filestore_path_from_frame_metadata(self.header_data.get_site_id(), self.header_data.get_instrument_id(), 
                                                           self.header_data.get_observation_day(), self.open_file.basename + self.open_file.extension)
    
    @staticmethod
    def get_filestore_path_from_frame_metadata(site_id: str, instrument_id: str, observation_day: str, filename: str):
        """
        Used to generate a filestore path from minimal frame metadata. This is useful when the full header information
        is not readily available.
        """
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
