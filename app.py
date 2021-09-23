from flask import Flask,render_template,request
from sklearn.linear_model import LinearRegression
import joblib
from sklearn.metrics import accuracy_score



app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html')

@app.route('/prediction')
def prediction():
    return render_template('prediction.html')

@app.route('/prediction1',methods=['POST','GET'])
def prediction1():
    a=[]
    if request.method=="POST":
        high=request.form['high']
        low = request.form['low']
        open = request.form['open']
        day = request.form['day']
        month = request.form['month']
        year = request.form['year']
        a.extend([high,low,open,day,month,year])
        model1=joblib.load('dtmodel.pkl')
        y_pred= model1.predict([a])
        return render_template('prediction.html',msg="a",op=y_pred)
    return render_template('prediction.html')



if __name__ == '__main__':
    app.run(debug=True)
