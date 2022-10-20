from flask import Flask, render_template, request
from forms import MyForm
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = "lolailo"

@app.route('/')
def index():
    return 'en marcha'

@app.route('/new', methods=["GET", "POST"])
def alta():
    form = MyForm()
    if request.method == "GET":
        return render_template("new.html", form = form)
    else:
        if 'calcular'  in  request.form:
            to_Q = form.from_Q.data * random.random()

            form.hidden_from.data = form.from_Q.data
            form.hidden_to.data = to_Q
            return render_template("new.html", form = form)
        elif 'comprar' in request.form:
            if form.validate():
                return "hago la compra"
            else:
                return render_template("new_html", form= form)

        print("por aquí pasa")
        return("Aquí debería hacer algo")        