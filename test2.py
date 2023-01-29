import openai

text_t_img = 'Messi and his dog play tennis anime style'
openai.api_key = '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'
openai.Model.list()
        # Chạy model 
response = openai.Image.create(prompt=text_t_img, n = 1, size= "1024x1024")
print(response)
image_url = response['data'][0]['url'] 
print(image_url)