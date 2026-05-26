import boto3

ec2 = boto3.client('ec2', region_name='us-east-1')

response = ec2.create_image(
    InstanceId='i-0123456789abcdef0',
    Name='MyApp-AMI',
    Description='AMI created from EC2 instance',
    NoReboot=True
)

print("AMI ID:", response['ImageId'])
