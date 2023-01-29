from flask import Flask, render_template, request, send_file, send_from_directory
import os
import random
from deep_translator import GoogleTranslator
import openai
import requests
import pandas as pd
import csv
import boto3
import cv2 
import requests
import numpy as np

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "static/images"
app.config['UPLOAD_FOLDER2'] = "static/bookmarks"
# Connect to S3
s3 = boto3.client('s3', aws_access_key_id='AKIAR56QI6RTALXWK3G3',
        aws_secret_access_key='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')


@app.route('/')
def home():
    # return '<button onclick="window.location.href=\'/text_to_image\'">Go to image</button>'
    return render_template('index.html')

@app.route("/main_page",methods = ['GET','POST'])
def text_To_Image():
    # global path_to_save
    # global path_to_save1
    # global path_to_save2
    global image_url
    global image_url1
    global image_url2
    global img_data1
    global img_data2
    global img_data3
    global img_name
    global img_name1
    global img_name2
  #lấy text từ client 
   
    text = request.args.get('text')
    
    if text:
        #Dịch văn bản 
        print("start translate text to english")
        translated_text = GoogleTranslator(source='auto', target='en').translate(text)
        Style_list = [' ','A digital illustration of with clockwork machines, 4k, detailed, trending in artstation, fantasy vivid colors',
                '| anime oil painting high resolution cottagecore ghibli inspired 4k',
                'mid century modern, indoor garden with fountain, retro,m vintage, designer furniture made of wood and plastic, concrete table, wood walls, indoor potted tree, large window, outdoor forest landscape, beautiful sunset, cinematic, concept art, sunstainable architecture, octane render, utopia, ethereal, cinematic light, -ar 16:9 -stylize 45000',
                'futuristic nighttime cyberpunk skyline landscape vista photography by Carr Clifton & Galen Rowell, 16K resolution, Landscape veduta photo by Dustin Lefevre & tdraw, 8k resolution, detailed landscape painting by Ivan Shishkin, DeviantArt, Flickr, rendered in Enscape, Miyazaki, Nausicaa Ghibli, Breath of The Wild, 4k detailed post processing, atmospheric, hyper realistic, 8k, epic composition, cinematic, artstation —ar 16:9',
                'The Legend of Zelda landscape atmospheric, hyper realistic, 8k, epic composition, cinematic, octane render, artstation landscape vista photography by Carr Clifton & Galen Rowell, 16K resolution, Landscape veduta photo by Dustin Lefevre & tdraw, 8k resolution, detailed landscape painting by Ivan Shishkin, DeviantArt, Flickr, rendered in Enscape, Miyazaki, Nausicaa Ghibli, Breath of The Wild, 4k detailed post processing, artstation, rendering by octane, unreal engine ']

        if 'Style1' in text:
            text = text.replace('Style1', "")#xoá chuỗi Style trong chuỗi văn bản 
            styles = Style_list[1] #thay đổi chuỗi Style ở đây
        elif 'Style2' in text:
            text = text.replace('Style2', "")
            styles = Style_list[2] #thay đổi chuỗi Style ở đây
        elif 'Style3' in text:
            text = text.replace('Style3', "")
            styles = Style_list[3] #thay đổi chuỗi Style ở đây
        elif 'Style4' in text:
            text = text.replace('Style4', "")
            styles = Style_list[4] #thay đổi chuỗi Style ở đây
        elif 'Style5' in text:
            text = text.replace('Style5', "")
            styles = Style_list[5] #thay đổi chuỗi Style ở đây
        elif text in text:
            styles = ' ' 
        
        
        #gửi translated_text vào model và chạy
        text_t_img = f"{translated_text},{styles}"
        print(text_t_img)
        #Nhập key dalle e 
        openai.api_key = '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'
        openai.Model.list()
        # Chạy model 
        response = openai.Image.create(prompt=text_t_img, n = 3, size= "1024x1024")
        print(response)
        image_url = response['data'][0]['url'] 
        image_url1 = response['data'][1]['url']
        image_url2 = response['data'][2]['url']
        
        #lưu ảnh#  
        ## tạo một tên ảnh ngẫu nhiên 
        sample_string = 'qwertyuiopasdfghj'
        random_name = ''.join((random.choice(sample_string)) for x in range(len(sample_string)))
        random_name1 = ''.join((random.choice(sample_string)) for x in range(len(sample_string)))
        random_name2 = ''.join((random.choice(sample_string)) for x in range(len(sample_string)))
        img_name = f"img_{random_name}.webp"
        img_name1 = f"img_{random_name1}.webp"
        img_name2 = f"img_{random_name2}.webp"
        

        ###Lưu ảnh vào aws S3
        #lấy ảnh từ url về
        response = requests.get(image_url)
        img_data1 = response.content
        response = requests.get(image_url1)
        img_data2 = response.content
        response = requests.get(image_url2)
        img_data3 = response.content

        # Decode image data and convert it to a numpy array
        img1 = cv2.imdecode(np.frombuffer(img_data1, np.uint8), cv2.IMREAD_UNCHANGED)
        img2 = cv2.imdecode(np.frombuffer(img_data2, np.uint8), cv2.IMREAD_UNCHANGED)
        img3 = cv2.imdecode(np.frombuffer(img_data3, np.uint8), cv2.IMREAD_UNCHANGED)

        # Compress the image using cv2
        params = [cv2.IMWRITE_WEBP_QUALITY, 50]
        result1, encimg1 = cv2.imencode('.webp', img1, params)
        result2, encimg2 = cv2.imencode('.webp', img2, params)
        result3, encimg3 = cv2.imencode('.webp', img3, params)
        # Encode the compressed image data to bytes
        img_bytes1 = encimg1.tobytes()
        img_bytes2 = encimg2.tobytes()
        img_bytes3 = encimg3.tobytes()

        bucket_name = 'my-s3-datofbucket1'

        # Upload the image to S3
        s3.put_object(Body=img_bytes1, Bucket=bucket_name, Key='static/images/'+img_name)
        s3.put_object(Body=img_bytes2, Bucket=bucket_name, Key='static/images/'+img_name1)
        s3.put_object(Body=img_bytes3, Bucket=bucket_name, Key='static/images/'+img_name2)
        
        #lưu dữ liệu promt vào data theo mỗi tên ảnh
        with open('data/prompt_data.csv', 'a', newline='') as csvfile:
        # Create a CSV writer object
            writer = csv.writer(csvfile)

            # Write the data rows
            writer.writerow([img_name, translated_text])
            writer.writerow([img_name1, translated_text])
            writer.writerow([img_name2, translated_text])
            #lấy tên ảnh đã lưu
        # image_path = "img01.png"
        print("have text")

        #Tạo đường dẫn đến các ảnh trên S3
        path_file_img = f'static/images/{img_name}'
        path_file_img1 = f'static/images/{img_name1}'
        path_file_img2 = f'static/images/{img_name2}'

        # Generate the presigned URL
        url = s3.generate_presigned_url(
            'get_object',
            Params={
                'Bucket': bucket_name,
                'Key': path_file_img
            },
            ExpiresIn=3600
        )
        
        url1 = s3.generate_presigned_url(
            'get_object',
            Params={
                'Bucket': bucket_name,
                'Key': path_file_img1
            },
            ExpiresIn=3600
        )
        url2 = s3.generate_presigned_url(
            'get_object',
            Params={
                'Bucket': bucket_name,
                'Key': path_file_img2
            },
            ExpiresIn=3600
        )
        print(url)
        return render_template("main_page.html", user_image = f'{url}', user_image1 = f'{url1}',
                            user_image2 = f'{url2}')
    else:
        return render_template("main_page.html")
    
