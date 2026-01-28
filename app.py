from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    target_date = "Jan 30, 2026 09:00:00"
    return render_template('index.html', target_date=target_date)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)