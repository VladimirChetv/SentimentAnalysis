from sentiment_classifier import SentimentClassifier
from codecs import open
import time
from flask import Flask, render_template, request, url_for

app = Flask(__name__)

print("Подготовка классификатора")
start_time = time.time()
classifier = SentimentClassifier()
print("Классификатор готов")
print(time.time() - start_time, "seconds")

@app.route('/')
def home_page():
    return render_template('home.html')

@app.route('/review', methods=["POST", "GET"])
def review(text='', prediction_message=''):
    if request.method == 'POST':
        text = request.form['text']
        prediction_message = classifier.get_prediction_message(text)
    return render_template('review.html', text=text, prediction_message=prediction_message)


@app.errorhandler(404)
def not_found(e):
    return render_template('404.html')


if __name__ == '__main__':
    app.run(debug=False)
