import boto3

# Variables receive values from the user:
quantity = int(input('Enter the number of EC2s to be created: '))
ami = (input('Enter the Image ID: '))
keyname = (input('Enter the key name: '))

# This function creates EC2 instance:
def create_instance():
 ec2_client = boto3.client("ec2", region_name="us-east-1")
 instances = ec2_client.run_instances(
    ImageId = ami,
    MinCount = quantity,
    MaxCount = quantity,
    InstanceType = "t2.micro",
    KeyName = keyname,
    TagSpecifications=[{'ResourceType': 'instance','Tags': [{'Key': 'Name','Value': 'VM'}]}])

# The created instances ID are printed:
 for n in range(quantity):
    print(instances["Instances"][n]["InstanceId"])
    print(type(instances))
    print(isinstance(instances))
    
create_instance()

