# This python program creates a VPC and its Internet Gateway

import boto3

ec2 = boto3.resource('ec2')

ipv4_space_var = input('Enter the IPv4 address space: ')
vpc_name_var = input('Enter the name of the VPC: ')

# Create VPC; assign TPv4 address space and name tag.
def CreateVpc():
    vpc = ec2.create_vpc(CidrBlock=ipv4_space_var)
    vpc.create_tags(Tags=[{'Key': 'Name', 'Value': vpc_name_var}])
    vpc.wait_until_available()
    print(vpc.id)
    return(vpc)
    
# Create the Internat Gateway and attach it to the VPC
def CreateIgw(vpc):
    igw = ec2.create_internet_gateway()
    vpc.attach_internet_gateway(InternetGatewayId=igw.id)
    print(igw.id)

vpc = CreateVpc()
CreateIgw(vpc)

