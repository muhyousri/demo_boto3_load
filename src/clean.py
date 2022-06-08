import boto3 

regions=["us-east-1","us-west-1","us-west-2"]

def is_deleted(regions):
    for f in regions:
        ec2 = boto3.client('ec2',region_name=f)
        get_sg = ec2.describe_security_groups(
        Filters=[
            {
                'Name': 'tag:boto3_vpc',
                'Values': [
                    'test',
                ]
            },
        ],
        )
        get_vpc = ec2.describe_vpcs(
        Filters=[
           {
               'Name': 'tag:boto3_vpc',
               'Values': [
                   'test',
               ]
           },
        ],
        )
        if len(get_sg['SecurityGroups']) != 0 and len(get_vpc['Vpcs']) != 0:
            return False
        else:
           return True
           


def delete_all(region):
    for f in region:
        ec2 = boto3.client('ec2',region_name=f)
        get_sg = ec2.describe_security_groups(
        Filters=[
            {
                'Name': 'tag:boto3_vpc',
                'Values': [
                    'test',
                ]
            },
        ],
        )
        for i in range(len(get_sg['SecurityGroups'])):
            ec2.delete_security_group(GroupId=get_sg['SecurityGroups'][i]['GroupId'])
    for f in region:
        ec2 = boto3.client('ec2',region_name=f)
        get_vpc = ec2.describe_vpcs(
        Filters=[
            {
                'Name': 'tag:boto3_vpc',
                'Values': [
                    'test',
                ]
            },
        ],
        )
        for i in range(len(get_vpc['Vpcs'])):
            ec2.delete_vpc(VpcId=get_vpc['Vpcs'][i]['VpcId'])




if is_deleted(regions) == True :
    print("No Resources found , use run.sh -c instead!")
else: 
    print("Cleaning resources ...")
    delete_all(regions)
    print("Done!")
