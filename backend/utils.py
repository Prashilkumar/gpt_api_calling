import base64
from io import BytesIO
from PIL import Image
from typing import Tuple

def image_bytes_to_base64(img_bytes:bytes)->str:
    return base64.b64encode(img_bytes).decode('utf-8')

def pil_image_to_bytes(img:Image.Image,fmt:str='PNG')->bytes:
    buf= BytesIO()
    img.save(buf,format=fmt)
    return buf.getvalue()

def validate_prompt(prompt:str)->str:
    prompt = (prompt or "").strip()
    if not prompt:
        raise ValueError("Prompt is empty. Please provide a non empty prompt")
    if len(prompt)>2000:
        raise ValueError("Prompt is too long (Max 2000 chars)")
    return prompt

def  validate_image_bytes(img_bytes:bytes)-> None:
    if not img_bytes:
        raise ValueError("Empty Image File")
    if len(img_bytes)>10*1024*1024:
        raise ValueError("Image too large. Max is 10MB allowed")