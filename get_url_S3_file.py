import boto3
from flask import Flask, render_template, request, send_file, send_from_directory


# app = Flask(__name__)

# @app.route('/')
# def home():
# Initialize a session using DigitalOcean Spaces.
session = boto3.Session(
        aws_access_key_id='',
        aws_secret_access_key='',
        region_name='ap-northeast-1'
    )
client = session.client('s3', endpoint_url='https://s3.ap-northeast-1.amazonaws.com')

    # Set the desired bucket name
bucket_name = 'my-s3-datofbucket1'
    # Set the desired folder name
folder_name = 'static/image_system'

img_urls = []

    # Use the boto3 client to list all objects in the specified folder
result = client.list_objects_v2(Bucket=bucket_name, Prefix=folder_name)

for content in result.get("Contents"):
        # Get the key (file name) of the object
    key = content.get("Key")
    if key.endswith("/"):
            # Skip if it's a folder
        continue
        # Get the URL of the object
    url = client.generate_presigned_url(ClientMethod='get_object', Params={'Bucket': bucket_name, 'Key': key})
    img_urls.append(url)
# print(img_urls)
for i in img_urls:
    if 'LP_AI2' in i:
        print(i)


#     return render_template('index2.html', img_urls = img_urls)

# if __name__ == '__main__':
#     app.run()