# @app.route('/download1')
# def download_img1():
#     img1 = path_to_save
#     return send_file(img1,as_attachment=True)

# @app.route('/download2')
# def download_img2():
#     img1 = path_to_save1
#     return send_file(img1,as_attachment=True)

# @app.route('/download3')
# def download_img3():
#     img1 = path_to_save2
#     return send_file(img1,as_attachment=True)

@app.route('/addBM', methods=['POST'])
def get_img_bookmarks():
    bucket_name = 'my-s3-datofbucket1'
    # # Lấy tên của hình ảnh từ request body
    image_path = request.form['image_path']
    img_name_path = image_path.split("?")[0]
    print(img_name_path)
    img_name = img_name_path[-26:]
    print(img_name)

    # Define the source and destination paths
    source_path = f'static/images/{img_name}'
    destination_path = f'static/bookmark/{img_name}'
    
    # Use the S3 client to copy the image file
    s3.copy_object(Bucket=bucket_name, CopySource={'Bucket': bucket_name, 'Key': source_path}, Key=destination_path)
    
    return 'Image file copied successfully'

    # # Lấy đường dẫn của hình ảnh từ request body
    # image_path = request.form['image_path']
    # print(image_path,"type:",type(image_path))
    # n = 25
    # image_name = image_path[-n:]
    # print(image_name)
    # images_path = image_path[-39:]
    # bookmark_path = f'Bookmarks/{image_name}'
    # shutil.copyfile(images_path,bookmark_path)
    # # Tải hình ảnh từ đường dẫn
    # response = requests.get(image_path, stream=True)
    # print(response.raw)
    # # Mở file để ghi hình ảnh vào
    # with open(f'Bookmarks/{image_name}', 'wb') as out_file:
    #     # Copy hình ảnh từ response vào file
    #     shutil.copyfileobj(response.raw, out_file)

    # return 'Đã copy hình ảnh vào thư mục Bookmarks'


