# This Python program prints the REgions that AWS Academy uses

import boto3
ec2_client = boto3.client('ec2')

# This retrives and prints region names
response = ec2_client.describe_regions()
print('List of AWS REgions available with AWS Academy')

counter = 0

for region in (response['Regions']):
    counter = counter + 1
    print(counter, ')', 'Region:', region['RegionName'])
