#  Mockend
## Documento de Design
###### Versão 1.0

### 1. Introdução
Este projeto tem como objetivo apresentar um design baseando-se no serviço [Mockend](https://mockend.com/), seguindo seu escopo e funcionalidades.

#### 1.1 Requisitos
Os requisitos deste software é basicamente gerar uma API "fake" para o desenvolver testar o seu frontend. Mais informações sobre os requisitos podem ser encontrados no documento abaixo:

[Requisitos](https://github.com/felipelagares/software-design-2021/tree/gustavomarques/mockfreend/requisitos)

### 2. Modelo
Este design utiliza conceitos do [C4 Model](https://c4model.com/) para auxiliar na sua definição. Foi utilizado a criação do diagrama de contexto e do diagrama de contâiner.

#### 2.1 Diagrama de Contexto
<img src="https://github.com/felipelagares/software-design-2021/blob/gustavomarques/mockfreend/imagens/Diagrama_de_Contexto.png">

#### 2.2 Diagrama de Contâiner
<img src="https://github.com/felipelagares/software-design-2021/blob/gustavomarques/mockfreend/imagens/Diagrama_de_Container.png">

### 3. Arquitetura
A arquitetura do software a ser desenvolvido será uma arquitetura híbrida e independente que
une as principais características dos estilos arquiteturais: ​Camadas,​ Cliente-Servidor, REST, e ​prioriza os Atributos de qualidade: Segurança e Portabilidade. Consulte o documento abaixo para mais detalhes.

[Arquitetura](https://github.com/felipelagares/software-design-2021/tree/gustavomarques/mockfreend/arquitetura)

### 4. Geração de Dados
#### 4.1 Tipos de Dados Suportados
Alguns dados possuem parâmetros opcionais, o parâmetro é estabelecido no formato. O tipo de dados gera um número aleatório entre uma faixa de valores estabelecida previamente, por exemplo, se quero um número entre 0 e 10000 uso o formato tipodedados tipodedado{parâmetro} em que o parâmetro é id-0 e id-1000. O comando utilizado é datatypes datatype{id-1000}.

##### 4.1.1 Números
|Chave|Descrição|Exemplo|Parâmetros opcionais|
|---|---|---|---|
|id|Inteiro entre 0 e 500|142|Gera um número inteiro aleatório entre 0 e id-500|
|random-float|Decimal entre 0 e 10|8.753240|Gera um número flutuante aleatório entre 0 e id-10|
|boolean|Verdadeiro ou falso|True|Sem parâmetros|

#### 4.2 Modelo de Dados(?)

### 5. Gestão de Usuários
#### 5.1 Interface

#### 5.2 Persisntência de Dados dos Usuários

### 6. Protótipos
<< colocar umas imagens de exemplo>>
