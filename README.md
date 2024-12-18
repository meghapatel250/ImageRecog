

# Image Recognition Web App

This project is a **Image Recognition Web Application** built with **Flask** (for the backend) and **TensorFlow** (for image classification). The application allows users to upload an image and receive predictions on what the image contains, using a pre-trained **MobileNetV2** model from TensorFlow.

---

## Table of Contents
- [Requirements](#requirements)
- [Installation](#installation)
- [Running the Project](#running-the-project)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [License](#license)

---

## Requirements

To run the project, you need the following:

- Python 3.6+
- Flask
- TensorFlow
- Pillow
- Jinja2

You can install these dependencies via a **Python virtual environment** (recommended).

---

## Installation

### 1. **Clone the Repository**
Clone the project repository to your local machine:

```bash
git clone https://github.com/yourusername/ImageRecognitionApp.git
cd ImageRecognitionApp
```

### 2. **Create a Virtual Environment (Optional but Recommended)**

It's a good practice to use a virtual environment to manage dependencies. Run the following commands to create a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate  # For Linux/Mac
# For Windows use: venv\Scripts\activate
```

### 3. **Install Dependencies**

Once inside the virtual environment, install the required dependencies:

```bash
pip install -r requirements.txt
```

Alternatively, you can manually install the dependencies using `pip`:

```bash
pip install flask tensorflow pillow
```

### 4. **Download Pre-trained Model**

The project uses **MobileNetV2** from TensorFlow for image classification. The model is pre-trained on the **ImageNet** dataset and is loaded automatically when you run the app. The model will be downloaded the first time the app is run.

---

## Running the Project

### 1. **Start the Flask Server**

To run the web application, navigate to the project folder (if you're not already there) and execute the following command:

```bash
python3 app.py
```

This will start the Flask development server. By default, the server will run on `http://127.0.0.1:5000`.

### 2. **Access the Application**

- Open a web browser.
- Go to `http://127.0.0.1:5000` to access the app.
- You can upload an image, and the app will display the predicted label along with the confidence level.

---

## Usage

1. **Homepage**: The home page (`index.html`) will ask you to upload an image for recognition.
2. **Upload**: Select an image (in PNG, JPG, or JPEG format).
3. **Results**: After uploading, the app will display the prediction result, which includes:
   - **Predicted Label**: The classification result from the model.
   - **Confidence**: The confidence level of the prediction.
4. **Go Back**: You can go back to the home page to upload another image.

---

## Project Structure

Here's the basic structure of the project:

```
ImageRecognitionApp/
│
├── app.py                 # Flask application code
├── model.py               # TensorFlow model loading and prediction logic
├── requirements.txt       # List of dependencies
├── static/                # Folder for storing uploaded images
│   └── uploads/           # Folder for uploaded images
├── templates/             # HTML templates for the app
│   ├── index.html         # Home page template
│   └── result.html        # Results page template
│
└── .gitignore             # Git ignore file (for excluding files from version control)
```

### `app.py`

This file contains the Flask application that handles the routing, image uploads, and predictions. It uses the `model.py` file to load the TensorFlow model and make predictions on the uploaded images.

### `model.py`

This file loads the pre-trained **MobileNetV2** model from TensorFlow and includes the logic for preprocessing images and predicting labels using the model.

### `static/uploads/`

This folder stores the uploaded images temporarily so that the Flask app can process them and display the results.

### `templates/`

This folder contains HTML templates used by Flask:
- `index.html`: The homepage template where users can upload an image.
- `result.html`: The results page template where users can see the prediction result.

### `requirements.txt`

A list of Python dependencies for your project, which can be installed using:

```bash
pip install -r requirements.txt
```

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Troubleshooting

1. **ModuleNotFoundError: No module named 'flask'**  
   If you encounter this error, ensure that you've installed all dependencies using:
   ```bash
   pip install -r requirements.txt
   ```
   or ensure the virtual environment is activated properly.

2. **TemplateNotFound Error**  
   If you encounter a `TemplateNotFound` error for `error.html` or other templates, ensure that you have the correct templates in the `templates/` folder.

3. **TensorFlow Model Not Found**  
   If you receive errors related to the model not being found, make sure the `MobileNetV2` model is being loaded correctly. The model will be downloaded automatically when the app is first run.

---
