from flask import Flask, render_template

app = Flask(__name__)  


@app.route('/')
        
def index():
    return render_template('dashboard/index.html')

@app.route('/About')
def about():
    return render_template('dashboard/about.html')

 






# should be at the end of your python files
if __name__ == '__main__':
    app.run(debug=True)