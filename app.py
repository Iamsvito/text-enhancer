from flask import Flask, render_template, request
import openai
import spacy
import nltk
from nltk.corpus import wordnet as wn
from dotenv import load_dotenv
import os

# 初始化 Flask 应用
app = Flask(__name__)

load_dotenv()
# 配置 OpenAI API 密钥
openai_api_key = os.getenv("OPENAI_API_KEY")

# 加载 SpaCy 英文模型
nlp = spacy.load("en_core_web_sm")
nltk.download('wordnet')

# SpaCy 分词和词性标注
def spacy_process(text):
    doc = nlp(text)
    return [(token.text, token.pos_) for token in doc]

# 使用 GPT 进行语言提升
def gpt_process(text, level):
    prompt = f"請根據 CEFR {level} 等級，將下面的文本進行語言提升，將簡單的詞語換成更高級的同義詞，保持語境自然：\n{text}"

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=150,
        temperature=0.7
    )

    return response['choices'][0]['message']['content'].strip()

# 处理文本管道
def process_text_pipeline(text, level):
    tagged_words = spacy_process(text)

    enhanced_words = []
    for word, tag in tagged_words:
        if tag in ['NOUN', 'VERB', 'ADJ', 'ADV']:
            synonyms = wn.synsets(word)
            if synonyms:
                synonym = synonyms[0].lemmas()[0].name()
                enhanced_words.append(synonym)
            else:
                enhanced_words.append(word)
        else:
            enhanced_words.append(word)

    nltk_text = ' '.join(enhanced_words)
    gpt_text = gpt_process(nltk_text, level)
    return gpt_text

# 定义主页路由
@app.route('/', methods=['GET', 'POST'])
def index():
    enhanced_text = None
    if request.method == 'POST':
        input_text = request.form['inputText']
        cefr_level = request.form['cefrLevel']
        enhanced_text = process_text_pipeline(input_text, cefr_level)
    
    return render_template('index.html', enhanced_text=enhanced_text)

# 启动应用
if __name__ == '__main__':
    app.run(debug=True)



