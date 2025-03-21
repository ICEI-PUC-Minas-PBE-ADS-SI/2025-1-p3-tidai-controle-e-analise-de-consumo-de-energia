# Especificação do projeto

<span style="color:red">Pré-requisitos: <a href="01-Contexto.md"> Documentação de contexto</a></span>

 Este documento define o problema e a ideia de solução a partir da perspectiva do usuário. O projeto visa desenvolver um site interativo para análise e controle de consumo de energia, permitindo que usuários residenciais e empresas visualizem, compreendam e otimizem seus gastos energéticos de forma intuitiva.

 O sistema oferecerá ferramentas didáticas, como um guia visual de consumo, análise interativa de contas de energia e testes personalizados para estimar o gasto energético.

A especificação do projeto incluirá os seguintes elementos:

- Personas: Perfis representativos dos usuários, detalhando suas características e necessidades específicas em relação ao consumo de energia.
- Histórias de usuários: Situações práticas em que os usuários interagem com o sistema, demonstrando seus objetivos e desafios.
- Requisitos funcionais e não funcionais: Definição das funcionalidades essenciais do sistema e das características técnicas para garantir desempenho, segurança e usabilidade.
- Restrições: Limitações do projeto, como prazos, orçamento e tecnologias utilizadas.
- Diagrama de casos de uso: Representação gráfica das interações dos usuários com o sistema.

Para a especificação do projeto, utilizaremos técnicas como brainstorming para levantamento de ideias e priorização de requisitos para definir o que é essencial.

A seguir, apresentamos a análise detalhada do público-alvo e dos requisitos do sistema.
## Personas

### 1. Lucas Sanches
- Usuário Residencial
- Idade: 35 anos
- Profissão: Analista de TI (home office)
- Rotina: Trabalha em casa e usa vários equipamentos eletrônicos diariamente.
- Dores:
  - Não sabe quais aparelhos mais consomem energia.
  - Acha as contas de luz confusas e difíceis de entender.
- Necessidades:
  - Ter uma forma simples de visualizar seu consumo.
  - Receber dicas práticas para reduzir o gasto energético.
### 2. Fabiana Sousa 
- Gerente de Pequena Empresa
- Idade: 42 anos
- Profissão: Proprietária de uma cafeteria
- Rotina: Lida com equipamentos como máquinas de café, geladeiras e fornos elétricos.
- Dores:
  - Gasto elevado com energia impacta o faturamento.
  - Dificuldade em identificar desperdícios.
- Necessidades:
  - Monitorar o consumo da loja de forma clara.
  - Ter sugestões para otimizar os gastos.
### 3. Leonardo Rodrigues
- Engenheiro de Sustentabilidade
- Idade: 28 anos
- Profissão: Engenheiro ambiental em uma grande empresa
- Rotina: Trabalha com análise de consumo energético industrial.
- Dores:
  - Falta de ferramentas intuitivas para gerar relatórios.
  - Dificuldade em convencer gestores sobre mudanças no consumo.
- Necessidades:
  - Gerar relatórios detalhados e personalizados.
  - Comparar consumo da empresa com padrões de mercado.

## Histórias de usuários

Com base na análise das personas, foram identificadas as seguintes histórias de usuários:

|EU COMO...          | QUERO/PRECISO ...                               |PARA ...                                  |
|--------------------|-------------------------------------------------|------------------------------------------|
|Lucas               | Visualizar os aparelhos que mais gastam energia | Conseguir reduzir minha conta de luz     |
|Fabiana             | Monitorar o consumo da minha empresa            | Identificar desperdícios e cortar custos |
|Leonardo            | Gerar relatórios personalizados                 | Apresentar insights para a diretoria     |


Apresente aqui as histórias de usuários que são relevantes para o projeto da sua solução. As histórias de usuários consistem em uma ferramenta poderosa para a compreensão e elicitação dos requisitos funcionais e não funcionais da sua aplicação. Se possível, agrupe as histórias de usuários por contexto, para facilitar consultas recorrentes a esta parte do documento.

