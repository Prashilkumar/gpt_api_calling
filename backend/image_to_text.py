from typing import Dict,Any
from .openai_client import get_client
from .utils import image_bytes_to_base64, validate_image_bytes

def image_to_text_description(img_bytes:bytes,max_tokens:int=512)->Dict[str,Any]:
    """
    Sends the image to an OpenAI multimodal endpoint and asks for a description.
    Returns a dict with keys: success (bool), text (str) or error (str).
    """
    try: 
        validate_image_bytes(img_bytes)
    except Exception as e:
        return {"success":False, 'error':f"Validation Error: {e}"}
    
    try:
        client = get_client()
    except Exception as e:
        return {"success":False,"error":f"OpenAI client error:{e}"}

    img_b64 = image_bytes_to_base64(img_bytes)
    img_data_uri = f"data:image/png;base,{img_b64}"

    try:
        response = client.chat.completions.create(
            model = 'gpt-4o-mini',
            messages = [{
                'role':"user",
                "content":[
                    {'type':'text','text':"Describe the image in details and list any text available in it"},
                    {'type':'image_url','image_url':{"url":img_data_uri}},
                ],
            },
            ],
            max_tokens =max_tokens,
        )

        text = None
        if hasattr(response,'output') and response.output:
            # Sometimes response.output is a list of items
            try:
                # Join text chunks
                chunks = [getattr(c,'content',getattr(c,'text',str(c))) for c in response.output]
                text = '\n'.join(map(str,chunks))
            except Exception:
                text = str(response.output)
        elif hasattr(response,'choices')and response.choices:
            text = response.choices[0].message.content
        else:
            text = str(response)

        return {"success":True, 'text':text}
    
    except Exception as e:
        return {"success":False, "error":f"OpenAI request Failed: {e}"}

