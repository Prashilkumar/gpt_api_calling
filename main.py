from flask import Flask,request,jsonify
from openai import OpenAI
import base64
from dotenv import load_dotenv
import os
load_dotenv()

app = Flask(__name__)
client=OpenAI(api_key = os.getenv('OPENAI_API_KEY'))

#---------------Route:Image -> Text (OCR/Description)------------------------------
@app.route('/image-to-text',methods=['POST'])
def image_to_text():
    if 'image' not in request.files:
        return jsonify({'error':"No Image Uploaded"}),400
    
    image_file = request.files['image']
    image_bytes = image_file.read()

    response  = client.chat.completions.create(
        model='gpt-4o-mini',
        messages = [
            {
                'role':'user', 'content':[
                    {'type':'input_text','text':'Describe the content of this image'},
                    {'type':'input_image','image':base64.b64encode(image_bytes).decode("utf-8")},
                ]
            }
        ]
    )

    text_output = response.choices[0].message['content'][0]['text']
    return jsonify({"describe":text_output})




#---------------Route:Image -> Text (OCR/Description)------------------------------

@app.route('/text-to-image',methods=['POST'])
def text_to_image():
    data = request.get_json()
    if not data or 'prompt' not in data:
        return jsonify({"error":"No prompt provided"}),400

    prompt = data['prompt']
    
    response = client.images.generate(
        model = 'gpt-image-1',
        prompt = prompt,
        size = "1024x1024"
    )

    image_url = response.data[0].url
    return jsonify({"image_url":image_url})



# To run script 

if __name__=='__main__':
    app.run(debug=True)
    



## To Test Text to Image 
#curl.exe -X POST http://127.0.0.1:5000/text-to-image -H "Content-Type: application/json" -d "@data.json"

## To Test Image to Text
#curl.exe -X POST http://127.0.0.1:5000/text-to-image -H "Content-Type: application/json" -d '{"prompt":"A futuristic cityscape with flying cars"}'






#################################################################################







## Debug for -> openai_client.py

# from backend.openai_client import get_client


# if __name__== "__main__":
#     try:
#         client = get_client()
#         print("Client Successfully Initiated",client)
#     except Exception as e:
#         print("Error: ",{e})


#################################################################################

# Debug Testing for -> utils.py

# from backend.utils import image_bytes_to_base64,pil_image_to_bytes,validate_prompt,validate_image_bytes
# from PIL import Image
# import io


# if __name__=="__main__":
#     # Test prompt validation
#     try:
#         print("Valid prompt:",validate_prompt("Hello World"))
#         print(" This should fail",validate_prompt(""))

#     except Exception as e:
#         print("Caugth error as expected",e)
    
#     # Test Image validation
#     img = Image.new("RGB",(50,50),color='blue')
#     img_bytes = pil_image_to_bytes(img)
#     try:
#         validate_image_bytes(img_bytes)
#         print("Image validation passed")
#     except Exception as e:
#         print("Image validation failed:",e)
    
#     # Test base64 conversion
#     b64 = image_bytes_to_base64(img_bytes)
#     print("Base64 length",len(b64))


#################################################################################

# Debug Testing for -> image_to_text.py

# from backend.image_to_text import image_to_text_description
# from backend.utils import pil_image_to_bytes
# from PIL import Image

# if __name__=="__main__":
#     # Create a simple image for testing
#     img = Image.new("RGB",(100,50),color='red')
#     img_bytes = pil_image_to_bytes(img)

#     result = image_to_text_description(img_bytes)
#     print(result)


#################################################################################

# debug_text_to_image.py
# from backend.text_to_image import text_to_image_base64

# if __name__ == "__main__":
#     prompt = "A cute robot playing guitar in a park"
#     result = text_to_image_base64(prompt, size="auto", n=1)
#     print(result)

#     if result.get("success"):
#         img_data = result["images"][0]
#         if "b64" in img_data:
#             print("✅ Got base64 image, length:", len(img_data["b64"]))
#         elif "url" in img_data:
#             print("✅ Got image URL:", img_data["url"])
