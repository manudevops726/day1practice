import boto3

# Create an EC2 resource
ec2 = boto3.resource('ec2')

# Launch an EC2 instance
instance = ec2.create_instances(
    ImageId='ami-0abcdef1234567890',  # Replace with a valid AMI ID
    InstanceType='t2.micro',  # Instance type
    MinCount=1,  # Minimum number of instances
    MaxCount=1   # Maximum number of instances
)

# Print the instance ID
print(f"Created EC2 instance with ID: {instance[0].id}")

