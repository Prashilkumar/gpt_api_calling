---

# 🧠 OpenAI Image ↔ Text Toolkit

An **AI-powered Streamlit application** that converts images into descriptive text and generates AI images from text prompts using **OpenAI’s GPT-4o** and **DALL·E models**.

---

## 🚀 Features

* 🖼️ **Image ➜ Text:** Upload an image and get a detailed caption + OCR-style text extraction.
* ✍️ **Text ➜ Image:** Generate AI images from descriptive text prompts.
* 🧩 **Streamlit Interface:** Clean, interactive UI with live previews.
* ⚙️ **OpenAI Integration:** Uses the official OpenAI Python SDK for multimodal and image generation APIs.
* 🔒 **Error Safe:** Catches and displays errors neatly within the UI.

---

## 🗂️ Project Structure

```
openai_image_text_toolkit/
│
├── backend/
│   ├── image_to_text.py        # Image→Text (GPT-4o Vision)
│   ├── text_to_image.py        # Text→Image (DALL·E)
│   ├── openai_client.py        # OpenAI client instance
│   ├── utils.py                # Helper utilities (validation, conversion)
│
├── app.py                      # Streamlit main app
├── requirements.txt            # Python dependencies
├── main.py                     # All Debug codes
├── img.png                     # image for testing (Image->Text)
├── data.json                   # prompt for testing (Text->Image)
└── README.md                   # Project documentation
```

---

## 🧰 Requirements

* Python 3.8+
* OpenAI SDK
* Streamlit
* Pillow (for image processing)

Install all dependencies:

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Setup

Set your OpenAI API key before running:

```bash
export OPENAI_API_KEY="your_openai_api_key_here"
```

*(Windows PowerShell)*

```powershell
setx OPENAI_API_KEY "your_openai_api_key_here"
```

---

## ▶️ Run the App

Start the Streamlit app:

```bash
streamlit run app.py
```

You’ll see output like:

```
  Local URL: http://localhost:8501
  Network URL: http://192.168.x.x:8501
```

Open the local URL in your browser.

---

## 💡 How It Works

### 🖼️ 1️⃣ Image → Text

1. Upload any image (PNG, JPG, JPEG).
2. The app sends it to OpenAI GPT-4o Vision endpoint.
3. You get:

   * A detailed description of the image
   * Any visible text detected within it

🧠 **Under the Hood:**
`backend/image_to_text.py` encodes the image in Base64 and uses the `responses.create()` call from the OpenAI SDK to request the GPT-4o-mini model for captioning.

---

### ✍️ 2️⃣ Text → Image

1. Type your description (e.g., “A futuristic cityscape with flying cars”).
2. The app uses DALL·E via OpenAI’s image generation API.
3. Generated images are displayed instantly inside the Streamlit UI.

🧠 **Under the Hood:**
`backend/text_to_image.py` uses `client.images.generate()` to create an image and returns a base64-encoded preview.

---

## 🧑‍💻 Author

**Prashilkumar Khurpe**
Data Scientist & AI Engineer
🔗 *OpenAI Vision + DALL·E Integration with Streamlit*

---