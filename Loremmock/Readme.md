#  Mockend
## Documento de Design
###### Versão 1.1

### 1. Introdução
Este projeto tem como objetivo apresentar um design baseando-se no serviço [Mockend](https://mockend.com/), seguindo seu escopo e funcionalidades.

#### 1.1 Requisitos
Os requisitos deste software é basicamente gerar uma API "fake" para o desenvolver testar o seu frontend. Mais informações sobre os requisitos podem ser encontrados no documento abaixo:

[Requisitos](https://github.com/felipelagares/software-design-2021/tree/dev/Loremmock/requisitos)

### 2. Modelo
Este design utiliza conceitos do [C4 Model](https://c4model.com/) para auxiliar na sua definição. Foi utilizado a criação do diagrama de contexto e do diagrama de contâiner.

#### 2.1 Diagrama de Contexto
<img src="https://github.com/felipelagares/software-design-2021/blob/dev/Loremmock/imagens/Diagrama_de_Contexto.png">

#### 2.2 Diagrama de Contâiner
<img src="https://github.com/felipelagares/software-design-2021/blob/dev/Loremmock/imagens/Diagrama_de_Container.png">

### 3. Arquitetura
A arquitetura do software a ser desenvolvido será uma arquitetura híbrida e independente que
une as principais características dos estilos arquiteturais: ​Camadas,​ Cliente-Servidor, REST, e ​prioriza os Atributos de qualidade: Segurança e Portabilidade. Consulte o documento abaixo para mais detalhes.

[Arquitetura](https://github.com/felipelagares/software-design-2021/tree/dev/Loremmock/arquitetura)

### 4. Geração de Dados
#### 4.1 Tipos de Dados Suportados
Alguns dados possuem parâmetros opcionais, o parâmetro é estabelecido no formato. O tipo de dados gera um número aleatório entre uma faixa de valores estabelecida previamente, por exemplo, se quero um número entre 0 e 10000 uso o formato tipodedados tipodedado{parâmetro} em que o parâmetro é id-0 e id-1000. O comando utilizado é datatypes datatype{id-1000}.

##### 4.1.1 Números
|Chave|Descrição|Exemplo|Parâmetros opcionais|
|---|---|---|---|
|id|Inteiro entre 0 e 500|142|Gera um número inteiro aleatório entre 0 e id-500|
|random-float|Decimal entre 0 e 10|8.753240|Gera um número flutuante aleatório entre 0 e id-10|
|boolean|Verdadeiro ou falso|True|Sem parâmetros|

##### 4.1.2 Pessoa
|Chave|Descrição|Exemplo|Parâmetros opcionais|
|---|---|---|---|
nome|Nome(homem por padrão)|Gabriel Leles|Gênero usando male ou female, name-male
first-name|Nome(homem por padrão)|Gabriel Leles|Gênero usando male ou female, first_name-male
last-name|Nome(homem por padrão|Lopes|Gênero usando male ou female, last_name-male
middle-name|Nome(homem por padrão|Pires|Gênero usando male ou female, middle_name-male
username|Nome de usuário|Gabriel-lpl|Sem parâmetros
email|Endereço de email(domínio padrão loremock.com)|gabrielleles@loremock.com|domínio, email-gmail.com
social-media|Link de conta de mídia social|https://facebook.com/gabrielleles.1042|Sites de mídia social, social_media-facebook, contas suportadas:facebook, instagram
blood-type|Tipo sanguíneo|O+|Sem parâmetros
job|Emprego|Engenheiro Civil|Sem parâmetro
degree|Formação acadêmica|Doutorado|Sem parâmetro
phone|Número de telefone|+1-(063)-278-5412|Formatar usando # para os dígitos, phone--(+#)-###-###

#### 4.2 Modelo de Dados(?)

### 5. Gestão de Usuários
#### 5.1 Interface

#### 5.2 Persisntência de Dados dos Usuários

### 6. Protótipos
<< colocar umas imagens de exemplo>>
