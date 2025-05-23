# Plano de testes de software

<span style="color:red">Pré-requisitos: <a href="02-Especificacao.md">Especificação do Projeto</a></span>, <a href="04-Projeto-interface.md">Projeto de Interface</a>


|               **Caso de teste**              |                                                                                        **CT-001 – Cadastrar Consumo de Energia**                                                                                       |
| :------------------------------------------: | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
|              Requisito associado             |                                                                     RF-001 - O sistema deve permitir que usuários cadastrem seu consumo de energia.                                                                    |
|               Objetivo do teste              |                                                                      Verificar se o usuário consegue registrar corretamente o consumo de energia.                                                                      |
|                    Passos                    | - Acessar o navegador <br> - Informar o endereço do sistema <br> - Fazer login (se necessário) <br> - Acessar a aba “Cadastro de Consumo” <br> - Preencher os campos com data e valor em kWh <br> - Clicar em “Salvar” |
|               Critério de êxito              |                                                                         - O sistema exibe o consumo salvo na listagem de registros do usuário.                                                                         |
| Responsável pela elaboração do caso de teste |                                                                                                          Gabriel                                                                                                         |


<br>

|               **Caso de teste**              |                                                   **CT-002 – Gerar Análise Comparativa**                                                   |
| :------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------: |
|              Requisito associado             |                      RF-002 - O sistema deve gerar uma análise do consumo energético com comparações médias regionais.                     |
|               Objetivo do teste              |                                Verificar se a análise é exibida corretamente com base nos dados cadastrados.                               |
|                    Passos                    | - Acessar o navegador <br> - Realizar login <br> - Acessar a seção “Análise de Consumo” <br> - Visualizar gráficos e comparações regionais |
|               Critério de êxito              |                                    - Os dados são exibidos corretamente com média comparativa regional.                                    |
| Responsável pela elaboração do caso de teste |                                                                    Luis, Matheus                                                                   |


<br>

|               **Caso de teste**              |                                                        **CT-003 – Exibir Dicas Personalizadas**                                                       |
| :------------------------------------------: | :---------------------------------------------------------------------------------------------------------------------------------------------------: |
|              Requisito associado             |                      RF-003 - Deve exibir dicas personalizadas para redução do consumo com base nos dados inseridos pelo usuário.                     |
|               Objetivo do teste              |                                  Verificar se as dicas apresentadas são coerentes com os dados de consumo do usuário.                                 |
|                    Passos                    | - Acessar o navegador <br> - Realizar login <br> - Acessar a seção “Dicas” <br> - Conferir se as dicas são relevantes ao padrão de consumo cadastrado |
|               Critério de êxito              |                                               - As dicas mudam conforme o padrão de consumo do usuário.                                               |
| Responsável pela elaboração do caso de teste |                                                                         Felipe, Gabriel                                                                         |


<br>

|               **Caso de teste**              |                                                             **CT-004 – Visualizar Gráficos Interativos**                                                            |
| :------------------------------------------: | :-----------------------------------------------------------------------------------------------------------------------------------------------------------------: |
|              Requisito associado             |                         RF-004 - O usuário poderá acessar gráficos interativos mostrando a evolução do consumo de energia ao longo do tempo.                        |
|               Objetivo do teste              |                                   Verificar se os gráficos estão sendo renderizados corretamente e atualizados conforme os dados.                                   |
|                    Passos                    | - Acessar o navegador <br> - Realizar login <br> - Acessar a seção “Gráficos” <br> - Visualizar evolução do consumo por mês <br> - Interagir com filtros de período |
|               Critério de êxito              |                                                - Os gráficos funcionam corretamente e refletem os dados cadastrados.                                                |
| Responsável pela elaboração do caso de teste |                                                                                Luis                                                                                |

<br>

|               **Caso de teste**              |                                                       **CT-005 – Estimar Consumo com Quiz**                                                       |
| :------------------------------------------: | :-----------------------------------------------------------------------------------------------------------------------------------------------: |
|              Requisito associado             |                    RF-006 - O site deve contar com um quiz interativo para estimar o consumo de aparelhos elétricos do usuário.                   |
|               Objetivo do teste              |                           Verificar se o quiz calcula corretamente o consumo estimado com base nas respostas do usuário.                          |
|                    Passos                    | - Acessar o navegador <br> - Entrar na aba “Quiz” <br> - Selecionar os aparelhos usados e tempo de uso diário <br> - Clicar em “Calcular Consumo” |
|               Critério de êxito              |                                 - O consumo estimado é apresentado com base nos aparelhos e horários selecionados.                                |
| Responsável pela elaboração do caso de teste |                                                                       Matheus, Gabriel                                                                       |





