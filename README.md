# Medicine-Detector

🩺 Medicine Detection Web App

A web-based application for detecting and retrieving usage information about medicines from A to Z, built using Python and Streamlit.

🚀 Project Overview

This project allows users to input the name of a medicine and receive detailed usage information about it. The application uses a preloaded dataset of medicines, making it useful for both patients and healthcare providers looking for quick references.


 🔍 Features

- Simple and intuitive UI with Streamlit.
- Medicine name search with auto-matching.
- Displays usage or description for selected medicines.
- Includes a dataset covering a wide range of medicines from A to Z.

Dataset

  Filename: `A_Z_medicines_dataset_with_usage.csv`

- Columns:
  - `Medicine` – Name of the medicine
  - `Description` – Usage or purpose of the medicine
- Size: ~26,000+ rows (depending on version)

This dataset serves as the knowledge base of the application.

 🛠️ Tech Stack

- Python 3
- Streamlit – For interactive web UI
- Pandas – For handling CSV data
- Virtual Environment (`.venv`) – For dependency management

Folder Structure

    Medicine Detection/
    │
    ├── app.py                         
    ├── A_Z_medicines_dataset_with_usage.csv 
    ├── requirements.txt            

Installation & Running the App

1. Clone the repository:
 
   git clone https://github.com/ambily08/medicine-detection.git
   cd medicine-detection
   
2. Create a virtual environment:
   
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install dependencies:

   pip install -r requirements.txt

4. Run the app:

   streamlit run app.py


                   
