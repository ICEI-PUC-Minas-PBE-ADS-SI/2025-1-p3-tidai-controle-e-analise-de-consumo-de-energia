from greenvolt import app, db
from flask import render_template, redirect, url_for, flash, request
from greenvolt.forms import CadastroForm, LoginForm, AdicionarContaForm, RemoverContaForm
from greenvolt.models import Usuario, Dispositivo, Conta, Noticia
from flask_login import login_user, logout_user, login_required, current_user, LoginManager
from datetime import datetime
from decimal import Decimal, InvalidOperation
import plotly.graph_objs as go
import plotly.io as pio 
import plotly
import json

@app.route('/')
def page_bem_vindo():
    if current_user.is_authenticated:
        return redirect(url_for('page_home'))
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
            flash(f"Erro ao cadastrar usuário {err}", category="danger") # definir category=danger

    return render_template("cadastro.html", form=form)


@app.route('/login', methods=['GET', 'POST'])
def page_login():
    form = LoginForm()
    if form.validate_on_submit():
        email_usuario_logado = Usuario.query.filter_by(email=form.email.data).first()
        if email_usuario_logado.email and email_usuario_logado.converte_senha(senha_texto_claro=form.senha.data):
            login_user(email_usuario_logado)
            flash(f"Bem-Vindo!", category="success") #definir category=sucess
            return redirect(url_for('page_home'))
        else:
            flash(f'Usuário ou senha incorretos! Tente novamente.', category="danger") 
    return render_template("login.html", form=form)


@app.route('/logout')
def page_logout():
    logout_user()
    flash("Você saiu com sucesso!", category="success")
    return redirect(url_for('page_bem_vindo'))



@app.route('/home', methods=['GET', 'POST'])
@login_required
def page_home():
    adicionar_form = AdicionarContaForm()
    remover_form = RemoverContaForm()

    contas = Conta.query.filter_by(usuario_id=current_user.id).all()

    meses = [conta.data_ref for conta in contas]
    valores = [conta.valor for conta in contas]

    fig = go.Figure()
    fig.add_trace(go.Bar(x=meses, y=valores, name='Gráfico de Gasto',marker=dict(color='green')))

    fig.update_layout(title='Consumo Mensal de Energia',
                      xaxis_title='Mês',
                      yaxis_title='Valor (R$)',
                      template='simple_white',
                      bargap=0.9,
                      )
    
    graph_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    # Verifica se o form de adicionar foi enviado e é válido
    if adicionar_form.validate_on_submit():
        try:
            nova_conta = Conta(
                data_ref=adicionar_form.data.data,
                valor=adicionar_form.valor.data,
                consumo_kwh=adicionar_form.consumo_kwh.data,
                usuario_id=current_user.id
            )
            db.session.add(nova_conta)
            db.session.commit()
            flash("Conta adicionada com sucesso!", category="success")
            return redirect(url_for('page_home'))  # Evita reenvio ao atualizar
        except Exception as e:
            db.session.rollback()
            flash(f"Ocorreu um erro ao adicionar a conta: {str(e)}", category="danger")

    # Verifica se o form de remover foi enviado e é válido
    if request.method == 'POST' and 'remover_conta' in request.form:
        data_ref_str = request.form.get('data_ref')
        
        if not data_ref_str:
            flash("Data de referência não recebida", "danger")
            return redirect(url_for('page_home'))

        try:
            # Converter string para date
            data_ref = datetime.strptime(data_ref_str, '%Y-%m-%d').date()
            
            # Buscar conta no banco
            conta = Conta.query.filter_by(
                usuario_id=current_user.id,
                data_ref=data_ref
            ).first()

            if conta:
                # Remover conta
                db.session.delete(conta)
                db.session.commit()
                flash("Conta removida com sucesso!", "success")
            else:
                flash("Conta não encontrada para esta data", "warning")
                
        except ValueError as e:
            flash(f"Formato de data inválido: {str(e)}", "danger")
        except Exception as e:
            db.session.rollback()
            flash(f"Erro ao remover conta: {str(e)}", "danger")
        
        return redirect(url_for('page_home'))

    return render_template(
        "home.html",
        adicionar_form=adicionar_form,
        remover_form=remover_form,
        contas=contas,
        graphJSON=graph_json
    )

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
