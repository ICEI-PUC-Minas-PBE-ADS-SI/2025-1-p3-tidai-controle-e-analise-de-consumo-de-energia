# Arquitetura da solução

O sistema GreenVolt foi projetado para monitorar o consumo de energia elétrica dos usuários, oferecendo uma experiência personalizada, com dicas de economia, controle de dispositivos e registro de contas de luz.

Como o sistema funciona:
Cadastro e acesso de usuários:
Cada usuário cria uma conta informando nome, e-mail e senha. Com isso, tem acesso ao sistema e pode cadastrar seus dispositivos.

Cadastro de dispositivos:
O usuário informa quais aparelhos elétricos possui, junto com a potência (em watts) e a média diária de uso. O sistema usa essas informações para estimar o consumo de energia de cada dispositivo.

Monitoramento do consumo:
Com base nos dados fornecidos, o sistema calcula o consumo diário (em kWh) e armazena esse histórico. Assim, o usuário pode visualizar como cada aparelho impacta na conta de energia.

Controle da conta de luz:
Mensalmente, o usuário pode registrar o valor da fatura, o total consumido e a data de vencimento. Isso ajuda a comparar o consumo estimado com o consumo real.

Favoritos de notícias:
O sistema fornece dicas e notícias sobre economia de energia. Caso o usuário ache interessante, pode salvar essas notícias em uma lista de favoritas para consultar depois.

Relacionamento entre os dados:

-Cada usuário pode cadastrar vários dispositivos, contas de luz e notícias favoritas.

-Cada dispositivo tem um histórico de consumo próprio.

Todos os dados são vinculados diretamente ao usuário, garantindo segurança e personalização.

## Diagrama de classes

