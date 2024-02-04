import numpy as np
import pandas as pd 
import joblib 
from flask import render_template , request , Flask


app = Flask(__name__)

model = joblib.load('random_forest_model.pkl')
df = pd.DataFrame()

@app.route('/')
def index():
    return render_template('final.html')


@app.route('/predict',methods=['GET','POST'])
def predict():
    if request.method == 'POST':
        global df
        data = request.form  
        features = []  


        feature_names = ['percentage', 'educational_resources', 'parents_education',
       'personality', 'passion', 'ott_time', 'sm_time', 'travel_time',
       'eduvids_time', 'game_time', 'extra_time', 'ai_usage']

        for feature_name in feature_names:
            feature_value = data.get(feature_name)
            if feature_value is not None:
                if feature_name == 'sub1' and feature_value.isdigit(): 
                    features.append(int(feature_value))
                else:
                    features.append(feature_value)

     
        if len(features) == 12:
            output = model.predict([features])[0].round(2)
            print("Success")
            if output <= 100:
                result_message = f'If You study {data["travel_time"]} hours then You can get {output}% Marks'
            else:
                result_message = f'If You study {data["travel_time"]} hours then You can get 100% Marks'

            df = pd.concat([df, pd.DataFrame({'study_time': data['travel_time'], 'predicted_score': [output]})],
                           ignore_index=True)
            print(df)
            df.to_csv('performance.csv')

            return render_template('final.html', predict=result_message)
        else:
            return render_template('final.html', predict='Mismatch in the number of features')
app.run(debug=True)

