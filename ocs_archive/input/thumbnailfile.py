from ocs_archive.input.file import DataFile, File
from ocs_archive.settings import settings


class ThumbnailFile(DataFile):
    """The ThumbnailFile class is a subclass of DataFile that is used to store thumbnail images in an OCS Archive."""

    def __init__(self, open_file: File, file_metadata: dict = None, blacklist_headers: tuple = settings.HEADER_BLACKLIST, required_headers: tuple = settings.REQUIRED_THUMBNAIL_METADATA):
        """Loads in thumbnail file headers, then does some automatic cleanup and normalization of values."""
        super().__init__(open_file, file_metadata, blacklist_headers, required_headers)
        self._normalize_null_values()

    def _normalize_null_values(self):
        header_updates = {}
        #  Sometimes keywords use N/A to mean null
        for k, v in self.header_data.get_headers().items():
            if v in settings.NULL_HEADER_VALUES:
                if k in settings.INTEGER_TYPES:
                    header_updates[k] = None
                else:
                    header_updates[k] = ''
            # Catch None and NONE values for Integer type fields so they pass archive validation
            elif k in settings.INTEGER_TYPES and ('NONE' in str(v).upper()):
                header_updates[k] = None
        self.header_data.update_headers(header_updates)

    def get_filestore_path(self):
        return '/'.join((self.header_data.get_site_id(), self.header_data.get_instrument_id(), self.header_data.get_observation_day(), 'thumbnails', self.open_file.basename + self.open_file.extension))

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
