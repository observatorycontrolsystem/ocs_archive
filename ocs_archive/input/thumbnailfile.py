from ocs_archive.input.file import DataFile


class ThumbnailFile(DataFile):
    """The ThumbnailFile class is a subclass of DataFile that is used to store thumbnail images in an OCS Archive."""
    
    def get_filestore_path(self):
        return '/'.join((self.header_data.get_site_id(), self.header_data.get_instrument_id(), self.header_data.get_observation_day(), 'thumbnails', self.open_file.basename)) + self.open_file.extension

    def get_filestore_content_type(self):
        return f'image/{self.open_file.extension[1:]}'
