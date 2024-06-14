import boto3

def describe_instance(instance_id):
    """
    Describes a specific EC2 instance.

    Args:
        instance_id (str): The ID of the instance to describe.
    """
    response = ec2_client.describe_instances(InstanceIds=[instance_id])
    instance = response['Reservations'][0]['Instances'][0]
    instance_id = instance['InstanceId']
    instance_state = instance['State']['Name']
    instance_type = instance['InstanceType']
    public_ip = instance.get('PublicIpAddress', 'N/A')
    private_ip = instance.get('PrivateIpAddress', 'N/A')
    print(f"Instance ID: {instance_id}")
    print(f"State: {instance_state}")
    print(f"Instance Type: {instance_type}")
    print(f"Public IP: {public_ip}")
    print(f"Private IP: {private_ip}")

def reboot_instance(instance_id):
    """
    Reboots an existing EC2 instance.

    Args:
        instance_id (str): The ID of the instance to reboot.
    """
    ec2_client.reboot_instances(InstanceIds=[instance_id])
    print(f"Rebooted EC2 instance with ID: {instance_id}")

def create_image(instance_id, image_name):
    """
    Creates an Amazon Machine Image (AMI) from an existing EC2 instance.

    Args:
        instance_id (str): The ID of the instance to create an image from.
        image_name (str): The name of the image to create.
    """
    response = ec2_client.create_image(
        InstanceId=instance_id,
        Name=image_name,
        Description=f"AMI created from instance {instance_id}"
    )
    image_id = response['ImageId']
    print(f"Created AMI with ID: {image_id}")

def create_key_pair(key_name):
    """
    Creates a new key pair for EC2 instances.

    Args:
        key_name (str): The name of the key pair to create.
    """
    response = ec2_client.create_key_pair(KeyName=key_name)
    key_material = response['KeyMaterial']
    key_file = f"{key_name}.pem"
    with open(key_file, 'w') as f:
        f.write(key_material)
    print(f"Created key pair: {key_name}")
    print(f"Key pair file saved as: {key_file}")

# Create an EC2 client
ec2_client = boto3.client('ec2')

def create_instance():
    """
    Creates a new EC2 instance.
    """
    response = ec2_client.run_instances(
        ImageId='ami-12345678',  # Replace with your desired AMI ID
        InstanceType='t2.micro',  # Replace with your desired instance type
        MinCount=1,
        MaxCount=1
    )
    instance_id = response['Instances'][0]['InstanceId']
    print(f"Created EC2 instance with ID: {instance_id}")

def start_instance(instance_id):
    """
    Starts an existing EC2 instance.

    Args:
        instance_id (str): The ID of the instance to start.
    """
    ec2_client.start_instances(InstanceIds=[instance_id])
    print(f"Started EC2 instance with ID: {instance_id}")

def stop_instance(instance_id):
    """
    Stops an existing EC2 instance.

    Args:
        instance_id (str): The ID of the instance to stop.
    """
    ec2_client.stop_instances(InstanceIds=[instance_id])
    print(f"Stopped EC2 instance with ID: {instance_id}")

def terminate_instance(instance_id):
    """
    Terminates an existing EC2 instance.

    Args:
        instance_id (str): The ID of the instance to terminate.
    """
    ec2_client.terminate_instances(InstanceIds=[instance_id])
    print(f"Terminated EC2 instance with ID: {instance_id}")

def list_instances():
    """
    Lists all EC2 instances.
    """
    response = ec2_client.describe_instances()
    instances = response['Reservations']
    for reservation in instances:
        for instance in reservation['Instances']:
            instance_id = instance['InstanceId']
            instance_state = instance['State']['Name']
            print(f"Instance ID: {instance_id}, State: {instance_state}")

# Example usage
create_instance()
list_instances()

# Call other functions as needed
instance_id = 'your-instance-id'  # Replace with the instance ID you want to work with
image_name = 'your-image-name'  # Replace with the desired image name
key_name = 'your-key-name'  # Replace with the desired key pair name

describe_instance(instance_id)
reboot_instance(instance_id)
create_image(instance_id, image_name)
create_key_pair(key_name)
start_instance(instance_id)
stop_instance(instance_id)
terminate_instance(instance_id)
list_instances()