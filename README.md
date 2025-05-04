# FlaskStarter

A minimal, scalable Flask project structure for quick starts.

## 🚀 Features

- Blueprint-based architecture
- Error handling (404 example)
- Static & template file support
- Environment config with `.env`

## 🗂️ File Structure

```txt
.
├── README.md
├── app
│   ├── __init__.py
│   ├── errors
│   │   ├── __init__.py
│   │   └── handlers.py
│   ├── routes
│   │   ├── __init__.py
│   │   └── main.py
│   ├── static
│   │   ├── css
│   │   │   └── style.css
│   │   └── js
│   │       └── script.js
│   └── templates
│       ├── 404.html
│       └── index.html
├── config.py
├── requirements.txt
└── run.py
```

## 🛠️ Setup Instructions

### macOS / Linux

```bash
# Clone or download the project
cd FlaskStarter

# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python3 run.py
```

### Windows (Command Prompt)

```bash
# Clone or download the project
cd FlaskStarter

# Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python run.py
```
