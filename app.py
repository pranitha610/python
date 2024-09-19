from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return "Flask inside Docker!!"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True,host='0.0.0.0',port=port)




#first install python 
#then python3.pip
#install [pip install flask]
#clone the git repo
# cd----ls---python
#vi requirement.txt
#numpy==1.21.2
pandas==1.3.3
flask==2.0.1
# python3 app.py 
# copy the private ip in the new webb

