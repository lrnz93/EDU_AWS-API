# Import the SDK
import boto3
import uuid

# set key variables
key = ""
secret = ""

try:
    filename = input("Enter file with extention: ")
    print("Recieved filename: "+ filename)

    messageinfile = input("enter message: \n")

except ValueError:
    print("uknown format")

#start client connection
s3client = boto3.client("s3", aws_access_key_id= key, aws_secret_access_key= secret)

#create bucket
bucket_name = 'Innovation2018'.format(uuid.uuid4())
print('bucketname is : {}'.format(bucket_name))
s3client.create_bucket(Bucket=bucket_name)

# list the bucket.
list_buckets_resp = s3client.list_buckets()
for bucket in list_buckets_resp['Buckets']:
    if bucket['Name'] == bucket_name:
        print('(Just created) --> {} - there since {}'.format(
            bucket['Name'], bucket['CreationDate']))


print('Upload data to {} with key: {}'.format(
    bucket_name, filename))

s3client.put_object(Bucket=bucket_name, Key=filename, Body=messageinfile)

url = s3client.generate_presigned_url(
    'get_object', {'Bucket': bucket_name, 'Key': filename})
print('\nURL to download the object:')
print(url)
