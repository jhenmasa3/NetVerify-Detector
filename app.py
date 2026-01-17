from flask import Flask, render_template, request
import requests

app = Flask(__name__)

MY_API_KEY = '597f85ec435141b3a8fe529de75b2d7c'

@app.route('/')
def home():
    return render_template('index.html')

import time

@app.route('/analyze', methods=['POST'])
def analyze():
    headline = request.form['headline']
    url = f'https://newsapi.org/v2/everything?q={headline}&language=en&apiKey={MY_API_KEY}'
    
    response = requests.get(url)
    data = response.json()
    total = data.get('totalResults', 0)

    if total > 0:
        result = f"✅ VERIFIED: Nahanap na ang source!"
        color = "green"
    else:
        result = "⏳ SCANNING: Wala pang credible source. Re-checking in background (24h Window)..."
        color = "orange"

    return render_template('index.html', result=result, color=color, headline=headline)

if __name__ == '__main__':
    app.run(debug=True)