from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.get('/')
def index():
    return render_template('index.html')
    
    
@app.get('/teste')

def teste():
    return render_template('m.html')
    

if __name__ == '__main__':
    app.run(debug=True)