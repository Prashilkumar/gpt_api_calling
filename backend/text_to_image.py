from typing import Dict,Any
from .openai_client import get_client
from .utils import validate_prompt
import base64

def text_to_image_base64(prompt:str,size:str="auto",n:int=1)->Dict[str,Any]:
    """
    Generates images from text. Returns base64 encoded PNG(s) in 'images' list.
    Each item is a dict: {"b64": <base64str>, "mime": "image/png"}
    """

    try:
        prompt = validate_prompt(prompt)
    except Exception as e:
        return {'success':False, "error":f"prompt validation failed: {e}"}
    
    try:
        client = get_client()
    except Exception as e:
        return {"success":False,"error":f"OpenAI client error"}
    
    try: 
        gen = client.images.generate(
            model = 'gpt-image-1',
            prompt=prompt,
            size = size,
            n=n
        )

        images = []

    # SDK may return data with b64_json or url. Prefer base64 if present.
        for item in gen.data:
            # item could have 'b64_json' or 'url':
            if 'b64_json' in item:
                images.append({"b64":item['b64_json'],'mime':"image/png"})
            elif 'url' in item:
                # If only URL provided, return URL (caller may want to fetch it)
                images.append({"url":item['url']})

            else:
                images.append({"raw":str(item)})
        return {"success":True, "images":images}
    
    except Exception as e:
        return {'success':False,"error":f"OpenAI image generation failed:{e}"}