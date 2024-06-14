# EC2 Helper Script

## Description
The `ec2-helper.py` script is a utility tool for managing Amazon EC2 instances. It provides various functionalities to interact with EC2 instances, such as starting, stopping, and terminating instances, retrieving instance information, and more.

## Prerequisites
Before using this script, make sure you have the following:
- Python 3.x installed on your system
- AWS CLI configured with valid credentials

## Installation
1. Clone the repository or download the `ec2-helper.py` script.
2. Install the required dependencies by running the following command:
    ```
    pip install -r requirements.txt
    ```

## Usage
To use the `ec2-helper.py` script, follow these steps:
1. Open a terminal or command prompt.
2. Navigate to the directory where the script is located.
3. Run the script using the following command:
    ```
    python ec2-helper.py [options]
    ```
    Replace `[options]` with the desired command and arguments. Refer to the script's help documentation for available options.

## Examples
Here are some examples of how to use the `ec2-helper.py` script:

- Start an EC2 instance:
    ```
    python ec2-helper.py start --instance-id i-1234567890abcdef0
    ```

- Stop an EC2 instance::
    ```
    python ec2-helper.py stop --instance-id i-1234567890abcdef0
    ```

- Terminate an EC2 instance:
    ```
    python ec2-helper.py terminate --instance-id i-1234567890abcdef0
    ```

- Retrieve information about an EC2 instance:
    ```
    python ec2-helper.py describe --instance-id i-1234567890abcdef0
    ```

- List all running EC2 instances::
    ```
    python ec2-helper.py list
    ```

- Create a new EC2 instance:
    ```
    python ec2-helper.py create --image-id ami-1234567890abcdef0 --instance-type t2.micro --key-name my-key-pair
    ```

- Attach an EBS volume to an EC2 instance:
    ```
    python ec2-helper.py attach-volume --instance-id i-1234567890abcdef0 --volume-id vol-1234567890abcdef0 --device /dev/sdf
    ```

- Detach an EBS volume from an EC2 instance:

    ```
    python ec2-helper.py detach-volume --instance-id i-1234567890abcdef0 --volume-id vol-1234567890abcdef0
    ```

- Create a snapshot of an EBS volume:
    ```
    python ec2-helper.py create-snapshot --volume-id vol-1234567890abcdef0
    ```

- Delete a snapshot:

    ```
    python ec2-helper.py delete-snapshot --snapshot-id snap-1234567890abcdef0
    ```
