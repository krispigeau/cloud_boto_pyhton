# import boto3 module
import boto3

# create ec2 client instance to get subnet ids
ec2_client = boto3.client('ec2')

# Set values to be use in filter, for eaiser readability
filter_values={"Name":"default-for-az","Values":["true"]}

# use the descibe_subnet method ans filter for default subnets
response=ec2_client.describe_subnets(Filters=[filter_values])

# Create list to hold subnet IDs
subnetIDs = []

# Add subnet IDs to list
for subnet in response['Subnets']:
    subnetIDs.append(subnet['SubnetId'])
    
print(subnetIDs)