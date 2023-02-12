import boto3

ec2_resource = boto3.resource('ec2')
vpc_iterator = ec2_resource.vpcs.all()

for vpc in vpc_iterator:
    if vpc.is_default:
        default_vpc_id = vpc.id

print(default_vpc_id)

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

for subnet in subnet_iterator:
    print(subnet.id)