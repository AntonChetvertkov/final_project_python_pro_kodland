from flask import Flask, render_template, request, redirect
app = Flask(__name__)
@app.route('/', methods=['GET','POST'])
def welcome():
    return render_template('weather_site.html')

@app.route('/register', methods=['GET','POST'])
def form():
    return render_template('form.html')

@app.route('/terms')
def terms():
    return render_template('tandc.html')

if __name__ == "__main__":
    app.run(debug=True)