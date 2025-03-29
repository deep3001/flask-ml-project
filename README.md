# Flask AI Prediction Project

This project is a simple AI model using Flask that allows users to enter data and get predictions.

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/your-repo.git
   cd your-repo
   ```
2. Create a virtual environment and install dependencies:
   ```sh
   python -m venv .venv
   source .venv/bin/activate  # On Windows, use: .venv\Scripts\activate
   pip install -r requirements.txt
   ```

## Usage

1. Run the Flask server:
   ```sh
   python app.py
   ```
2. Open in browser: [http://127.0.0.1:5000](http://127.0.0.1:5000)

## API Endpoint

- **POST** `/predict` → Send JSON data and get a prediction.

## License
MIT License
