import boto3
target = boto3.client('ec2')
response=target.describe_subnets()
print(response['Subnets'])