# import boto3 module
import boto3


# Instantiate a ec2 service resource object
ec2_resource = boto3.resource('ec2')


# create an iterator that hold info for all vpcs
vpc_iterator = ec2_resource.vpcs.all()


# Loop through iterator to find default vpc and store id into variable
for vpc in vpc_iterator:
    if vpc.is_default:
        default_vpc_id = vpc.id
        

# create a subnet_iterator that uses default_vpc_id variable in filter
subnet_iterator = ec2_resource.subnets.filter(
    Filters=[
        {
            'Name': 'vpc-id',
            'Values': [
                default_vpc_id,
            ]
        },
    ]
)


# Define a function to create an ec2 instance

def create_instance(ID):
    KEY_PAIR_NAME = "kris_desktop"
    AMI_ID = 'ami-0c02fb55956c7d316' # Amazon Linux 2
    SUBNET_ID = ID # takes argument passed when calling function
    SECURITY_GROUP_ID = "sg-0135c8e5aa0fb0553" # uses demo-sg
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

    # Print statment can be used also used for different min/max values
    for instance in instances:
        print(f'The Instance ID is {instance.id}', 
            f'In the Subnet {instance.subnet_id} '
            f'with Private IP {instance.private_ip_address}')


# Print output output header
print('Create EC2 Instances')
print('----------------')


# Loop through subnet_iterator passing the return from subnet.id as the ID
for subnet in subnet_iterator:
    create_instance(subnet.id)
    