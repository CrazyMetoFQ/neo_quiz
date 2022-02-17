from flask import Flask, render_template, url_for
from flask import redirect, request

from flask_wtf import FlaskForm
from wtforms.fields import RadioField, SubmitField, StringField, BooleanField

from pprint import pprint

from main_quiz import rand_q as rnq

# base_path = "C:/Users/Ali Hussain/flaskwtf_tri"

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'



# Initialize our ngrok settings into Flask
app.config.from_mapping(
BASE_URL="http://localhost:5000",
USE_NGROK=True
)


from pyngrok import ngrok
port = 5000
ngrok.set_auth_token("24k83aoHO3om9fz4iWAhPgQBymf_6ri1xmk9vXw8cWp3kbVzh")
public_url = ngrok.connect(port, bind_tls=True) # .public_url

print(public_url.public_url)

# print(help(RadioField))
class MainForm(FlaskForm):
        
    # super(bsf, self).__init__(**kw)
    
    submit = SubmitField("SUMBIT")


class DummyForm(MainForm):

    for _sn,_q in enumerate(rnq(1)):
        vars()[f'q{_sn}'] = RadioField(_q.q, choices= _q.opts )
        vars()[f"raw_q{_sn}"] = _q

    upfrm = BooleanField("Update Form")


def seteer(cls, n=3):

    for _sn,_q in enumerate(rnq(n)):
        
        setattr(cls, f'q{_sn}', RadioField(_q.q, choices= _q.opts ))
        setattr(cls, f"raw_q{_sn}", _q)

def geteer(cls,x):

    return [getattr(cls,i)  for i in dir(cls) if i.startswith(x)]


def b2c(x, y=True):
    
    if y==None:
        return "Not Answered"
    elif x == True:
        return "Correct"
    elif x == False:
        return "Wrong"
    else:
        return f"INVALID {x}"
        

@app.route('/', methods=["GET", "POST"])
def quiz():

    # seteer(DummyForm,2)
    form = DummyForm()

    # return str([i for i in dir(form) if not i.startswith("_")])

    atz = geteer(form,"q")
    rql = geteer(form,"raw_")
    sns = range(1,len(rql)+1)

    # return str(list(zip([i.label for i in atz],[i.q for i in rql])))

    if form.validate_on_submit():
        pass
    else:
        pass
    

    return render_template("qz.html",
                            aform = form,
                            zzz=zip(sns,atz,rql),
                            b2c = b2c)


@app.route('/updateform', methods=["get",'post'])
def updateform():
    
    seteer(DummyForm,1)
    atz = geteer(DummyForm,"q")
    rql = geteer(DummyForm,"raw_")
    sns = range(1,len(rql)+1)

    for q in atz:
        q.data=None

    return redirect("/")





if __name__ == '__main__':
    app.run(debug=False)