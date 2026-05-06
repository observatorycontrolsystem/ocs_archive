from ocs_archive.input.fitsfile import FitsFile
from ocs_archive.input.file import File
from ocs_archive.settings import settings

SOAR_PREFIX_TO_RLEVEL = {
    'cfzst': 62,
    'ecfzst': 63,
    'wecfzst': 64
}

class SOARFitsFile(FitsFile):
    def __init__(self, open_file: File, file_metadata: dict = None, blacklist_headers: tuple = settings.HEADER_BLACKLIST, required_headers: tuple = settings.REQUIRED_HEADERS):
        """SOAR AEON specific FitsFile format, provides some extra repair for broken headers from the filename."""
        super().__init__(open_file, file_metadata, blacklist_headers, required_headers)
        self._repair_reduction_level()

    def _repair_reduction_level(self):
        # For SOAR AEON data, even if the reduction level is set it may be wrong so we should attempt to set it
        # from the filename prefix, otherwise set it to 0
        basename = self.open_file.basename
        # Base reduction level is 0 (raw) or what is included in header
        reduction_level = self.header_data.get_reduction_level()
        # But if any prefix exists, force the reduction level to use that value in case it is set wrong in the file
        for prefix, rlevel in SOAR_PREFIX_TO_RLEVEL.items():
            if basename.startswith(prefix):
                reduction_level = rlevel
                break

        self.header_data.update_headers({settings.REDUCTION_LEVEL_KEY: reduction_level})
