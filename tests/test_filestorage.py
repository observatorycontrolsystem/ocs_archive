import os
from unittest.mock import patch
import unittest

from ocs_archive.storage.filestore import FileStore
from ocs_archive.storage.filesystemstore import FileSystemStore
from ocs_archive.storage.s3store import strip_quotes_from_etag, S3Store
from ocs_archive.input.file import File
from ocs_archive.input.lcofitsfile import LcoFitsFile


FITS_PATH = os.path.join(
    os.path.dirname(__file__),
    'test_files/fits/'
)
OTHER_PATH = os.path.join(
    os.path.dirname(__file__),
    'test_files/other/'
)
FITS_FILE = os.path.join(
    FITS_PATH,
    'coj1m011-kb05-20150219-0125-e90.fits.fz'
)
PDF_FILE = os.path.join(
    OTHER_PATH,
    'cptnrs03-fa13-20150219-0001-e92-summary.pdf'
)


def mocked_s3_object(*args, **kwargs):
    class MockS3Object:
        class Object:
            def __init__(self, *args, **kwargs):
                pass

            def put(self, *args, **kwargs):
                return {'ETag': '"fakemd5"', 'VersionId': 'fakeversion'}

    return MockS3Object()

def mocked_boto3_client(*args, **kwargs):
    class MockBoto3Client:
        def __init__(self, *args, **kwargs):
            pass

        def download_fileobj(self, Bucket, Key, Fileobj):
            filename = os.path.basename(Key)
            Fileobj.write(b"Test 123")
            setattr(Fileobj, 'name', filename)

        def head_object(self, Bucket, Key):
            return {'ContentLength': 10}

        def generate_presigned_url(self, *args, **kwargs):
            params = kwargs['Params']
            return f"s3://{params['Bucket']}/{params['Key']}"
        
        def delete_object(self, *args, **kwargs):
            pass

    return MockBoto3Client()

class TestS3Store(unittest.TestCase):
    def setUp(self):
        self.s3 = S3Store(bucket='somebucket')

    def test_strip_quotes_from_etag(self):
        self.assertEqual('fakemd5', strip_quotes_from_etag('"fakemd5"'))
        self.assertIsNone(strip_quotes_from_etag('"wrong'))

    @patch('boto3.resource', side_effect=mocked_s3_object)
    def test_upload_file(self, s3_mock):
        fits_dict = {'SITEID': 'tst', 'INSTRUME': 'inst01', 'DATE-OBS': '2019-10-11T00:11:22.123'}
        with open(FITS_FILE, 'rb') as fileobj:
            data_file = LcoFitsFile(File(fileobj))
            self.s3.store_file(data_file)
        self.assertTrue(s3_mock.called)

    @patch('boto3.client', side_effect=mocked_boto3_client)
    def test_get_file(self, boto3_mock):
        with self.s3.get_fileobj('special/dir/thing.fits.fz') as fileobj:
            self.assertTrue(boto3_mock.called)
            self.assertEqual(fileobj.name, 'thing.fits.fz')

    @patch('boto3.client', side_effect=mocked_boto3_client)
    def test_get_file_size(self, boto3_mock):
        filesize = self.s3.get_file_size('thing.fits.fz')
        self.assertTrue(boto3_mock.called)
        self.assertEqual(filesize, 10)

    @patch('boto3.client', side_effect=mocked_boto3_client)
    def test_get_url(self, boto3_mock):
        url = self.s3.get_url('thing.fits.fz', '', 0)
        self.assertTrue(boto3_mock.called)
        self.assertEqual(url, 's3://somebucket/thing.fits.fz')

    @patch('boto3.client', side_effect=mocked_boto3_client)
    def test_delete_file(self, boto3_mock):
        self.s3.delete_file('thing.fits.fz', '')
        self.assertTrue(boto3_mock.called)
