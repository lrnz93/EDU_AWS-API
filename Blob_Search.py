import boto3
from botocore.exceptions import ClientError


#keys
key = "AKIAINULDQ6YLRMDZ5GQ"
secret = "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"

#user input
try:
    filename = input("Enter filename: ")
    print("Recieved filename: "+ filename)

except ValueError:
    print("uknown format")

# First, create the service resource object
s3resource = boto3.resource("s3", aws_access_key_id= key, aws_secret_access_key= secret)
s3client = boto3.client("s3", aws_access_key_id= key, aws_secret_access_key= secret)

# bucket name the bucket object
bucket = s3resource.Bucket('Innovation2018')

#object
obj = bucket.Object(filename)

try:
    print('Bucket name: {}'.format(bucket.name))
    print('Object key: {}'.format(obj.key))
    print('Object content length: {}'.format(obj.content_length))
    print('Object body: {}'.format(obj.get()['Body'].read()))
    print('Object last modified: {}'.format(obj.last_modified))

except ClientError as e:
    if e.response['Error']['Code'] == '404':
        print ('file not found')
    else:
        print(e.response)
