from greenvolt import app, db
from flask import render_template, redirect, url_for, flash, request
from greenvolt.forms import CadastroForm, LoginForm
from greenvolt.models import Usuario, Dispositivo, Conta, Noticia


@app.route('/')
def page_bem_vindo():
    return render_template("bem-vindo.html")


@app.route('/cadastro', methods=['GET', 'POST'])
def page_cadastro():
    form = CadastroForm()
    if form.validate_on_submit:
        usuario = Usuario(
            nome = form.nome.data,  ## Quero padroninzar para entrar somente com o Email, trocar nome de Usuario para nome completo  
            email = form.email.data,
            senhacrip = form.senha1
        )

        db.session.add(usuario)
        db.session.commit()
        return redirect(url_for('home.html'))
    if form.errors != {}:
        for err in form.errors.values():
            flash(f"Erro ao cadastrar usuário {err}") # definir category=danger

    return render_template("cadastro.html", form=form)


@app.route('/login', methods=['GET', 'POST'])
def page_login():
    return render_template("login.html")


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
