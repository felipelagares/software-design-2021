
#  Mockend
## Documento de descrição da Arquitetura de Software 
###### Versão 1.0

### 1. Introdução 
#### 1.1 Finalidade
Este documento tem como objetivo definir os aspectos da arquitetura do software Mockend. Utilizando-se de diferentes pontos de vista de desenvolvimento, para descrever aspectos distintos do sistema. Sua finalidade é capturar e transmitir as decisões arquiteturais significativas que foram feitas no sistema.

#### 1.2 Escopo
Este documento é gerado a partir do levantamento de requisitos feito para o Mockend que tem por finalidade auxiliar o levantamento de dados brutos para testes no front-end. As seções foram extraidas de um modelo de documento de arquitetura de software.

#### 1.3 Definições, Acrônimos e Abreviações

#### 1.4 Referências

#### 1.5 Visão Geral
Os próximos tópicos descrevem quais serão os requisitos e restrições utilizados para definir a arquitetura a ser implementada, bem como, quais atributos de qualidades serão priorizados e o porquê da escolha. Quais os padrões arquiteturais serão utilizados conforme os atributos de qualidade selecionados e como funcionará o trade-off entre esses padrões arquiteturais, bem como o porquê da escolha dos padrões arquiteturais. Quais e como as visões arquiteturais serão detalhadas e quais os pontos de vista da arquitetura serão utilizados para descrever as visões.

### 2. Contexto da Arquitetura
 Decidiu-se utilizar a arquitetura cliente-servidor pelo fato de estarmos desenvolvendo um serviço e Restful por ser voltada a serviços e sua ampla utilização globalmente.

#### 2.1 Funcionalidades e Restrições Arquiteturais

|Id.|Tipo|Id. do documento de História de Usuário|
|---|---|---|
|RAS_1|Requisitos Não-Funcionais|US01|

Os RAS serão os responsáveis por guiar as decisões sobre quais estilos arquiteturais serão adequados para favorecer os atributos de qualidade priorizados.

O RAS_1 deixa claro que haverá uma comunicação entre este software e um software externo, através da API "fake". Isto direciona para a utilização do estilo arquitetural Cliente-Servidor e fica claro, também, a necessidade da utilização do estilo arquitetural de Camadas, como forma de viabilizar a separação das responsabilidades do sistema e do estilo arquitetural REST para definir os métodos de comunicação entre os componentes.

#### 2.2 Atributos de Qualidades Prioritários
Conforme definido pelo tópico anterior (2.1), o software a ser desenvolvido realizará interações com um software externo. Devido a essa característica é necessário implantar um modelo arquitetural que possua a **Segurança** como um de seus atributos de qualidade.

O Software a ser desenvolvido deverá coexistir com outros sistemas. Os estilos arquiteturais cliente-servidor em conjunto com ferramentas de implantação favorecem a coexistência do software e por conseguinte o atributo de qualidade **Portabilidade**.

E assim, definimos os atributos de qualidade a serem priorizados durante o
desenvolvimento da arquitetura a ser implementada: Segurança e Portabilidade respectivamente.

### 3. Representação da Arquitetura

Arquitetura do software a ser desenvolvido será uma arquitetura híbrida e independente que
une as principais características dos estilos arquiteturais: ​Camadas,​ Cliente-Servidor, REST, e ​prioriza os Atributos de qualidade: Segurança e Portabilidade.<br />
Para representar as decisões arquiteturais definidas ao findar da análise, serão utilizados os pontos de vista definidos detalhados a baixo.

### 4. Ponto de vista dos Casos de Uso
#### 4.1 Visão Geral
Para fornecer uma base para o planejamento da arquitetura e de todos os outros artefatos que serão gerados durante o ciclo de vida do software, é gerada,
na análise de requisitos, uma visão chamada visão de casos de uso. Só existe uma visão de casos de uso para cada sistema. Ela ilustra os casos de uso e
cenários que englobam o comportamento, as classes e riscos técnicos significativos do ponto de vista da arquitetura. A visão de casos de uso é refinada
e considerada inicialmente em cada iteração do ciclo de vida do software.

### 5. Ponto de vista do Desenvolvedor
#### 5.1 Visão Geral
Desenvolver uma API seguindo as restrições e funcionalidades arquiteturais a estrutura Restful, sendo capaz de receber solicitações de dados seguindo parâmetros definidos pelo usuario e usar e escrever num banco de dados com os dados pedidos, entregando ao software externo esses dados que usará da API como o usuário desejar. Tudo isso deve seguir os atributos impostos pela 2.2 por serem prioritarios. 
#### 5.2 Visão lógica
As caracteristicas de uma API e os atributos prioritarios serão definidos pela estrutura Restful, porém os parâmetros dados ao API serão dados em página Web que serão aplicados com HTTPS pelo usuário, junto com a base de dados do usuário, que permitirá a API diretamente use e escreva para o software externo.