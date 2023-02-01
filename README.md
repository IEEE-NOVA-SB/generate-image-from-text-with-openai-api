# generate-image-from-text-with-openai-api
Generate image from text with openai api

#Para documentação

#import gradio as gr
#from PIL import Image
#import requests
#from io import BytesIO


'''
response = requests.get(image_url)
img = Image.open(BytesIO(response.content))
img.save('./projects/generate-image/', 'JPEG')
'''



'''
import gradio as gr
from PIL import Image

img = Image.open("path/to/image.jpg")

def show_image(img):
    return img

inputs = gr.inputs.Image(shape=(None, None, 3))
output = gr.outputs.Image()
interface = gr.Interface(fn=show_image, inputs=inputs, outputs=output, title="Show Image")

interface.launch()
'''


'''
import requests
from io import BytesIO
from PIL import Image

url = "https://example.com/image.jpg"
response = requests.get(url)
img = Image.open(BytesIO(response.content))
img.show()

'''
