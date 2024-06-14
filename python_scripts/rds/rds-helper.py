import boto3


def create_rds_instance():
    """
    Creates a new RDS instance with the specified configuration.

    Returns:
        None
    """
    # Create an RDS client
    rds_client = boto3.client('rds')
    
    # Create a new RDS instance
    response = rds_client.create_db_instance(
        DBInstanceIdentifier='my-rds-instance',
        Engine='mysql',
        AllocatedStorage=20,
        DBInstanceClass='db.t2.micro',
        MasterUsername='admin',
        MasterUserPassword='password',
        VpcSecurityGroupIds=['sg-12345678'],
        AvailabilityZone='us-east-1a'
    )
    
    print("Created RDS instance:", response['DBInstance']['DBInstanceIdentifier'])


def describe_rds_instance():
    """
    Retrieves information about the specified RDS instance.

    Returns:
        None
    """
    # Create an RDS client
    rds_client = boto3.client('rds')
    
    # Describe the newly created RDS instance
    response = rds_client.describe_db_instances(
        DBInstanceIdentifier='my-rds-instance'
    )
    
    print("RDS instance status:", response['DBInstances'][0]['DBInstanceStatus'])


def modify_rds_instance():
    """
    Modifies the configuration of the specified RDS instance.

    Returns:
        None
    """
    # Create an RDS client
    rds_client = boto3.client('rds')
    
    # Modify the RDS instance
    response = rds_client.modify_db_instance(
        DBInstanceIdentifier='my-rds-instance',
        AllocatedStorage=30,
        ApplyImmediately=True
    )
    
    print("Modified RDS instance:", response['DBInstance']['DBInstanceIdentifier'])


def delete_rds_instance():
    """
    Deletes the specified RDS instance.

    Returns:
        None
    """
    # Create an RDS client
    rds_client = boto3.client('rds')
    
    # Delete the RDS instance
    response = rds_client.delete_db_instance(
        DBInstanceIdentifier='my-rds-instance',
        SkipFinalSnapshot=True
    )
    
    print("Deleted RDS instance:", response['DBInstance']['DBInstanceIdentifier'])


def start_rds_instance():
    """
    Starts the specified RDS instance.

    Returns:
        None
    """
    # Create an RDS client
    rds_client = boto3.client('rds')
    
    # Start the RDS instance
    response = rds_client.start_db_instance(
        DBInstanceIdentifier='my-rds-instance'
    )
    
    print("Started RDS instance:", response['DBInstance']['DBInstanceIdentifier'])


def stop_rds_instance():
    """
    Stops the specified RDS instance.

    Returns:
        None
    """
    # Create an RDS client
    rds_client = boto3.client('rds')
    
    # Stop the RDS instance
    response = rds_client.stop_db_instance(
        DBInstanceIdentifier='my-rds-instance'
    )
    
    print("Stopped RDS instance:", response['DBInstance']['DBInstanceIdentifier'])


def reboot_rds_instance():
    """
    Reboots the specified RDS instance.

    Returns:
        None
    """
    # Create an RDS client
    rds_client = boto3.client('rds')
    
    # Reboot the RDS instance
    response = rds_client.reboot_db_instance(
        DBInstanceIdentifier='my-rds-instance'
    )
    
    print("Rebooted RDS instance:", response['DBInstance']['DBInstanceIdentifier'])


def main():
    """
    Main function that executes all the RDS instance operations.

    Returns:
        None
    """
    create_rds_instance()
    describe_rds_instance()
    modify_rds_instance()
    delete_rds_instance()
    start_rds_instance()
    stop_rds_instance()
    reboot_rds_instance()


if __name__ == "__main__":
    main()
