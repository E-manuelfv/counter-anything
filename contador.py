from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    # O alvo é 28/01/2026 às 08:00:00
    target_date = "Jan 28, 2026 08:00:00"
    return render_template('index.html', target_date=target_date)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)