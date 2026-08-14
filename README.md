# Urdu OCR Project

**Urdu OCR — A TrOCR-based deep learning model for extracting Urdu text from images.**

## 1. Project Title and Description

Urdu OCR is an Optical Character Recognition (OCR) project developed to recognize and extract Urdu text from images. The project uses **TrOCR (Transformer-based Optical Character Recognition)** and provides a simple web interface through Streamlit for uploading an image and generating the detected text.

The project was developed as part of the **Code Saviours ML/AI Internship — Batch SI-26**.

---

## 2. What Problem This Solves and Why It Matters

Urdu is a complex language for Optical Character Recognition because of its connected writing style, different fonts, character shapes, and variations in text appearance. Many OCR systems are primarily optimized for English and other widely supported languages, which can result in poor recognition of Urdu text.

This project explores the use of a transformer-based OCR model for recognizing Urdu text from images.

### Real-World Use Case

An Urdu OCR system can help convert printed Urdu books, newspapers, historical documents, educational material, and scanned records into editable digital text. This can support **document digitization, Urdu content preservation, searchable archives, and educational applications**.

---

## 3. How It Works

### What is OCR?

OCR stands for **Optical Character Recognition**. It is a technology that allows a computer to look at an image containing text and convert that text into machine-readable text.

For example:

**Input:** An image containing Urdu text

**Output:** Extracted Urdu text

### What is TrOCR?

This project uses **TrOCR**, a transformer-based OCR architecture developed for recognizing text from images.

The model takes an image as input and predicts the corresponding text sequence.

The basic workflow is:

1. The user uploads an image containing Urdu text.
2. The image is processed and prepared for the OCR model.
3. The TrOCR model analyzes the visual information in the image.
4. The model predicts the text.
5. The extracted text is displayed to the user through the application.

### Fine-Tuning

Fine-tuning means taking an already trained machine learning model and further training it using a dataset designed for a specific task.

For this project, a TrOCR model was adapted for the Urdu OCR task using a custom collection of Urdu text images. The goal was to make the model more suitable for recognizing Urdu rather than relying only on its original training.

The dataset contains **200 Urdu text images** collected from online sources and prepared for the OCR task.

---

## 4. Live Demo / Hugging Face Model

The trained Urdu OCR model is available on Hugging Face:

**Hugging Face:**
https://huggingface.co/Nadianaz/SI26-urdu-ocr-model-nadia

**GitHub Repository:**
https://github.com/nadianaz0514-cloud/urdu-ocr-codesaviours-si26-Nadia

> Note: The Hugging Face URL above is the project model page. The Streamlit application is included in this repository through `app.py`.

---

## 5. How to Run It Locally

Follow the steps below to run the Urdu OCR application on your computer.

### Step 1 — Clone the Repository

```bash
git clone https://github.com/nadianaz0514-cloud/urdu-ocr-codesaviours-si26-Nadia.git
```

Move into the project directory:

```bash
cd urdu-ocr-codesaviours-si26-Nadia
```

### Step 2 — Install the Required Libraries

Install the dependencies using:

```bash
pip install -r requirements.txt
```

The project uses the following main libraries:

* Streamlit
* Transformers
* PyTorch
* Pillow
* SentencePiece
* Torchvision

### Step 3 — Run the Application

Start the Streamlit application using:

```bash
streamlit run app.py
```

### Step 4 — Use the OCR Application

1. Open the local Streamlit URL shown in the terminal.
2. Upload an image containing Urdu text.
3. Allow the application to process the image.
4. The predicted text will be displayed by the application.

---

## 6. Dataset Details

The project dataset contains approximately **200 images** containing Urdu text.

### Dataset Information

| Detail            | Description                                   |
| ----------------- | --------------------------------------------- |
| Total Images      | 200                                           |
| Language          | Urdu                                          |
| Image Type        | Text images                                   |
| Main Source       | Internet / Google                             |
| Collection Method | Images collected and prepared for the project |
| Text Variety      | Different Urdu text samples                   |
| Fonts             | Multiple Urdu font styles                     |
| Font Sizes        | Different sizes                               |
| Backgrounds       | Different backgrounds                         |
| Image Sizes       | Different image dimensions                    |
| Task              | Urdu Optical Character Recognition            |

The dataset was collected from online sources and Google searches and was used to experiment with adapting a TrOCR-based model for Urdu text recognition.

The variety in fonts, sizes, backgrounds, and image dimensions was intended to expose the model to different visual forms of Urdu text.

---

## 7. Results

The final accuracy obtained during **Week 4 evaluation was 0.00%**.

Although the result was low, it provided an important indication that the selected model and training approach were not sufficiently suited to the Urdu OCR task.

### Why Was the Accuracy Low?

One major reason is that the original TrOCR checkpoint used in the project was designed primarily for **printed English text** rather than Urdu. Urdu has a different writing system, connected characters, and different visual patterns.

Therefore, directly applying an English-oriented OCR model to Urdu images can result in very poor recognition performance.

Other possible factors include:

* Limited dataset size of 200 images.
* Differences between the training images and evaluation images.
* Urdu-specific character and word structures.
* Variation in fonts and image quality.
* Insufficient Urdu-specific training data.
* The base model was not originally designed specifically for Urdu OCR.

### What Could Be Improved?

With more time and resources, the project could be improved by:

1. Collecting a much larger Urdu OCR dataset.
2. Using a dataset with accurately verified Urdu text labels.
3. Increasing the number of training examples for different Urdu fonts.
4. Using an OCR model or pretrained checkpoint better suited to Urdu or multilingual text.
5. Performing more extensive fine-tuning.
6. Improving image preprocessing and normalization.
7. Evaluating the model using OCR-specific metrics such as **Character Error Rate (CER)** and **Word Error Rate (WER)**.
8. Testing the model on a larger and more diverse validation dataset.

The **0.00% accuracy result should therefore be viewed as an evaluation outcome that helped identify the limitations of the current approach**, rather than as the final potential of Urdu OCR using transformer-based models.

---

## 8. Credit

**Nadia Naz**

Built during the **Code Saviours ML/AI Internship — Batch SI-26.**

### Technologies Used

* Python
* PyTorch
* Hugging Face Transformers
* TrOCR
* Streamlit
* Gradio
* Pillow
* Torchvision
* SentencePiece

### Project Files

The repository contains the main notebooks and application files used throughout the internship:

```text
README.md
SI26_Week1_Nadia.ipynb
SI26_Week2_Nadia.ipynb
SI26_Week3_Nadia.ipynb
SI26_Week4_Nadia.ipynb
SI26_Week5_Nadia.ipynb
app.py
data.zip
data2.zip
labels.csv
labels_fixed.csv
requirements.txt
```

---

## Project Links

**GitHub Repository:**
https://github.com/nadianaz0514-cloud/urdu-ocr-codesaviours-si26-Nadia

**Hugging Face Model:**
https://huggingface.co/Nadianaz/SI26-urdu-ocr-model-nadia