## Requisitos

As tabelas a seguir apresentam os requisitos funcionais e não funcionais que detalham o escopo do projeto. Para determinar a prioridade dos requisitos, aplique uma técnica de priorização e detalhe como essa técnica foi aplicada.

### Requisitos funcionais

|ID    | Descrição do Requisito  | Prioridade |
|------|-----------------------------------------|----|
|RF-001| O sistema deve permitir que usuários cadastrem seu consumo de energia | ALTA | 
|RF-002| O sistema deve gerar uma análise do consumo energético com comparações médias regionais.   | ALTA |
|RF-003| Deve exibir dicas personalizadas para redução do consumo com base nos dados inseridos pelo usuário. | ALTA | 
|RF-004| O usuário poderá acessar gráficos interativos mostrando a evolução do consumo de energia ao longo do tempo.| MÉDIA |
|RF-005| Deve permitir que empresas monitorem o consumo energético por setor/departamento.	 | MÉDIA | 
|RF-006| O site deve contar com um quiz interativo para estimar o consumo de aparelhos elétricos do usuário. | MÉDIA |

### Requisitos não funcionais

|ID     | Descrição do Requisito  |Prioridade |
|-------|-------------------------|----|
|RNF-001| O sistema deve ser responsivo e funcionar corretamente em desktops, tablets e smartphones. | ALTA | 
|RNF-002| Deve ser compatível com os navegadores mais utilizados (Chrome, Firefox, Edge e Safari). |  ALTA | 
|RNF-003| Deve utilizar HTTPS para garantir a segurança dos dados dos usuários. | ALTA | 
|RNF-004| Os dados dos usuários devem ser armazenados de forma segura, seguindo a LGPD (Lei Geral de Proteção de Dados). |  ALTA | 
|RNF-005| O backend deve processar requisições em no máximo 2 segundos para garantir uma experiência fluida. | MÉDIA | 
|RNF-006| A interface deve seguir um design intuitivo e minimalista, facilitando a experiência do usuário, mesmo sem conhecimento técnico. |  ALTA | 

## Restrições

Enumere as restrições à sua solução. Lembre-se de que as restrições geralmente limitam a solução candidata.

O projeto está restrito aos itens apresentados na tabela a seguir.

|ID| Restrição                                             |
|--|-------------------------------------------------------|
|001| O projeto deve ser desenvolvido utilizando Python (Flask) no backend e HTML, CSS e JavaScript no frontend. |
|002| A aplicação deve ser implementada e testada em um ambiente de desenvolvimento local antes de qualquer implantação.       |
|003| O sistema deve ser compatível com navegadores modernos (Google Chrome, Mozilla Firefox, Microsoft Edge). |
|004| O desenvolvimento deve ser documentado conforme as normas acadêmicas exigidas pela instituição.       |
|005| O projeto deverá ser entregue até o final do semestre |


## Diagrama de casos de uso

No sistema, os casos de uso são estruturados para atender tanto às necessidades dos clientes quanto dos administradores, promovendo uma interação eficaz. 
-Para os clientes, os casos de uso envolvem o registro de consumo, o que permite que os usuários insiram os dados de suas contas de energia e acompanhem seu histórico de consumo. 
Apartir desses dados, o sistema gera relatórios detalhados que facilitam o monitoramento do padrão de uso e identificam oportunidades para economia.
-Por outro lado, os administradores possuem casos de uso voltados para a gestão do conteúdo e dos usuários: eles podem gerenciar o cadastro e os dados dos clientes, publicar, editar ou excluir notícias relacionadas à economia de energia e administrar as dicas oferecidas.
Essa divisão de responsabilidades torna o sistema robusto, permitindo que cada grupo de usuários interaja de forma adequada com os recursos disponíveis e contribuindo para a promoção de um consumo energético mais consciente e econômico.
![image](https://github.com/user-attachments/assets/ab9e4b05-a9c4-4c77-80e5-101af05a96c6)


