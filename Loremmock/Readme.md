#  Mockend
## Documento de Design
###### Versão 1.2

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
name|Nome(homem por padrão)|Gabriel Leles|Gênero usando male ou female, name-male
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

##### 4.1.3 Endereço
|Chave|Descrição|Exemplo|Parâmetros|
|---|---|---|---|
|address|Endereço|Rua Riachuelo|Sem parâmetros|
|postal_code|CEP|69900-809|Sem parâmetros|
|number|Número da casa, do prédio, do andar e do apartamento|768|Sem parâmetros|
|neighbourhood|Bairro|José Augusto|Sem parâmetros|
|city|Cidade|Rio Branco|Sem parâmetros|
|state_code|Sigla do estado|AC|Sem parâmetros|
|coordinates|Coordenadas|{'longitude':-9.96337570564154, 'latitude':-67.80888950056246}|Sem parâmetros|

##### 4.1.4 Texto
|Chave|Descrição|Exemplo|Parâmetros|
|---|---|---|---|
|text|Sentença|Isto é um exemplo de texto|número de sentenças, máx: 15|
|word|Palavra|['Pneumoultramicroscopicossilicovulcanoconiótico']|número de palavras, máx:15|
|quote|Citação aleatória|Não tenha medo de tentar nem se culpe quando fizer algo que não dê certo|Sem parâmetros|
|lorem|Lorem Ipsum|Lorem ipsum dolor sit amet, consectetur adipiscing elit|número de palavras no lorem, máx:20|

##### 4.1.5 Data
|Chave|Descrição|Exemplo|Parâmetros|
|---|---|---|---|
|date|Data no formato YYYY-MM-DD|2022-03-06|Sem parâmetros|
|time|Tempo no formato 24h|16:33:30|Sem parâmetros|
|month|Mês|Março|Sem parâmetros|
|year|Ano|2022|Sem parâmetros|

#### 4.1.6 Hardware
|Chave|Descrição|Exemplo|Parâmetros|
|---|---|---|---|
|cpu|modelo de CPU|Intel Core I7-8550U|Sem parâmetros|
|graphic|modelo da placa de vídeo|NVIDIA GeForce MX150|Sem parâmetros|
|model|modelo do hardware|Lenovo ideapad 330|Sem parâmetros|

#### 4.1.7 Comida
|Chave|Descrição|Exemplo|Parâmetros|
|---|---|---|---|
|fruit|nome de fruta|Goiaba|Sem parâmetros|
|dish|nome da refeição|Feijão tropeiro|Sem parâmetros|
|spice|nome de um tempero ou especiaria|Pimenta do reino|Sem parâmetros|
|vegetable|nome de verduras ou legumes|Couve|Sem parâmetros|
|drink|nome de bebida|Suco de tamarindo|Sem parâmetros|

#### 4.1.8 Arquivo
|Chave|Descrição|Exemplo|Parâmetros|
|---|---|---|---|
|extension|extensão do arquivo|.png|dependerá do tipo do arquivo. tipos disponiveis: source, text, data, audio, video, image, executable, compressed|
|mime_type|MIME type|application/json|dependerá do tipo do arquivo. tipos disponiveis: application, audio, image, message, text, video|
|filename|nome do arquivo|design.md|dependerá do tipo do arquivo. tipos disponiveis: source, text, data, audio, video, image, executable, compressed|

##### 4.1.9 Negocios
|Chave|Descrição|Exemplo|Parâmetros|
|---|---|---|---|
|company|nome da empresa|Panificadora Alegria|Sem parâmetros|
|company_type|tipo da empresa|Microempresa|Sem parâmetros|
|copyright|copyright|© Mott's, LLP|Sem parâmetros|
|company_catch_phrase|frase de  efeito/lema da empresa|Tecnologia intiutiva nossa especialidade|Sem parâmetros|
|cryptocurrency|codigo da criptomoeda|ETH|Sem parâmetros|
|cryptocurrency|codigo da moeda|BRL|Sem parâmetros|

#### 4.2 Modelo de Dados(?)

### 5. Gestão de Usuários
#### 5.1 Interface

#### 5.2 Persisntência de Dados dos Usuários

### 6. Protótipos
<< colocar umas imagens de exemplo>>
