
import streamlit as st
from transformers import TrOCRProcessor, VisionEncoderDecoderModel
from PIL import Image
import torch

# Page settings
st.set_page_config(
    page_title="Urdu OCR - Code Saviours SI-26",
    page_icon="📝"
)

st.title("Urdu OCR — Code Saviours SI-26")
st.write("Upload an image containing Urdu text and get the extracted text.")

# Hugging Face model
model_path = "Nadianaz/SI26-urdu-ocr-model-nadia"

@st.cache_resource
def load_model():
    processor = TrOCRProcessor.from_pretrained(model_path, use_fast=False)
    model = VisionEncoderDecoderModel.from_pretrained(model_path)
    model.eval()
    return processor, model

processor, model = load_model()

# Upload image
uploaded_file = st.file_uploader(
    "Upload Urdu Image",
    type=["png", "jpg", "jpeg"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file).convert("RGB")

    st.image(image, caption="Uploaded Urdu Image")

    if st.button("Extract Urdu Text"):

        pixel_values = processor(
            image,
            return_tensors="pt"
        ).pixel_values

        with torch.no_grad():
            generated_ids = model.generate(pixel_values)

        text = processor.batch_decode(
            generated_ids,
            skip_special_tokens=True
        )[0]

        if text:
            st.subheader("Extracted Urdu Text")
            st.write(text)
        else:
            st.write("Could not extract text from this image.")
