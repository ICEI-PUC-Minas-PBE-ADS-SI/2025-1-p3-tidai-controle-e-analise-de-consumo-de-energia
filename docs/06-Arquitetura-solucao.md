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

### Esquema relacional

![Esquema relacional](https://github.com/user-attachments/assets/7f3e6838-0e09-481f-9875-748f17ac59a6)

---

### Modelo físico

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

A hospedagem e o lançamento da plataforma GreenVolt foram realizados utilizando a plataforma Render, que oferece serviços gratuitos e pagos para aplicações web em Node.js, Python, static sites, entre outros.

🔧 Processo de Hospedagem:
Preparação do projeto:

O código da aplicação foi armazenado em um repositório no GitHub.

Garantimos que o projeto estivesse configurado com scripts de inicialização (start) no package.json, facilitando o deploy automático.

Integração com o GitHub:

Conectamos o repositório do GitHub à conta da Render.

A cada novo push na branch principal, a plataforma realiza automaticamente o build e o deploy da aplicação.

Configuração do ambiente:

Escolhemos a opção de Web Service no Render.

Definimos a porta padrão e as variáveis de ambiente (caso necessário).

A aplicação foi exposta por um domínio padrão .onrender.com.

Resultado final:

O sistema ficou disponível online para testes e uso em tempo real.

A URL gerada permite que usuários testem funcionalidades como cadastro de dispositivos, visualização de consumo e leitura de notícias.


## Qualidade de software

📋 Características e Subcaracterísticas Selecionadas (ISO/IEC 25010)
Com base na norma ISO/IEC 25010, selecionamos as seguintes subcaracterísticas como foco principal do projeto GreenVolt:

1. Usabilidade
Subcaracterísticas:

Apreensibilidade: O usuário entende rapidamente como utilizar o sistema.

Operacionalidade: O sistema é fácil de operar e interagir.

Justificativa: Como o sistema é voltado a usuários comuns, muitos sem conhecimentos técnicos, a interface precisa ser clara, simples e intuitiva.

Métricas:

Tempo médio para completar tarefas básicas (ex: cadastrar dispositivo).

Percentual de erros cometidos durante testes de usabilidade.

Satisfação medida por questionário pós-uso (ex: escala Likert).

2. Desempenho e Eficiência
Subcaracterística:

Tempo de resposta: Velocidade com que o sistema responde às interações.

Justificativa: A experiência do usuário depende da fluidez ao interagir com o site — páginas e cálculos precisam carregar rapidamente.

Métricas:

Tempo médio de carregamento das páginas (< 2 segundos).

Testes com Lighthouse (Google) e WebPageTest.

3. Segurança
Subcaracterísticas:

Confidencialidade: Proteção de dados pessoais (nome, e-mail, senha).

Autenticidade: Verificação segura do acesso do usuário.

Justificativa: O sistema armazena informações sensíveis, sendo essencial garantir que os dados estejam protegidos e que somente usuários autorizados acessem suas contas.

Métricas:

Uso de hash de senha (ex: SHA-256).

Testes de login e logout, além de verificação de falhas de segurança básicas.

4. Portabilidade
Subcaracterística:

Adaptabilidade: O sistema se adapta bem a diferentes dispositivos e tamanhos de tela.

Justificativa: Muitos usuários acessam via smartphones, então é essencial que o sistema funcione bem em mobile.

Métricas:

Testes em diferentes navegadores e resoluções.

Avaliação via Google Mobile-Friendly Test.

5. Manutenibilidade
Subcaracterística:

Modificabilidade: Facilidade para realizar alterações ou correções no código.

Justificativa: O projeto pode evoluir no futuro com novas funcionalidades ou ajustes. Um código limpo e modular ajuda muito nesse processo.

Métricas:

Organização e clareza do repositório (ex: estrutura de pastas, nome de arquivos).

Análise de complexidade ciclomática (ex: com SonarQube ou VS Code extensions).

📌 Conclusão
A qualidade do sistema GreenVolt foi planejada desde o início com base em critérios reais de usabilidade, segurança e desempenho. A equipe utilizou a norma ISO/IEC 25010 como guia para priorizar subcaracterísticas compatíveis com os objetivos do projeto e com o perfil dos usuários.
