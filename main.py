from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

df = pd.read_csv("dictonary.csv")

@app.route('/')
def home():
    return render_template("home.html")


@app.route('/api/v1/<word>/')
def api(word):
    definition = df.loc[df["word"] == word]['defination'].squeeze()
    result_dictionary = {'word': word, 'defination' : definition}
    return result_dictionary


if __name__ == "__main__":
    app.run(debug=True, port=5001)