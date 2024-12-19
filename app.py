from flask import Flask, render_template, request, Markup
import openai
import spacy
import nltk
from nltk.corpus import wordnet as wn
from dotenv import load_dotenv
import os

# 初始化 Flask 应用
app = Flask(__name__)

# 加载环境变量
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# 加载 SpaCy 英文模型
nlp = spacy.load("en_core_web_sm")
try:
    nltk.data.find('corpora/wordnet')
except LookupError:
    nltk.download('wordnet')

# 处理文本
def spacy_process(text):
    doc = nlp(text)
    return [(token.text, token.pos_) for token in doc]

def gpt_process(text, level):
    prompt = f"請根據 CEFR {level} 等級，將下面的文本進行語言提升，保持語境自然：\n{text}"
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000,
            temperature=0.7
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        print(f"Error with OpenAI API: {e}")
        return "Error: Unable to process your request."

def process_text_pipeline(text, level):
    tagged_words = spacy_process(text)
    enhanced_words = [wn.synsets(word)[0].lemmas()[0].name() if tag in ['NOUN', 'VERB', 'ADJ', 'ADV'] and wn.synsets(word) else word for word, tag in tagged_words]
    nltk_text = ' '.join(enhanced_words)
    gpt_text = gpt_process(nltk_text, level)
    return gpt_text

@app.route('/', methods=['GET', 'POST'])
def index():
    enhanced_text = None
    if request.method == 'POST':
        input_text = request.form['inputText']
        cefr_level = request.form['cefrLevel']
        enhanced_text = process_text_pipeline(input_text, cefr_level)
    return render_template('index.html', enhanced_text=Markup(enhanced_text) if enhanced_text else None)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)




