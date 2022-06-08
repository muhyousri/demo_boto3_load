import boto3
import pandas as pd


regions=["us-east-1","us-west-1","us-west-2"]


def describe_full_sg(region):
    for f in region :
        sg_ids=[]
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

    
    return get_sg

print("loading ..")
df = pd.DataFrame(describe_full_sg(regions)["SecurityGroups"])
data = df[['GroupId','GroupName','VpcId','Description']]
writer = pd.ExcelWriter('output.xlsx')
data.to_excel(writer)
writer.save()
print("Done! , Check the spreadsheet in output.xlsx")

