!pip install gradio transformers torch pillow

import gradio as gr
from transformers import TrOCRProcessor, VisionEncoderDecoderModel
from PIL import Image
import torch
from google.colab import drive

drive.mount('/content/drive')

model_path = "/content/drive/MyDrive/SI26-urdu-ocr-model"

from transformers import RobertaTokenizer, ViTImageProcessor, TrOCRProcessor

tokenizer = RobertaTokenizer.from_pretrained(model_path)
image_processor = ViTImageProcessor.from_pretrained(model_path)
processor = TrOCRProcessor(image_processor=image_processor, tokenizer=tokenizer)
model = VisionEncoderDecoderModel.from_pretrained(model_path)

model.eval()

def extract_urdu_text(image):
    if image is None:
        return "Please upload an image"

    pixel_values = processor(image, return_tensors="pt").pixel_values

    with torch.no_grad():
        generated_ids = model.generate(pixel_values)

    text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]

    return text if text else "Could not extract text from this image"

interface = gr.Interface(
    fn=extract_urdu_text,
    inputs=gr.Image(type="pil", label="Upload Urdu Image"),
    outputs=gr.Textbox(label="Extracted Urdu Text"),
    title="Urdu OCR -- Code Saviours SI-26",
    description="Upload an image containing Urdu text and get the extracted text.",
    examples=[]
)

interface.launch(share=True)
