# RDS Helper Script

## Description
This script, `rds-helper.py`, is designed to assist with managing Amazon RDS instances. It provides various functionalities to automate common tasks related to RDS.

## Features
- Create RDS instances
- Delete RDS instances
- Modify RDS instance settings
- Backup and restore RDS instances
- Monitor RDS instance performance
- Scale RDS instances
- Enable Multi-AZ deployment
- Enable Read Replicas

## Prerequisites
Before using this script, ensure that you have the following:
- Python 3.x installed
- AWS CLI configured with appropriate credentials
- Access to the necessary AWS services (RDS, IAM, etc.)

## Installation
1. Clone this repository or download the `rds-helper.py` script.
2. Install the required Python packages by running the following command:
    ```
    pip install -r requirements.txt
    ```

## Usage
To use the `rds-helper.py` script, follow these steps:
1. Open a terminal or command prompt.
2. Navigate to the directory where the script is located.
3. Run the script using the following command:
    ```
    python rds-helper.py [options]
    ```
    Replace `[options]` with the desired command-line options.

## Command-line Options
The `rds-helper.py` script supports the following command-line options:
- `--create`: Create a new RDS instance.
- `--delete`: Delete an existing RDS instance.
- `--modify`: Modify the settings of an existing RDS instance.
- `--backup`: Backup an existing RDS instance.
- `--restore`: Restore a backup of an RDS instance.
- `--monitor`: Monitor the performance of an RDS instance.
- `--scale`: Scale an existing RDS instance.
- `--enable-multi-az`: Enable Multi-AZ deployment for an existing RDS instance.
- `--enable-read-replica`: Enable Read Replicas for an existing RDS instance.

## Examples
Here are some examples of how to use the `rds-helper.py` script:
- Create a new RDS instance:
  ```
  python rds-helper.py --create --instance-name my-rds-instance --db-engine mysql --db-username admin --db-password password123 --db-size 10
  ```
- Delete an existing RDS instance:
  ```
  python rds-helper.py --delete --instance-name my-rds-instance
  ```
- Modify the settings of an existing RDS instance:
  ```
  python rds-helper.py --modify --instance-name my-rds-instance --db-size 20
  ```
- Backup an existing RDS instance:
  ```
  python rds-helper.py --backup --instance-name my-rds-instance --backup-name my-backup
  ```
- Restore a backup of an RDS instance:
  ```
  python rds-helper.py --restore --instance-name my-rds-instance --backup-name my-backup
  ```
- Monitor the performance of an RDS instance:
  ```
  python rds-helper.py --monitor --instance-name my-rds-instance
  ```
- Scale an existing RDS instance:
  ```
  python rds-helper.py --scale --instance-name my-rds-instance --db-size 50
  ```
- Enable Multi-AZ deployment for an existing RDS instance:
  ```
  python rds-helper.py --enable-multi-az --instance-name my-rds-instance
  ```
- Enable Read Replicas for an existing RDS instance:
  ```
  python rds-helper.py --enable-read-replica --instance-name my-rds-instance
  ```