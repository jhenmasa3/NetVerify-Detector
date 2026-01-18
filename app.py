from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Palitan ito ng iyong actual News API Key
API_KEY = '597f85ec435141b3a8fe529de75b2d7c'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    # Kukunin nito ang text mula sa name="headline" sa HTML mo
    user_headline = request.form.get('headline') 
    
    # News API request
    url = f'https://newsapi.org/v2/everything?q={user_headline}&apiKey={API_KEY}'
    response = requests.get(url)
    data = response.json()
    
    # Logic para sa result at kulay
    if data.get('totalResults', 0) > 0:
        res = "VERIFIED NEWS"
        clr = "#10b981" # Green
    else:
        res = "UNVERIFIED / POTENTIAL FAKE"
        clr = "#ef4444" # Red
        
    return render_template('index.html', result=res, color=clr, headline=user_headline)

if __name__ == "__main__":
    app.run(debug=True)