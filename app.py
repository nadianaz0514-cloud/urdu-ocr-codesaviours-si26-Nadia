import streamlit as st
from transformers import (
    VisionEncoderDecoderModel,
    AutoImageProcessor,
    AutoTokenizer
)
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

    # Load image processor
    image_processor = AutoImageProcessor.from_pretrained(
        model_path
    )

    # Load tokenizer
    tokenizer = AutoTokenizer.from_pretrained(
        model_path,
        use_fast=False
    )

    # Load trained OCR model
    model = VisionEncoderDecoderModel.from_pretrained(
        model_path
    )

    model.eval()

    return image_processor, tokenizer, model


image_processor, tokenizer, model = load_model()


# Upload image
uploaded_file = st.file_uploader(
    "Upload Urdu Image",
    type=["png", "jpg", "jpeg"]
)


if uploaded_file is not None:

    image = Image.open(uploaded_file).convert("RGB")

    st.image(
        image,
        caption="Uploaded Urdu Image"
    )

    if st.button("Extract Urdu Text"):

        # Process image
        pixel_values = image_processor(
            images=image,
            return_tensors="pt"
        ).pixel_values

        # Generate prediction
        with torch.no_grad():

            generated_ids = model.generate(
                pixel_values,
                max_length=128
            )

        # Convert prediction to text
        text = tokenizer.batch_decode(
            generated_ids,
            skip_special_tokens=True
        )[0].strip()

        if text:

            st.subheader("Extracted Urdu Text")
            st.write(text)

        else:

            st.write(
                "Could not extract text from this image."
            )
