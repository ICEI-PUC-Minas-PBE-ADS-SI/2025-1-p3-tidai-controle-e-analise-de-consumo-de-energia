# Plano de testes de usabilidade



## Cenários de Teste de Usabilidade

A seguir, são detalhados os cenários de testes de usabilidade para a **Plataforma Interativa para Controle e Análise de Consumo de Energia**, com base nas Histórias de Usuários e Requisitos Funcionais fornecidos.

| **Caso de Teste** | **CT-US-001 – Registrar Consumo de Energia e Visualizar Análise Básica** |
| :------------------------------------------: | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| **Requisito associado** | RF-001 (Cadastrar Consumo), RF-002 (Gerar Análise Comparativa). |
| **Funcionalidades avaliadas** | Cadastro de dados de consumo, clareza dos campos do formulário, feedback pós-cadastro, acesso e compreensão da análise comparativa inicial. |
| **Grupo de usuários** | **Lucas Sanches** (Analista de TI, usuário residencial), e outros usuários residenciais com pouca ou nenhuma familiaridade com análise de consumo. |
| **Objetivo do teste** | Avaliar a facilidade do usuário em registrar seu consumo de energia e em entender a primeira análise comparativa oferecida pela plataforma. |
| **Passos** | - Acessar a plataforma e realizar o login (ou cadastro se for o primeiro acesso). <br> - Navegar até a seção de "Registro de Consumo". <br> - Inserir os dados de consumo (data, valor em kWh, etc.) conforme solicitado. <br> - Submeter o formulário de registro. <br> - Acessar a seção de "Análise de Consumo" para visualizar a comparação com médias regionais. |
| **Critério de êxito** | - O usuário consegue cadastrar o consumo sem hesitação ou erros. <br> - A mensagem de confirmação do cadastro é clara. <br> - A análise comparativa é compreendida sem a necessidade de explicação. <br> - O tempo para completar a tarefa é inferior a 90 segundos. <br> - O usuário avalia a satisfação subjetiva como "Bom" ou "Ótimo". |
| **Ferramentas utilizadas** | Observação direta, cronômetro, gravação de tela (com consentimento), questionário de satisfação pós-tarefa. |
| **Responsável pela elaboração do caso de teste** | Equipe de UX/UI. |

---

| **Caso de Teste** | **CT-US-002 – Explorar Dicas Personalizadas** |
| :------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------: |
| **Requisito associado** | RF-003 (Exibir Dicas Personalizadas). |
| **Funcionalidades avaliadas** | Navegação para a seção de dicas, relevância das dicas apresentadas com base nos dados do usuário, clareza e aplicabilidade do conteúdo das dicas. |
| **Grupo de usuários** | **Lucas Sanches** (Analista de TI, usuário residencial), e outros usuários residenciais buscando formas de economizar. |
| **Objetivo do teste** | Verificar se as dicas de redução de consumo são facilmente encontradas, compreendidas e percebidas como úteis e personalizadas pelo usuário. |
| **Passos** | - Acessar a plataforma. <br> - Navegar até a seção de "Dicas de Economia" (ou similar). <br> - Ler algumas das dicas apresentadas. <br> - Avaliar se as dicas são relevantes para seu perfil de consumo. |
| **Critério de êxito** | - O usuário localiza a seção de dicas intuitivamente. <br> - O usuário afirma que as dicas são relevantes para seu consumo. <br> - O usuário compreende as dicas e sabe como aplicá-las. <br> - O usuário avalia a satisfação subjetiva como "Bom" ou "Ótimo". |
| **Ferramentas utilizadas** | Observação direta, entrevista semi-estruturada pós-tarefa, questionário de relevância das dicas. |
| **Responsável pela elaboração do caso de teste** | Equipe de UX/UI. |

---

