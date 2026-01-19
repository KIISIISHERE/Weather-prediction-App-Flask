from flask import Flask,render_template,request
import requests
#create a flask app
app=Flask(__name__)
#API Key
API_KEY="f9da638613c4607d4d28c8b209ba9b10"
@app.route('/', methods=['GET','POST'])
def home():
    result=""
    if request.method=='POST':
        #Get the city name from the form
        city=request.form['city']
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        #response
        response=requests.get(url).json()
        #print the response
        result=response
    return render_template('index.html',result=result)
#run the app
if __name__=='__main__':
    app.run(debug=True)
