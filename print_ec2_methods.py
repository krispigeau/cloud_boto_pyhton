import boto3
print(dir(boto3.resource('ec2')))

print("\n\n\n")
ec2 = boto3.resource('ec2')
print(dir(ec2.Subnet.__get__))