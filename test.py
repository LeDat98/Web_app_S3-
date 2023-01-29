from flask import Flask, render_template, request, send_file, send_from_directory


app = Flask(__name__)

@app.route('/')
def home():
    # return '<button onclick="window.location.href=\'/text_to_image\'">Go to image</button>'
    return render_template('index2.html')
if __name__ == '__main__':
    app.run()