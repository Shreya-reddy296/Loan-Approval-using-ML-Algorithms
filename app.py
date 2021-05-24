from flask import Flask, render_template, request

import pickle
from sklearn.linear_model import LogisticRegression


app=Flask(__name__)

@app.route('/')

def index1():
    return render_template('index1.html')

@app.route('/predict',methods=['POST'])

def predict():
    if request.method=='POST':
        Dependents=request.form['Dependents']
        ApplicantIncome=request.form['ApplicantIncome']
        CoapplicantIncome=request.form['CoapplicantIncome']
        LoanAmount=request.form['LoanAmount']
        Loan_Amount_Term=request.form['Loan_Amount_Term']
        Credit_History=request.form['Credit_History']
        Gender=request.form['Gender']
        Married=request.form['Married']
        Self_Employed=request.form['Self_Employed']
        Education=request.form['Education']
        Property_Area=request.form['Property_Area']
        

        data=[[float(Dependents),float(ApplicantIncome),float(CoapplicantIncome),float(LoanAmount),float(Loan_Amount_Term),float(Credit_History),float(Gender),float(Married),float(Self_Employed),float(Education),float(Property_Area)]]

        lr=pickle.load(open('project.pkl','rb'))
        prediction=lr.predict(data)[0]
        
    return render_template('index1.html',prediction=prediction)



if __name__=='__main__':
    app.run()