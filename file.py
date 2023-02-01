import openai
import webbrowser

# Setting the API key for the OpenAI API.
#https://www.youtube.com/watch?v=DFmmiYlbgX0 -  How to get your OpenAI API key - Fun with Dall-E 
#https://platform.openai.com/account/api-keys

openai.api_key = ''


# Asking the user to input a description of the image they want to create.
user_input = input("Enter a description of your image: ")

# Creating an image based on the prompt.
response = openai.Image.create(
  prompt=user_input,
  n=1,
  size="1024x1024"
)

# Getting the url of the image that was created.
image_url = response['data'][0]['url']

# It opens the image in a new tab in the default browser.
webbrowser.open(image_url)