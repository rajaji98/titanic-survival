#backend code using flask
import pickle

# model_path = os.path.join(os.path.dirname(__file__), 'savedmodel.sav')
# model = pickle.load(open(model_path, 'rb'))

from flask import Flask, render_template, request,redirect, url_for

app = Flask(__name__)
#load the modell
model = pickle.load(open('savedmodel.sav', 'rb'))


@app.route('/survived<result>')
def survive(result):
    return "the person survived"

@app.route('/survived<result>')
def died(result):
    return "the person died"


@app.route('/')         # this will create a homepage
def home():
    result = ''
    try:
        return render_template('index.html', result=result)
    except Exception as e:
         print("Render error:", e)
    return str(e)


@app.route('/predict', methods = ['POST','GET'])
def predict(): 
    if request.method == "GET":
        return render_template('index.html')  
    else:
        Pclass = float(request.form['Pclass'])
        Age = float(request.form['Age'])
        Fare = float( request.form['Fare'])
        Sex_male =float( request.form['Sex_male'])
        Name_Miss =float( request.form['Name_Miss'])
        Name_Mr = float(request.form['Name_Mr'])
        Name_Mrs = float(request.form['Name_Mrs'])
        Name_rare = float(request.form['Name_rare'])
        Embarked_Q = float(request.form['Embarked_Q'])
        Embarked_S = float(request.form['Embarked_S'])
        Family_Members = float(request.form['Family_Members'])
        IsAlone = float(request.form['IsAlone'])

        result = model.predict([[Pclass, Age, Fare, Sex_male, Name_Miss, Name_Mr, Name_Mrs,
                              Name_rare, Embarked_Q, Embarked_S,Family_Members, IsAlone]])[0]
        res = ""
        if result == 1:
            res = "survive"
        else:
            res = "died"            

        return redirect(url_for(res,result= result))
 

if __name__ == '__main__':
    app.run(debug= True)

