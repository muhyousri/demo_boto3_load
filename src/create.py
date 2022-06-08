import boto3

regions = ["us-west-1","us-west-2","us-east-1"]

def create_vpc(region):
    ec2 = boto3.resource('ec2',region_name=region)
    vpc = ec2.create_vpc(
        CidrBlock="10.0.0.4/16",
        TagSpecifications=[
        {
            'ResourceType': 'vpc',
            'Tags': [
                {
                    'Key': 'boto3_vpc',
                    'Value': 'test'
                },
            ]
        },
    ]

    )
    return vpc.id

def create_sg(region,n,vpc):
    ec2 = boto3.resource('ec2',region_name=region)
    group_name = "boto3_group-"+str(n)
    sg = ec2.create_security_group(
    Description='Test Boto3',
    GroupName=group_name,
    VpcId=vpc,
    TagSpecifications=[
        {
            'ResourceType': 'security-group',
            'Tags': [
                {
                    'Key': 'boto3_vpc',
                    'Value': 'test'
                },
            ]
        },
    ]

)

vpc_ids={}

print("Creating Resources ..")

for i in  regions:
    vc = create_vpc(i)
    vpc_ids[i]=vc

print("Created VPCs")

print("Creating Security Groups  ..")
for b in range (50):
    for c in regions:
        create_sg(c,b,vpc_ids[c])
print("Done")
