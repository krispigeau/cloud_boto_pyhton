# Python program describe_az.py displays the availability zones description only
import boto3
target = boto3.client('ec2')
response = target.describe_availability_zones()
print(response['AvailabilityZones'])