![Diagrama de Classes](https://github.com/user-attachments/assets/34b925d0-5dec-4f57-ba98-b77390188110)


##  Modelo de dados

O desenvolvimento da solução proposta requer a existência de bases de dados que permitam realizar o cadastro de dados e os controles associados aos processos identificados, assim como suas recuperações.

Utilizando a notação do DER (Diagrama Entidade-Relacionamento), elabore um modelo, usando alguma ferramenta, que contemple todas as entidades e atributos associados às atividades dos processos identificados. Deve ser gerado um único DER que suporte todos os processos escolhidos, visando, assim, uma base de dados integrada. O modelo deve contemplar também o controle de acesso dos usuários (partes interessadas nos processos) de acordo com os papéis definidos nos modelos do processo de negócio.

Apresente o modelo de dados por meio de um modelo relacional que contemple todos os conceitos e atributos apresentados na modelagem dos processos.

### Modelo ER

O Modelo ER representa, por meio de um diagrama, como as entidades (coisas, objetos) se relacionam entre si na aplicação interativa.

> **Links úteis**:
> - [Como fazer um diagrama entidade relacionamento](https://www.lucidchart.com/pages/pt/como-fazer-um-diagrama-entidade-relacionamento)

### Esquema relacional

![Esquema relacional](https://github.com/user-attachments/assets/7f3e6838-0e09-481f-9875-748f17ac59a6)

---

> **Links úteis**:
> - [Criando um modelo relacional - documentação da IBM](https://www.ibm.com/docs/pt-br/cognos-analytics/12.0.0?topic=designer-creating-relational-model)

### Modelo físico

Insira aqui o script de criação das tabelas do banco de dados.

Veja um exemplo:

```sql
-- Tabela de usuários do sistema
CREATE TABLE usuarios (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    senha_hash VARCHAR(255) NOT NULL
);

-- Tabela de dispositivos registrados pelos usuários
CREATE TABLE dispositivos (
    id SERIAL PRIMARY KEY,
    usuario_id INT NOT NULL,
    nome VARCHAR(100) NOT NULL,
    potencia_watts FLOAT NOT NULL,
    horas_uso_diario FLOAT NOT NULL,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE
);

-- Tabela de registros de consumo dos dispositivos
CREATE TABLE consumo (
    id SERIAL PRIMARY KEY,
    dispositivo_id INT NOT NULL,
    data_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    consumo_kwh FLOAT NOT NULL,
    FOREIGN KEY (dispositivo_id) REFERENCES dispositivos(id) ON DELETE CASCADE
);

-- Tabela de notícias salvas como favoritas pelos usuários
CREATE TABLE noticias_favoritas (
    id SERIAL PRIMARY KEY,
    usuario_id INT NOT NULL,
    titulo VARCHAR(255) NOT NULL,
    url VARCHAR(255) NOT NULL,
    data_salva TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE
);

-- Tabela de contas de luz cadastradas pelos usuários
CREATE TABLE conta_de_luz (
    id SERIAL PRIMARY KEY,
    usuario_id INT NOT NULL,
    mes_referencia VARCHAR(7) NOT NULL,  -- Exemplo: "03/2025"
    valor_total DECIMAL(10,2) NOT NULL,
    consumo_total_kwh FLOAT NOT NULL,
    data_vencimento DATE NOT NULL,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE
);

```
Esse script deverá ser incluído em um arquivo .sql na pasta [de scripts SQL](../src/db).


## Tecnologias

Descreva qual(is) tecnologias você vai usar para resolver o seu problema, ou seja, implementar a sua solução. Liste todas as tecnologias envolvidas, linguagens a serem utilizadas, serviços web, frameworks, bibliotecas, IDEs de desenvolvimento, e ferramentas.

Apresente também uma figura explicando como as tecnologias estão relacionadas ou como uma interação do usuário com o sistema vai ser conduzida, por onde ela passa até retornar uma resposta ao usuário.


| **Dimensão**   | **Tecnologia**  |
| ---            | ---             |
| Front-end      | HTML + CSS + JS + Bootstrap |
| Back-end       | Python          |
| SGBD           | Postgres           |
| Deploy         | Render          |


## Hospedagem

Explique como a hospedagem e o lançamento da plataforma foram realizados.

> **Links úteis**:
> - [Website com GitHub Pages](https://pages.github.com/)
> - [Programação colaborativa com Repl.it](https://repl.it/)
> - [Getting started with Heroku](https://devcenter.heroku.com/start)
> - [Publicando seu site no Heroku](http://pythonclub.com.br/publicando-seu-hello-world-no-heroku.html)

## Qualidade de software

Conceituar qualidade é uma tarefa complexa, mas ela pode ser vista como um método gerencial que, por meio de procedimentos disseminados por toda a organização, busca garantir um produto final que satisfaça às expectativas dos stakeholders.

No contexto do desenvolvimento de software, qualidade pode ser entendida como um conjunto de características a serem atendidas, de modo que o produto de software atenda às necessidades de seus usuários. Entretanto, esse nível de satisfação nem sempre é alcançado de forma espontânea, devendo ser continuamente construído. Assim, a qualidade do produto depende fortemente do seu respectivo processo de desenvolvimento.

A norma internacional ISO/IEC 25010, que é uma atualização da ISO/IEC 9126, define oito características e 30 subcaracterísticas de qualidade para produtos de software. Com base nessas características e nas respectivas subcaracterísticas, identifique as subcaracterísticas que sua equipe utilizará como base para nortear o desenvolvimento do projeto de software, considerando alguns aspectos simples de qualidade. Justifique as subcaracterísticas escolhidas pelo time e elenque as métricas que permitirão à equipe avaliar os objetos de interesse.

> **Links úteis**:
> - [ISO/IEC 25010:2011 - Systems and Software Engineering — Systems and Software Quality Requirements and Evaluation (SQuaRE) — System and Software Quality Models](https://www.iso.org/standard/35733.html/)
> - [Análise sobre a ISO 9126 – NBR 13596](https://www.tiespecialistas.com.br/analise-sobre-iso-9126-nbr-13596/)
> - [Qualidade de software - Engenharia de Software](https://www.devmedia.com.br/qualidade-de-software-engenharia-de-software-29/18209)
