#!/usr/bin/env python3
import boto3
AWS_REGION = "us-east-1"
KEY_PAIR_NAME = "kris_desktop"
AMI_ID = 'ami-0c02fb55956c7d316' # Amazon Linux 2
SUBNET_ID = 'subnet-0e30cfd012330e1db'
SECURITY_GROUP_ID = 'sg-0135c8e5aa0fb0553'
USER_DATA = '''#!/bin/bash
yum update
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
                    'Value': 'my-ec2-instance'
                },
            ]
        },
    ]
)

for instance in instances:
    print(f'EC2 instance "{instance.id}" has been launched')
    instance.wait_until_running()
    print(f'EC2 instance "{instance.id}" has been started')