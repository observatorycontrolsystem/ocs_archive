# OCS Archive Library

![Build](https://github.com/observatorycontrolsystem/ocs_archive/workflows/Build/badge.svg)
[![Coverage Status](https://coveralls.io/repos/github/observatorycontrolsystem/ocs_archive/badge.svg)](https://coveralls.io/github/observatorycontrolsystem/ocs_archive)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/ede4bb8145d348109a330ed8ba8479b1)](https://www.codacy.com/gh/observatorycontrolsystem/ocs_archive/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=observatorycontrolsystem/ocs_archive&amp;utm_campaign=Badge_Grade)

A base library for the Science Archive and Ingester library to support generalized input file types, generalized data stores, and shared configuration items. This library is configurable via environment variables, but more customization is possible by subclassing the `DataFile` class for a specific file type, or subclassing the `FileStore` class for a specific file storage scheme.

## Prerequisites

Optional prerequisites may be skipped for reduced functionality.

-   Python >= 3.6

## Installation

It is highly recommended that you install and run your python code inside a dedicated python
[virtual environment](https://docs.python.org/3/tutorial/venv.html).

Add the `ocs_archive` package to your python environment:

```bash
(venv) $ pip install ocs_archive
```

## Configuration

### Environment Variables

| Group | Variable | Description                                                                    | Default |
| ----- | -------- | ------------------------------------------------------------------------------ | ------- |
| FileStore | `FILESTORE_TYPE` | Type of filestorage to use. Options are `dummy`, `local`, or `s3`. | `dummy` |
|           | `FILESYSTEM_STORAGE_ROOT_DIR` | If using `local` file storage, this is the directory on the local filesystem to use as the root of the storage directories | _empty string_ |
|           | `FILESYSTEM_STORAGE_BASE_URL` | If using `local` file storage, this is the base URL at which those files will be hosted from | `http://0.0.0.0/` |
| AWS | `BUCKET` | If using `s3` file storage; AWS S3 Bucket Name | `testbucket` |
|     | `AWS_ACCESS_KEY_ID` | If using `s3` file storage; AWS Access Key with write access to the S3 bucket | _empty string_ |
|     | `AWS_SECRET_ACCESS_KEY` | If using `s3` file storage; AWS Secret Access Key | _empty string_ |
|     | `AWS_DEFAULT_REGION` | If using `s3` file storage; AWS S3 Default Region | _empty string_ |
|     | `S3_ENDPOINT_URL` | If using `s3` file storage; Endpoint url for connecting to s3. This can be modified to connect to a local instance of s3. | `"http://s3.us-west-2.amazonaws.com"` |
|     | `S3_DAYS_TO_IA_STORAGE` | If using `s3` file storage, this is the age in days after which data will be ingested directly to Infrequent Access (IA) storage vs normal storage. | 60 |
| DataFile | `FILETYPE_MAPPING_OVERRIDES` | A string literal representation of a python dictionary containing a mapping of file extensions to dotpaths to python Classes which subclass the DataFile class. This appends and overrides the default list in the FileFactory class. | `"{}"` |
|          | `HEADER_BLACKLIST` | Comma delimited string list of header values that should be removed from the data before storage in the archive. This can be overriden when instantiating a DataFile as well as via environment variable. | `HISTORY,COMMENT` |
|          | `REQUIRED_HEADERS` | Comma delimited string list of header values that must be present in the DataFile. This can be overriden when instantiating a DataFile as well as via environment variable |
|          | `NULL_HEADER_VALUES` | Comma delimited string list of header values that should be turned into `None` or empty keys. This only applies to the FitsFile class. | `N/A,UNSPECIFIED,UNKNOWN` |
|          | `CALIBRATION_TYPES` | Comma delimited string list of configuration types which represent calibration images. This is used to automatically set calibration images public date to be the observation date if it is not present | `BIAS,DARK,SKYFLAT,EXPERIMENTAL` |
|          | `PUBLIC_PROPOSALS` | Comma delimited string list of proposal IDs which represent public proposals. This is used to set the public date of observations under those proposals to the observation date if it is not present. The matching is based on if each character group appears anywhere within the proposal ID | `EPO,calib,standard,pointing` |
|          | `PRIVATE_PROPOSALS` | A comma delimited string list of proposal IDs which represent private proposals. This is used to set the public date of the observations under those proposals to be 999 years in the future. The matching is based on if each character group appears anywhere within the proposal ID | `LCOEngineering` |
|          | `DAYS_UNTIL_PUBLIC` | The number of days until user data becomes public by default. This is added onto the observation date to get the public date if one is not specifed with the data | `365` |
|          | `PRIVATE_FILE_TYPES` | A comma delimited string list of fragments of the file name which denote a private data file. If any of the fragments are found within the filename, the public date will be set 999 years in the future for this file | `-t00,-x00` |
| Header Mapping | `OBSERVATION_DATE_KEY` | The key in which to find an iso formatted observation date within the header data | `DATE-OBS` |
|                | `OBSERVATION_DAY_KEY` | The key in which to find an iso formatted observation day within the header data | `DAY-OBS` |
|                | `OBSERVATION_END_TIME_KEY` | The key in which to find an iso formatted observation end date within the header data | `UTSTOP` |
|                | `REDUCTION_LEVEL_KEY` | The key in which to find a numeric reduction level within the header data. Raw is 0, while anything non-zero is some form of processing | `RLEVEL` |
|                | `EXPOSURE_TIME_KEY` | The key in which to find the exposure time in fractional seconds in the header data | `EXPTIME` |
|                | `INSTRUMENT_ID_KEY` | The key in which to find the instrument ID in the header data | `INSTRUME` |
|                | `SITE_ID_KEY` | The key in which to find the site ID in the header data | `SITEID` |
|                | `TELESCOPE_ID_KEY` | The key in which to find the telescope ID in the header data | `TELID` |
|                | `OBSERVATION_ID_KEY` | The key in which to find the observation ID in the header data | `BLKUID` |
|                | `CONFIGURATION_ID_KEY` | The key in which to find the configuration ID in the header data | `MOLUID` |
|                | `PRIMARY_FILTER_KEY` | The key in which to find the primary filter value in the header data | `FILTER` |
|                | `TARGET_NAME_KEY` | The key in which to find the target object's name in the header data | `OBJECT` |
|                | `REQUEST_ID_KEY` | The key in which to find the request ID in the header data | `REQNUM` |
|                | `REQUESTGROUP_ID_KEY` | The key in which to find the request group ID in the header data | `TRACKNUM` |
|                | `CONFIGURATION_TYPE_KEY` | The key in which to find the configuration type in the header data | `OBSTYPE` |
|                | `PROPOSAL_ID_KEY` | The key in which to find the proposal ID in the header data | `PROPID` |
|                | `CATALOG_TARGET_FRAME_KEY` | The key in which to find the base filename of the catalog file for the target of this observation in the header data | `L1IDCAT` |
|                | `PUBLIC_DATE_KEY` | The key in which to find the iso formatted date in which this data should become available to the public in the header data | `L1PUBDAT` |
|                | `RELATED_FRAME_KEYS` | A comma delimited list of keys in the header data to look for related frame base filenames for this observation | `L1IDBIAS,L1IDDARK,L1IDFLAT,L1IDSHUT,L1IDMASK,L1IDFRNG,L1IDCAT,L1IDARC,L1ID1D,L1ID2D,L1IDSUM,TARFILE,ORIGNAME,ARCFILE,FLATFILE,GUIDETAR` |
|                | `RADIUS_KEY` | The key in which to find FOV radius for a circular FOV, used to calculate WCS polygon if specified. Unit of arcseconds | `RADIUS` |
|                | `RA_KEY` | The key in which to find FOV center RA for a circular FOV, used to calculate WCS polygon if specified. Unit of hour angle | `RA` |
|                | `DEC_KEY` | The key in which to find FOV center DEC for a circular FOV, used to calculate WCS polygon if specified. Unit of decimal degrees | `DEC` |

### Input File Format Configuration

The library is designed to be configured mostly through environment variables, but custom `DataFile` subclasses can be included and specified via an environment variable in order to support new and more complicated data formats. All data files must contain the minimum set of metadata in order to ingested into the archive. This metadata is used to provide filtering and querying support within the archive. The pieces of file metadata that should be specified have their mappings defined in the Header Data section of the environment variables below. The `FitsFile` class provided will work for normal or funpacked fits files, provided you set up the Header Data environment variables with the correct mapping of observation concepts to header keys in your data format.

### File Storage Format Configuration

The library supports three types of file storage by default, that can be selected via environment variable. The `dummy` type is just used for testing and development and doesn't actually store any file. The `local` storage just saves the files into a locally mounted directory. It requires you to run a separate file server on that directory so it knows how to direct links to download the files. This can be accomplished as simply as running `python -m http.server --directory=/my/root/dir`. It could alternatively be served using any other file server, like node's http-server. The third option is `s3`, and expects to connect to Amazon's S3 or something with that same interface like minio. S3 file storage requires `BUCKET`, `AWS_*`, and `S3_*` environment variables to be set. More storage types can be added via forking the library and subclassing the `FileStore` class.

## Development

### Running the Tests

After cloning this project, from the project root and inside your virtual environment:

```bash
(venv) $ pip install -e .[tests]
(venv) $ pytest
```
