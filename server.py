from flask import Flask, render_template, request, redirect, session
import datetime

app = Flask(__name__)  
app.secret_key='password'

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    session['now'] = datetime.datetime.now()
    #print('Charging' + {{request.form['first_name']}} + {{request.form['last_name']}} + 'for' + {{request.form['strawberry']|int + request.form['raspberry']|int + request.form['apple']|int}} + 'fruits')
    return render_template("checkout.html")

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True, port=5001)    