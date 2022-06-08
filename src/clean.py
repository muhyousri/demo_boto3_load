import boto3 

regions=["us-east-1","us-west-1","us-west-2"]


def get_sg(region):
    sg_ids=[]
    ec2 = boto3.client('ec2',region_name=region)
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
            sg_ids.append(get_sg['SecurityGroups'][i]['GroupId'])
        
    return sg_ids


def get_vpc(region):
    vpc_ids=[]
    ec2 = boto3.client('ec2',region_name=region)
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
            vpc_ids.append(get_vpc['Vpcs'][i]['VpcId'])
        
    return vpc_ids



def is_deleted(regions):
    test = 0
    for f in regions:
        if len(get_sg(f)) != 0 and len(get_vpc(f)) != 0:
            test += 1
    if test > 0 :
        return False
    else:
        return True



def delete_all(region):

    for f in region:
        ec2 = boto3.client('ec2',region_name=f)
        sg_ids=get_sg(f)
        for i in sg_ids:
            ec2.delete_security_group(GroupId=i)
        vpc_ids=get_vpc(f)
        for x in vpc_ids:
            ec2.delete_vpc(VpcId=x)



print("Checking for Existing resources ..")

if is_deleted(regions) == True :
    print("No Resources found , use run.sh -c instead!")
else:
    print("Resources found! , Deleting ...")
    delete_all(regions)
    print("Done!")
