#!/usr/bin/env python3
import boto3
AWS_REGION = "us-east-1"
KEY_PAIR_NAME = 'Lenovo T410'
AMI_ID = 'ami-0c02fb55956c7d316' # Amazon Linux 2
SUBNET_ID = 'subnet-0984555689f5894d8'
SECURITY_GROUP_ID = 'sg-01304974040835e2f'
INSTANCE_PROFILE = 'EC2-Admin'
USER_DATA = '''#!/bin/bash
yum update
'''
EC2_RESOURCE = boto3.resource('ec2', region_name=AWS_REGION)
EC2_CLIENT = boto3.client('ec2', region_name=AWS_REGION)
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
                    'Value': 'my-ec2-instance'
                },
            ]
        },
    ]
)

for instance in instances:
    print(f'EC2 instance "{instance.id}" has been launched')
    
    instance.wait_until_running()
    
    EC2_CLIENT.associate_iam_instance_profile(
        IamInstanceProfile = {'Name': INSTANCE_PROFILE},
        InstanceId = instance.id,
    )
    print(f'EC2 Instance Profile "{INSTANCE_PROFILE}" has been attached')
    print(f'EC2 instance "{instance.id}" has been started')