from greenvolt import app, db
from flask import render_template, redirect, url_for, flash, request
from greenvolt.forms import CadastroForm, LoginForm
from greenvolt.models import Usuario, Dispositivo, Conta, Noticia
from flask_login import login_user, logout_user, login_required, current_user, LoginManager


@app.route('/')
def page_bem_vindo():
    return render_template("bem-vindo.html")


@app.route('/cadastro', methods=['GET', 'POST'])
def page_cadastro():
    form = CadastroForm()
    if form.validate_on_submit():
        usuario = Usuario(
            nome = form.nome.data,  ## Quero padroninzar para entrar somente com o Email, trocar nome de Usuario para nome completo  
            email = form.email.data,
            senhacrip = form.senha1.data
        )

        db.session.add(usuario)
        db.session.commit()
        return redirect(url_for('page_home'))
    if form.errors != {}:
        for err in form.errors.values():
            flash(f"Erro ao cadastrar usuário {err}") # definir category=danger

    return render_template("cadastro.html", form=form)


@app.route('/login', methods=['GET', 'POST'])
def page_login():
    form = LoginForm()
    if form.validate_on_submit():
        email_usuario_logado = Usuario.query.filter_by(email=form.email.data).first()
        if email_usuario_logado.email and email_usuario_logado.converte_senha(senha_texto_claro=form.senha.data):
            login_user(email_usuario_logado)
            flash(f"Bem-Vindo!") #definir category=sucess
            return redirect(url_for('page_home'))
        else:
            print(f'Usuário ou senha incorretos! Tente novamente.') # definir category=danger
    return render_template("login.html", form=form)


@app.route('/home')
@login_required
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
