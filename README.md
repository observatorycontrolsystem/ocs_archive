# OCS Archive Library

![Build](https://github.com/observatorycontrolsystem/ocs_archive/workflows/Build/badge.svg)
[![Coverage Status](https://coveralls.io/repos/github/observatorycontrolsystem/ocs_archive/badge.svg?branch=master)](https://coveralls.io/github/observatorycontrolsystem/ocs_archive?branch=main)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/24eb8debeb0c499ca192b4497a1f1e12)](https://www.codacy.com/gh/observatorycontrolsystem/ocs_archive?utm_source=github.com&utm_medium=referral&utm_content=observatorycontrolsystem/ocs_archive&utm_campaign=Badge_Grade)

A base library for the science archive and ingester library to support generalized input file types, generalized data stores, and shared configuration items.

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

TODO

#### Environment Variables

|                 | Variable                            | Description                                                                                                                                                                                                                                | Default                    |
| --------------- | ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------- |
| AWS             | `BUCKET`                            | AWS S3 Bucket Name                                                                                                                                                                                                                         | `ingestertest`             |
|                 | `AWS_ACCESS_KEY_ID`                 | AWS Access Key with write access to the S3 bucket                                                                                                                                                                                          | _empty string_             |
|                 | `AWS_SECRET_ACCESS_KEY`             | AWS Secret Access Key                                                                                                                                                                                                                      | _empty string_             |
|                 | `AWS_DEFAULT_REGION`                | AWS S3 Default Region                                                                                                                                                                                                                      | _empty string_             |
|                 | `S3_ENDPOINT_URL`                   | Endpoint url for connecting to s3. This can be modified to connect to a local instance of s3.                                                                                                                                              | `"http://s3.us-west-2.amazonaws.com"` |
|

## For Developers

#### Running the Tests

After cloning this project, from the project root and inside your virtual environment:

```bash
(venv) $ pip install -e .[tests]
(venv) $ pytest
```
