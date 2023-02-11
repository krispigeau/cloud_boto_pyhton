import boto3
target = boto3.client('ec2')
filter_values={"Name":"default-for-az","Values":["true"]}
response=target.describe_subnets(Filters=[filter_values])

for subnet in response['Subnets']:
    print(subnet['SubnetId'])