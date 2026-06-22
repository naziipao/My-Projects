import ollama
import io
from log import logging_function
def scan_image(image, model_name):

    logger = logging_function("scan_image" , "engine")

    """
    Core AI Function: Converts image files to bytes, communicates with Ollama,
    and splits the string output into short and long sections.
    """
    img_byte_arr = io.BytesIO()
    image.save(img_byte_arr, format=image.format)
    img_bytes = img_byte_arr.getvalue()
    
    prompt = """
    Analyze this image with microscopic attention to detail. 

    OUTPUT FORMAT:
    [SHORT]
    Write briefly in natural sentences that summarizes the object. AND if the model number of this product is visible, include it in the summary. If not, just write the summary without it. Do not include any other information in this section.
    
    [LONG]
    Write a single paragraph describing everything you see in the image comprehensively. Do not exceed 7 sentences.
    """
    
    response = ollama.chat(
        model=model_name,
        messages=[{
            'role': 'user',
            'content': prompt,
            'images': [img_bytes]
        }],
        options={'num_ctx': 8192}
    )
    
    full_text = response['message']['content']
    
    # Clean text splitting logic
    if "[SHORT]" in full_text and "[LONG]" in full_text:
        parts = full_text.split("[LONG]")
        short_desc = parts[0].replace("[SHORT]", "").strip()
        long_desc = parts[1].strip()
    else:
        short_desc = "The model failed to format the response with the exact tags."
        long_desc = full_text
        
    logger.info(short_desc)
    logger.info(long_desc)
    return short_desc, long_desc