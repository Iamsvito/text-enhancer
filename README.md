# Text Enhancer

Text Enhancer is a Flask-based web application designed to enhance text quality using OpenAI's GPT models.

## Features

- **Tokenization and Part-of-Speech Tagging**: Utilizes SpaCy for text tokenization and tagging.
- **Synonym Replacement**: Offers basic synonym enhancements using NLTK.
- **Advanced Language Processing**: Enhances text quality based on CEFR levels using OpenAI GPT models.
- **Web Interface**: Provides a user-friendly interface for text input and real-time processing.

## Project Structure

```
/text-enhancer
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── runtime.txt         # Python runtime version
├── Procfile            # Heroku deployment command
├── templates/          # HTML templates
│   └── index.html
├── static/             # Static files (CSS, JS, images)
│   ├── style.css
│   └── script.js
└── README.md           # Project documentation
```

## Technology Stack

- **Backend**:
  - Python 3.12.x
  - Flask
  - OpenAI API
  - SpaCy
  - NLTK
- **Frontend**:
  - HTML5
  - JavaScript
  - Bootstrap (optional)
- **Deployment**:
  - Heroku

## Installation and Running

1. **Clone the repository**

   ```bash
   git clone https://github.com/Iamsvito/text-enhancer.git
   cd text-enhancer
   ```

2. **Create a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/MacOS
   venv\Scripts\activate     # Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set OpenAI API Key**

   Configure your OpenAI API key in the application to enable interaction with the GPT models.

5. **Run the application**

   ```bash
   python app.py
   ```

6. **Access the application**

   Open `http://localhost:5000` in your web browser to use the application.

## Deploying to Heroku

1. **Login to Heroku**

   ```bash
   heroku login
   ```

2. **Create a Heroku application**

   ```bash
   heroku create your-app-name
   ```

3. **Deploy the code**

   ```bash
   git push heroku main
   ```

4. **Set environment variables**

   ```bash
   heroku config:set OPENAI_API_KEY=your_openai_api_key
   ```

5. **Open the application**

   ```bash
   heroku open
   ```

## Contributing

We welcome contributions to this project. You can contribute by:

1. **Forking the repository**
2. **Creating a feature branch**

   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Committing your changes**

   ```bash
   git commit -m 'Add new feature'
   ```

4. **Pushing to your branch**

   ```bash
   git push origin feature/your-feature-name
   ```

5. **Creating a Pull Request**

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Acknowledgments

Thanks to everyone who contributed to this project.
