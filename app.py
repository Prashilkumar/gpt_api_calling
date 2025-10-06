import streamlit as st
from backend.image_to_text import image_to_text_description
from backend.text_to_image import text_to_image_base64
from backend.utils import pil_image_to_bytes
from PIL import Image
import base64
import io

st.set_page_config(page_title='Image Text with OpenAI',layout='wide')
st.title("Image to Text - OpenAI Demo")

st.sidebar.header("Configuration")
mode = st.sidebar.radio("Mode",["Image -> Text", "Text -> Image"])

if mode =="Image -> Text":
    st.header("Image to Text")
    uploaded = st.file_uploader("Upload an image",type=["png","jpg","jpeg","bmp","tiff"])
    if uploaded is not None:
        try:
            img = Image.open(uploaded).convert('RGB')
            st.image(img,caption='Uploaded Image',width='stretch')
            if st.button("Describe Image"):
                with st.spinner("Contacting OpenAI..."):

                    img_bytes = io.BytesIO()
                    img.save(img_bytes,format='PNG')
                    response = image_to_text_description(img_bytes.getvalue())
                if response.get('success'):
                    st.subheader("Description / Extracted Text")
                    st.text_area("Result",value=response.get('text',''),height=300)
                else:
                    st.error(response.get('error'))            

        except Exception as e:
            st.error(f"Failed to Process image:{e}")

else:
    st.header("Text to Image")
    prompt = st.text_area("Prompt",height=600)
    size  = st.selectbox("Size",["1024 x 1024","1536 x 1024 ","1024 x 1536"],index = 1) 
    num = st.slider("Number of images",1,4,1)

    if st.button('Generate Image(s)'):
        try:
            with st.spinner("Generating Images..."):
                response = text_to_image_base64(prompt,size=size,n=num)
            if not response.get('success'):
                st.error(response.get('error'))
            else:
                for i, item in enumerate(response.get('images',[])):
                    st.subheader(f"Image{i+1}")
                    if 'b64' in item:
                        b = item['b64']
                        img_bytes = io.BytesIO(base64.b64decode(b))
                        img = Image.open(img_bytes)
                        st.Image(img,use_column_width=True)
                        # Download button
                        st.download_button(f"Download Image {i+1}",data=img_bytes.getvalue(),file_name=f"generated_{i+1}.png")
                    elif 'url' in item:
                        st.write("Image URL:",item['url'])
                    else:
                        st.write(item)

        except Exception as e:
            st.error(f"Generation Failed:{e}")              