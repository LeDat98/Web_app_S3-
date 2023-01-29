import boto3
##Lấy đường link của tất cả các file có trong thư mục static/images trên S3 
s3 = boto3.client('s3', aws_access_key_id='AKIAR56QI6RTALXWK3G3',
        aws_secret_access_key='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')

bucket_name = 'my-s3-datofbucket1'
prefix = 'static/images/'

result = s3.list_objects(Bucket=bucket_name, Prefix=prefix)
print(type(result),end ="\n")
print(result,end ="\n")
images = []
for content in result.get('Contents', []):
    images.append(content.get('Key'))
print(images,end ="\n")