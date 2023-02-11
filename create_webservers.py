# import boto3 module
import boto3


# create ec2 client instance to get subnet ids
ec2_client = boto3.client('ec2')


# Set values to be use in filter, for eaiser readability
filter_values={"Name":"default-for-az","Values":["true"]}


# use the descibe_subnet method and filter for default subnets
response=ec2_client.describe_subnets(Filters=[filter_values])


# Create list to hold subnet IDs
subnetIDs = []


# Add subnet IDs to list
for subnet in response['Subnets']:
    subnetIDs.append(subnet['SubnetId'])


# Define a function to create an ec2 instance

def create_instance(ID):
    KEY_PAIR_NAME = "kris_desktop"
    AMI_ID = 'ami-0c02fb55956c7d316' # Amazon Linux 2
    SUBNET_ID = ID # takes argument passed when calling function
    SECURITY_GROUP_ID = "sg-0135c8e5aa0fb0553"
    USER_DATA = '''#!/bin/bash
    yum update -y
    yum install httpd -y
    cd /var/www/html
    echo "<html><body><h1> Hello from Kris Pigeau at \
    $(hostname -f) </html></body></h1>" > index.html
    systemctl restart httpd
    systemctl enable httpd
    '''
    EC2_RESOURCE = boto3.resource("ec2", region_name="us-east-1")
    instances = EC2_RESOURCE.create_instances(
        MinCount = 1,
        MaxCount = 1,
        ImageId=AMI_ID,
        InstanceType='t2.micro',
        KeyName=KEY_PAIR_NAME,
        SecurityGroupIds = [SECURITY_GROUP_ID],
        SubnetId=SUBNET_ID,
        UserData=USER_DATA,
        TagSpecifications=[
            {
                'ResourceType': 'instance',
                'Tags': [
                    {
                        'Key': 'Name',
                        'Value': 'VM'
                    },
                ]
            },
        ]
    )

    for instance in instances:
        print(f'The Instance ID is {instance.id}', 
            f'In the Subnet {instance.subnet_id} '
            f'with Private IP {instance.private_ip_address}')

# Print output output header
print('Create EC2 Instances')
print('----------------')

for subID in subnetIDs:
    create_instance(subID)
    