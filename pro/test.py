# # # import pandas as pd

# # # df = pd.read_csv('C:/Users/venkatesh.tholleti/Desktop/pro/Timesheet.csv')
# # # print(df)



# # # cols = df.columns.tolist()
# # # print(cols)
# # # cols = cols[-1:] + cols[:-1]
# # # print(cols)
# # # df = df[cols]
# # # df



# # import boto3

# # AWS_ACCESS_KEY="AKIA2O26VPFNPS32BE5N"
# # AWS_SECRET_KEY="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"
# # # client = boto3.client('ce',region_name="ap-south-1",
# # #     aws_access_key_id = AWS_ACCESS_KEY,
# # #     aws_secret_access_key = AWS_SECRET_KEY,
# # # )

# # import boto3
# # from datetime import datetime, timedelta
# # import json
# # ec2 = boto3.client('ec2', region_name='ap-south-1',aws_access_key_id = AWS_ACCESS_KEY,
# #     aws_secret_access_key = AWS_SECRET_KEY)
# # # ce = boto3.client('ce', region_name='ap-south-1',aws_access_key_id = AWS_ACCESS_KEY,
# # #     aws_secret_access_key = AWS_SECRET_KEY)


# # instance_id = 'i-0ae1e4d915c7471fd'
# # # Get the hourly rate for the instance type
# # instance_type = ec2.describe_instances(InstanceIds=[instance_id])['Reservations'][0]['Instances'][0]['InstanceType']
# # pricing = boto3.client('pricing', region_name='ap-south-1',aws_access_key_id = AWS_ACCESS_KEY,
# #     aws_secret_access_key = AWS_SECRET_KEY)
# # response = pricing.get_products(
# #     ServiceCode='AmazonEC2',
# #     Filters=[
# #         {'Type': 'TERM_MATCH', 'Field': 'instanceType', 'Value': instance_type},
# #         {'Type': 'TERM_MATCH', 'Field': 'operatingSystem', 'Value': 'Linux'},
# #         {'Type': 'TERM_MATCH', 'Field': 'tenancy', 'Value': 'Shared'},
# #     ],
# #     MaxResults=1
# # )

# # # print(response)
# # # hourly_rate = float(response['PriceList'][0]['terms']['OnDemand']['USD'])

# # # hourly_rate = response['PriceList'][0]['terms']['OnDemand']['USD']
# # # print(type(response))
# # # response

# # import json

# # # assume response is the JSON string from the AWS API
# # response_dict = json.loads(response)

# # price_per_unit_str = response_dict['PriceList'][0]['terms']['OnDemand'].values()[0]['priceDimensions'].values()[0]['pricePerUnit']

# # price_per_unit = {'USD': float(price_per_unit_str)}

# # print(price_per_unit)


# # res = '{'FormatVersion': 'aws_v1', 'PriceList': ['{"product":{"productFamily":"Compute Instance","attributes":{"enhancedNetworkingSupported":"Yes","intelTurboAvailable":"No","memory":"192 GiB","dedicatedEbsThroughput":"20000 Mbps","vcpu":"96","classicnetworkingsupport":"false","capacitystatus":"UnusedCapacityReservation","locationType":"AWS Region","storage":"EBS only","instanceFamily":"Compute optimized","operatingSystem":"Linux","abdInstanceClass":"c","intelAvx2Available":"No","regionCode":"us-west-2","physicalProcessor":"AMD EPYC 7R13 Processor","clockSpeed":"2.95 GHz","ecu":"NA","networkPerformance":"37500 Megabit","servicename":"Amazon Elastic Compute Cloud","instancesku":"3BVZJAR5RKP7X62X","gpuMemory":"NA","vpcnetworkingsupport":"true","instanceType":"c6a.24xlarge","tenancy":"Shared","usagetype":"USW2-UnusedBox:c6a.24xlarge","normalizationSizeFactor":"192","intelAvxAvailable":"No","processorFeatures":"AMD Turbo; AVX; AVX2","servicecode":"AmazonEC2","licenseModel":"No License required","currentGeneration":"Yes","preInstalledSw":"NA","location":"US West (Oregon)","processorArchitecture":"64-bit","marketoption":"OnDemand","operation":"RunInstances","availabilityzone":"NA"},"sku":"4FQRHN9RR8WPR7RC"},"serviceCode":"AmazonEC2","terms":{"OnDemand":{"4FQRHN9RR8WPR7RC.JRTCKXETXF":{"priceDimensions":{"4FQRHN9RR8WPR7RC.JRTCKXETXF.6YS6EN2CT7":{"unit":"Hrs","endRange":"Inf","description":"$3.672 per Unused Reservation Linux c6a.24xlarge Instance Hour","appliesTo":[],"rateCode":"4FQRHN9RR8WPR7RC.JRTCKXETXF.6YS6EN2CT7","beginRange":"0","pricePerUnit":{"USD":"3.6720000000"}}},"sku":"4FQRHN9RR8WPR7RC","effectiveDate":"2023-02-01T00:00:00Z","offerTermCode":"JRTCKXETXF","termAttributes":{}}}},"version":"20230228202612","publicationDate":"2023-02-28T20:26:12Z"}'], 'NextToken': 'Gp6DHjFV8VxhR8xoTgfR6w==:zxdnKP8ReCnRP8cVeOpLCxb0EipQ1QBNELo6I/HZrX82H2aUm9uSBrkG6fLrFUOosfpCzMSnoI4xYao6yArOz5OVQsb5Rdc5MctwhT2YxY0bo/35EMbDGHAKkTuESkgFWbnIIcVL/VawQ1sQWFsqlFpHORU+VhhHIY+nMxFNk+h/Z3CeYt6YSS5O2/Lv+4nc', 'ResponseMetadata': {'RequestId': '2e8ee5d9-8ef6-4397-a2c9-a2f56d32b619', 'HTTPStatusCode': 200, 'HTTPHeaders': {'date': 'Fri, 03 Mar 2023 11:57:28 GMT', 'content-type': 'application/x-amz-json-1.1', 'content-length': '2226', 'connection': 'keep-alive', 'x-amzn-requestid': '2e8ee5d9-8ef6-4397-a2c9-a2f56d32b619'}, 'RetryAttempts': 0}}'''



# # import boto3
# # import os

# # # set the S3 bucket and local directory
# # bucket_name = 'yaco-dev'
# # local_directory = 'C:/Users/venkatesh.tholleti/Desktop/nifi-1.19.1/source'

# # # create an S3 client
# # s3 = boto3.client('s3')
# # AWS_ACCESS_KEY = 'AKIA2O26VPFNPS32BE5N'
# # AWS_SECRET_KEY = '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'
# # # s3 = boto3.client('s3')
# # s3_resource = boto3.resource(service_name="s3", region_name="ap-south-1",
# #     aws_access_key_id=AWS_ACCESS_KEY, aws_secret_access_key=AWS_SECRET_KEY)




# # # list all objects in the bucket
# # objects = s3.list_objects(Bucket=bucket_name)['Contents']

# # # download each object to the local directory
# # for obj in objects:
# #     print(obj['Key'])
#     # file_path = os.path.join(local_directory, file_name)
#     # with open(file_path, 'wb') as f:
#     #     s3.download_fileobj(bucket_name, file_name, f)

# import boto3

# session = boto3.Session( aws_access_key_id='AKIA2O26VPFNPS32BE5N', aws_secret_access_key='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')



# s3 = session.resource('s3')

# my_bucket = s3.Bucket('yaco-dev')

# for my_bucket_object in my_bucket.objects.all():
#     print(my_bucket_object.key)


print('Hello World')

