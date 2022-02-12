from flask import Flask, request, render_template
import joblib
import sklearn
import pandas as pd
import numpy as np

app = Flask(__name__)

model = joblib.load('Sales_Prediction.pkl')


@app.route('/')
def home():
    return render_template("home.html")


@app.route("/predict", methods=["POST"])
def predict():
    holiday = request.form["holiday"]
    discount = request.form["discount"]
    
    order = request.form["order"]

    date = request.form["date"]
    day = float(pd.to_datetime(date, format="%Y-%m-%dT%H:%M").day)
    month = float(pd.to_datetime(date, format="%Y-%m-%dT%H:%M").month)

    
    Store_Type = request.form["Store_Type"]
    if Store_Type == "Store_Type_S2":
        Store_Type_S1 = 0
        Store_Type_S2 = 1
        Store_Type_S3 = 0
        Store_Type_S4 = 0

    elif Store_Type == "Store_Type_S3":
        Store_Type_S1 = 0
        Store_Type_S2 = 0
        Store_Type_S3 = 1
        Store_Type_S4 = 0

    elif Store_Type == "Store_Type_S4":
        Store_Type_S1 = 0
        Store_Type_S2 = 0
        Store_Type_S3 = 0
        Store_Type_S4 = 1

    else:
        Store_Type_S1 = 1
        Store_Type_S2 = 0
        Store_Type_S3 = 0
        Store_Type_S4 = 0
    

    Location_Type = request.form["Location_Type"]
    if Location_Type == "Location_Type_L2":
        Location_Type_L1 = 0
        Location_Type_L2 = 1
        Location_Type_L3 = 0
        Location_Type_L4 = 0
        Location_Type_L5 = 0

    elif Location_Type == "Location_Type_L3":
        Location_Type_L1 = 0
        Location_Type_L2 = 0
        Location_Type_L3 = 1
        Location_Type_L4 = 0
        Location_Type_L5 = 0

    elif Location_Type == "Location_Type_L4":
        Location_Type_L1 = 0
        Location_Type_L2 = 0
        Location_Type_L3 = 0
        Location_Type_L4 = 1
        Location_Type_L5 = 0

    elif Location_Type == "Location_Type_L5":
        Location_Type_L1 = 0
        Location_Type_L2 = 0
        Location_Type_L3 = 0
        Location_Type_L4 = 0
        Location_Type_L5 = 1

    else:
        Location_Type_L1 = 1
        Location_Type_L2 = 0
        Location_Type_L3 = 0
        Location_Type_L4 = 0
        Location_Type_L5 = 0
    
    Region_Code = request.form["Region_Code"]
    if Region_Code == "Region_Code_R2":
        Region_Code_R1 = 0
        Region_Code_R2 = 1
        Region_Code_R3 = 0
        Region_Code_R4 = 0

    elif Region_Code == "Region_Code_R3":
        Region_Code_R1 = 0
        Region_Code_R2 = 0
        Region_Code_R3 = 1
        Region_Code_R4 = 0

    elif Region_Code == "Region_Code_R4":
        Region_Code_R1 = 0
        Region_Code_R2 = 0
        Region_Code_R3 = 0
        Region_Code_R4 = 1

    else:
        Region_Code_R1 = 1
        Region_Code_R2 = 0
        Region_Code_R3 = 0
        Region_Code_R4 = 0
        


    arr = np.array([[float(holiday), float(discount), float(order), month, day,
                     float(Store_Type_S2), float(Store_Type_S3), float(Store_Type_S4),
                     float(Location_Type_L2),float(Location_Type_L3), float(Location_Type_L4), float(Location_Type_L5),
                     float(Region_Code_R2), float(Region_Code_R3), float(Region_Code_R4)]])

    pred = model.predict(arr)

    return render_template('home.html', prediction_text='SALES WILL BE OF Rs: {}'.format(int(pred[0])))


if __name__ == "__main__":
    app.run(debug=True)
