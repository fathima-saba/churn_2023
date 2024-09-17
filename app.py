from flask import Flask,render_template,request
import pickle


app=Flask(__name__)



with open('RFC_churn.pkl','rb')as f:
    model = pickle.load(f)

#by default method get
@app.route('/') #it is use to routing path

def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/predict')
def predict():
    return render_template('predict.html')

@app.route('/result',methods=['POST','GET'])
def result():
    Tenure=float(request.form.get('utenure'))
    monthly_charges = float(request.form.get('umonth'))
    total_charges =float(request.form.get('utotal'))
    gender = float(request.form.get('ugender'))
    phone_service= int(request.form.get('uphnservice'))
    internet_service = int(request.form.get('uintservice'))
    device_protection = int(request.form.get('udeviceprotect'))
    contract =int(request.form.get('ucontract'))
    paperless_bill = int(request.form.get('upaperbill'))
    payment = int(request.form.get('upayment'))

    input= [[Tenure,monthly_charges,total_charges,gender,phone_service,internet_service,device_protection,contract,paperless_bill,payment]]
    predict = model.predict(input)
    print(predict)

    if predict == [0]:
        result = "no churn"
    else:
        result = "churn"
    

    return render_template('result.html',res=result)


if __name__ == '__main__':

    app.run(debug=True)


