import boto3
subnets = boto3.resource('ec2').subnets.all()

for subnet in subnets:
    print(dir(subnet))
    break

for subnet in subnets:
    print(f' Subet {subnet.cidr_block}',
    f'in Availability Zone {subnet.availability_zone}', 
    f'has {subnet.available_ip_address_count} addresses')