| **Caso de Teste** | **CT-US-003 – Utilizar Quiz Interativo para Estimar Consumo** |
| :------------------------------------------: | :---------------------------------------------------------------------------------------------------------------------------------------------------: |
| **Requisito associado** | RF-006 (Quiz interativo para estimar consumo). |
| **Funcionalidades avaliadas** | Localização do quiz, interação com as perguntas (seleção de aparelhos, tempo de uso), exibição e compreensão da estimativa de consumo. |
| **Grupo de usuários** | Usuários residenciais ou empresariais que desejam ter uma ideia rápida do consumo sem necessidade de dados detalhados da conta de luz. |
| **Objetivo do teste** | Avaliar a intuitividade e a utilidade do quiz interativo para estimar o consumo de energia dos aparelhos elétricos. |
| **Passos** | - Acessar a plataforma. <br> - Navegar até a seção de "Estimativa de Consumo" ou "Quiz de Consumo". <br> - Preencher as perguntas do quiz, selecionando aparelhos e tempos de uso. <br> - Visualizar a estimativa de consumo gerada pelo quiz. |
| **Critério de êxito** | - O usuário encontra o quiz sem dificuldade. <br> - O usuário completa o quiz em menos de 120 segundos. <br> - A estimativa de consumo é apresentada de forma clara e é percebida como útil. <br> - O número de erros de preenchimento é zero. |
| **Ferramentas utilizadas** | Observação direta, cronômetro, registro de interações do usuário, questionário de satisfação. |
| **Responsável pela elaboração do caso de teste** | Equipe de UX/UI. |

---

| **Caso de Teste** | **CT-US-004 – Monitorar Consumo da Empresa (Painel)** |
| :------------------------------------------: | :-----------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| **Requisito associado** | RF-005 (Permitir que empresas monitorem o consumo por setor/departamento). |
| **Funcionalidades avaliadas** | Acesso ao painel empresarial, visualização de dados por setor/departamento, identificação de áreas de alto consumo, filtros de visualização. |
| **Grupo de usuários** | **Fabiana Sousa** (Gerente de Pequena Empresa), e outros perfis de gestores ou responsáveis por custos energéticos em empresas. |
| **Objetivo do teste** | Avaliar a usabilidade do painel empresarial para monitoramento detalhado do consumo e identificação de oportunidades de otimização. |
| **Passos** | - Acessar a plataforma com um perfil de empresa. <br> - Navegar até o "Painel Empresarial" ou "Gestão de Consumo". <br> - Visualizar os dados de consumo por diferentes setores/departamentos. <br> - Tentar identificar o setor de maior consumo ou áreas de potencial desperdício. |
| **Critério de êxito** | - O usuário empresarial consegue acessar e navegar pelo painel sem dificuldades. <br> - As informações de consumo por setor são claras e compreensíveis. <br> - O usuário consegue identificar rapidamente os setores de maior consumo. <br> - O usuário avalia a satisfação subjetiva como "Bom" ou "Ótimo". |
| **Ferramentas utilizadas** | Observação direta, entrevista semi-estruturada, registro de tempo na tarefa. |
| **Responsável pela elaboração do caso de teste** | Equipe de UX/UI. |

---

| **Caso de Teste** | **CT-US-005 – Gerar Relatórios Personalizados (Engenheiro)** |
| :------------------------------------------: | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| **Requisito associado** | RF-004 (Acessar gráficos interativos), Histórias de Usuários (Leonardo Rodrigues - Gerar relatórios personalizados). |
| **Funcionalidades avaliadas** | Acesso à ferramenta de relatórios, opções de personalização (período, tipo de dado), geração e exportação do relatório, clareza da apresentação dos dados. |
| **Grupo de usuários** | **Leonardo Rodrigues** (Engenheiro de Sustentabilidade), e outros profissionais que precisam de análises aprofundadas. |
| **Objetivo do teste** | Avaliar a capacidade da plataforma de gerar relatórios detalhados e personalizados de forma eficiente, atendendo às necessidades de análise de um profissional. |
| **Passos** | - Acessar a plataforma com um perfil de usuário que tenha permissão para gerar relatórios avançados. <br> - Navegar até a seção de "Relatórios" ou "Análise Avançada". <br> - Selecionar opções de filtros (período, tipo de visualização, etc.). <br> - Gerar o relatório e analisar a apresentação dos dados. |
| **Critério de êxito** | - O usuário encontra as opções de relatório e personalização facilmente. <br> - O relatório gerado é claro, completo e reflete as opções selecionadas. <br> - O usuário consegue extrair insights relevantes do relatório. <br> - O tempo para gerar um relatório é aceitável (inferior a 60 segundos). |
| **Ferramentas utilizadas** | Observação direta, entrevista pós-teste, análise de resultados gerados. |
| **Responsável pela elaboração do caso de teste** | Equipe de UX/UI. |

---

