from flask import Flask, render_template
# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(port = 80, debug = True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
