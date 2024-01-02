# PictureTales

PictureTales allows you to upload an image, and it will generate a short story based on the image's content using image captioning. The generated story is then converted to audio using text-to-speech technology. You can both see the generated story and listen to it.

# Demo
- Launching the application
![01](https://github.com/SartajBhuvaji/Image-to-Story-Generator/assets/31826483/984ad132-14eb-4ddf-8e5a-33fe2a7c7b28)

- Select an image and Upload
![02](https://github.com/SartajBhuvaji/Image-to-Story-Generator/assets/31826483/20ef38ee-562f-4cfa-9d64-3f01e85f231b)

- Image
![beach (1)](https://github.com/SartajBhuvaji/Image-to-Story-Generator/assets/31826483/69a5b52b-c6dd-41cb-889b-486977ebf37c)


- Download the audio story
  
https://github.com/SartajBhuvaji/Image-to-Story-Generator/assets/31826483/1fe00f34-9716-4047-9b57-a7794524816a


## Features

- Upload an image.
- Generate a story based on the content of the image.
- Listen to the generated story as an audio file.

## Usage

1. Clone this repository to your local machine.

```bash
git clone https://github.com/SartajBhuvaji/Image-to-Story-Generator.git

pip install -r requirements.txt

python app.py
```
- Create a .env file and paste your HUGGINGFACE, OPEN AI API Keys (Check the dummy_env file)
- Open your web browser and navigate to http://localhost:7860 to access the app.
- Upload an image to the app and click "Generate Story." You will see the generated story and be able to listen to it as audio.

# Tech
- HuggingFace
- Image to Caption model
- Chat GPT 3.5 LLM
- Text-to-speech 
