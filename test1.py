image_url = "https://oaidalleapiprodscus.blob.core.windows.net/private/org-mGqTIQna9KUtkQ88MPKZH1hJ/user-FMimY3Zbo4Xkw4UU7YYL7oSx/img-Sr1xDVVsqKhZYs5vtwwUhdlC.png?st=2023-01-28T04%3A02%3A09Z&se=2023-01-28T06%3A02%3A09Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2023-01-27T23%3A33%3A41Z&ske=2023-01-28T23%3A33%3A41Z&sks=b&skv=2021-08-06&sig=pG%2Be60ZxWZ1CF5TbqbZbwseV8wT1RmzTba15eqK7hbk%3D"
#
# n = len(string.split("?")[0])
# img_name_path = string.split("?")[0]
# print(img_name_path)
# img_name = img_name_path[-25:]
# print(img_name)
import cv2
import boto3
import requests
import numpy as np

# Get image data from image URL
response = requests.get(image_url)
img_data = response.content

# Decode image data and convert it to a numpy array
img = cv2.imdecode(np.frombuffer(img_data, np.uint8), cv2.IMREAD_UNCHANGED)

# Compress the image using cv2
params = [cv2.IMWRITE_WEBP_QUALITY, 50]
result, encimg = cv2.imencode('.webp', img, params)

# Encode the compressed image data to bytes
img_bytes = encimg.tobytes()

# Connect to S3 and upload the image
s3 = boto3.client('s3', aws_access_key_id='AKIAR56QI6RTALXWK3G3',
        aws_secret_access_key='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')
s3.put_object(Bucket='my-s3-datofbucket1', Key='image_EX.webp', Body=img_bytes)

