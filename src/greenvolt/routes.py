from greenvolt import app
from flask import render_template
from greenvolt.forms import CadastroForm, LoginForm


@app.route('/')
def page_bem_vindo():
    return render_template("bem-vindo.html")


@app.route('/login')
def page_login():
    return render_template("login.html") ## discutir com o grupo se o login e cadastro vai ficar na mesma pagina ou vai ser diferente


@app.route('/home')
def page_home():
    return render_template("home.html")

@app.route('/simulador-de-gastos')
def page_simulador_de_gastos():
    return render_template("simulador-de-gastos.html")


@app.route('/dicas')
def page_dicas():
    return render_template("dicas.html")


@app.route('/sobre')
def page_sobre():
    return render_template("sobre.html")


@app.route('/funcionalidades')
def page_funcionalidades():
    return render_template("funcionalidades.html")


@app.route('/perfil')
def page_perfil():
    return render_template("perfil.html")