# @app.route('/Bookmarks/<path:path>')
# def send_image(path):
#     return send_from_directory('Bookmarks', path)

@app.route('/bookmarks')
def show_bookmars():
    #đọc file CSV xuất ra data
    df = pd.read_csv('data/prompt_data.csv')

    # chuyển data sang dạng mảng numpy
    array = df.values

    # lấy danh sách url các file ảnh có trong thư mục bookmarks
    session = boto3.Session(
        aws_access_key_id='AKIAR56QI6RTALXWK3G3',
        aws_secret_access_key='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',
        region_name='ap-northeast-1'
    )
    client = session.client('s3', endpoint_url='https://s3.ap-northeast-1.amazonaws.com')

    # Set the desired bucket name
    bucket_name = 'my-s3-datofbucket1'
    # Set the desired folder name
    folder_name = 'static/bookmark/'

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
        
    return render_template('bookmarks.html', img_urls= img_urls, array = array)

@app.route('/static/images/<path:path>')
def send_image2(path):
    return send_from_directory('static/images', path)

# @app.route('/images')
# def show_images():
#     #đọc file CSV xuất ra data
#     df = pd.read_csv('data/prompt_data.csv')

#     # chuyển data sang dạng mảng numpy
#     array = df.values

#     # lấy danh sách tên các file ảnh có trong thư mục bookmarks
#     images = os.listdir('static/images')
#     return render_template('images.html', images= images, array = array)
@app.route('/images')
def show_images():
    #đọc file CSV xuất ra data
    df = pd.read_csv('data/prompt_data.csv')

    # chuyển data sang dạng mảng numpy
    array = df.values

    # lấy danh sách url các file ảnh có trong thư mục bookmarks
    session = boto3.Session(
        aws_access_key_id='AKIAR56QI6RTALXWK3G3',
        aws_secret_access_key='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',
        region_name='ap-northeast-1'
    )
    client = session.client('s3', endpoint_url='https://s3.ap-northeast-1.amazonaws.com')

    # Set the desired bucket name
    bucket_name = 'my-s3-datofbucket1'
    # Set the desired folder name
    folder_name = 'static/images/'

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
        
    return render_template('images.html', img_urls= img_urls, array = array)


@app.route('/ranking')
def ranking():
    return render_template('ranking.html')

# @app.route('/bookmarks')
# def bookmarks():
#     return render_template('bookmarks.html')

@app.route('/Help&FAQ')
def Help_FAQ():
    return render_template('help&faq.html')




#start server 
if __name__ == '__main__':
    app.run()
