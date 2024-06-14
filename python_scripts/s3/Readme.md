# S3 Helper Script

This script, `s3-helper.py`, is designed to assist with common tasks related to Amazon S3 (Simple Storage Service). It provides a set of functions and utilities to interact with S3 buckets and objects programmatically.

## Prerequisites

Before using this script, make sure you have the following:

- Python 3.x installed on your system
- AWS SDK for Python (Boto3) installed. You can install it using `pip`:

    ```shell
    pip install boto3
    ```

- AWS credentials configured on your system. You can set them up using the AWS CLI or by configuring environment variables.

## Usage

To use the `s3-helper.py` script, follow these steps:

1. Clone or download this repository to your local machine.
2. Open a terminal or command prompt and navigate to the directory where the script is located.
3. Run the script using the following command:

     ```shell
     python s3-helper.py
     ```

4. The script will prompt you for the necessary inputs, such as AWS credentials and the S3 bucket and object details.
5. Follow the on-screen instructions to perform the desired S3 operations.

## Features

The `s3-helper.py` script provides the following features:

- Uploading files to an S3 bucket
- Downloading files from an S3 bucket
- Listing objects in an S3 bucket
- Deleting objects from an S3 bucket
- Creating and deleting S3 buckets
- Setting and getting object ACLs (Access Control Lists)

## Examples

Here are a few examples of how to use the `s3-helper.py` script:

- Uploading a file to an S3 bucket:

    ```shell
    python s3-helper.py upload my-bucket my-file.txt
    ```

- Downloading a file from an S3 bucket:

    ```shell
    python s3-helper.py download my-bucket my-file.txt
    ```

- Listing objects in an S3 bucket:

    ```shell
    python s3-helper.py list my-bucket
    ```

- Deleting an object from an S3 bucket:

    ```shell
    python s3-helper.py delete my-bucket my-file.txt
    ```

- Creating an S3 bucket:

    ```shell
    python s3-helper.py create-bucket my-bucket
    ```

- Deleting an S3 bucket:

    ```shell
    python s3-helper.py delete-bucket my-bucket
    ```

- Setting object ACL:

    ```shell
    python s3-helper.py set-acl my-bucket my-file.txt private
    ```

- Getting object ACL:

    ```shell
    python s3-helper.py get-acl my-bucket my-file.txt
    ```

