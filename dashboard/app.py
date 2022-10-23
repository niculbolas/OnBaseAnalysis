import numpy as np
from flask import Flask, request, render_template
import pickle

#initialize Flask and set the template folder to "template"
app = Flask(__name__, template_folder = "template")

#Open model
model = pickle.load(open('model.pkl', 'rb'))

#create our "home" route using the "index.html" page
@app.route('/')
def home():
    return render_template('index.html')

#Set a method to yield predictions
@app.route('/', methods = ['POST'])
def predict():

        #obtain all form values and place them in an array, convert into integers
    int_features = [int(x) for x in request.form.values()]
    #Combine them all into a final numpy array
    final_features = [np.array(int_features)]
    #predict the price given the values inputted by user
    prediction = model.predict(final_features)
    
    #Round the output to 2 decimal places
    output = round(prediction[0], 2)
    
    #If the output is negative, the values entered are unreasonable to the context of the application
    #If the output is greater than 0, return prediction
    if output < 0:
        return render_template('index.html', prediction_text = "Predicted wins are negative, please enter valid statistics in appropriate format.")
    elif output >= 0:
        return render_template('index.html', prediction_text = 'Predicted wins are: {}'.format(output))   

#Run app
if __name__ == "__main__":
    app.run(debug=True)

#References: 
# https://towardsdatascience.com/deploying-machine-learning-models-into-a-website-using-flask-8582b7ce8802
# https://www.analyticsvidhya.com/blog/2020/09/integrating-machine-learning-into-web-applications-with-flask/