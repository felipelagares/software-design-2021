#  Mockend
## Documento de Design
###### Versão 1.2

### 1. Introdução
Este projeto tem como objetivo apresentar um design baseando-se no serviço [Mockend](https://mockend.com/), seguindo seu escopo e funcionalidades.

#### 1.1 Requisitos
Os requisitos deste software é basicamente gerar uma API "fake" para o desenvolver testar o seu frontend. Mais informações sobre os requisitos podem ser encontrados no documento abaixo:

[Requisitos](https://github.com/felipelagares/software-design-2021/tree/dev/Loremmock/requisitos)

### 2. Arquitetura
A arquitetura do software a ser desenvolvido será uma arquitetura híbrida e independente que
une as principais características dos estilos arquiteturais: ​Camadas,​ Cliente-Servidor, REST, e ​prioriza os Atributos de qualidade: Segurança e Portabilidade. Consulte o documento abaixo para mais detalhes.

[Arquitetura](https://github.com/felipelagares/software-design-2021/tree/dev/Loremmock/arquitetura)

#### 2.1 Modelo C4
Este design utiliza conceitos do [C4 Model](https://c4model.com/) para auxiliar na sua definição. Foi utilizado a criação do diagrama de contexto e do diagrama de contâiner.

##### 2.1.2 Diagrama de Contexto
<img src="https://github.com/felipelagares/software-design-2021/blob/dev/Loremmock/imagens/Diagrama_de_Contexto.png">

##### 2.1.2 Diagrama de Contâiner
<img src="https://github.com/felipelagares/software-design-2021/blob/dev/Loremmock/imagens/Diagrama_de_Container.png">

### 3. Geração de Dados
#### 3.1 Tipos de Dados Suportados
Alguns dados são complexos demais, portanto tem um hiperlink em sua categoria, que descreve com detalhes como gerar essas valores, todos os tipos de dados possuem parametros opcionais, que permitem o usuario escolher mais precisamente como o dado sera gerado, como por exemplo o id tem como parametro **rep**, **min** e **max**, sendo **rep** quantos id serão gerados(por padrão 1), **min** seria o valor minimo do id e o **max** o valor maximo do id, enquanto respeita o minimo absoluto de 0 e o maximo absoluto de 500. Esse parametros estarão em negrito.

##### 3.1.1 Números
|Chave|Descrição|Exemplo|Parâmetros opcionais|
|---|---|---|---|
|id|Inteiro entre 0 e 500|142|**rep** - Quantos valores diferentes serão gerados;**min** - O valor minimo do numero a ser gerado(Deve ser maior que 0);**max** - O numero maximo a ser gerado(Deve ser menor que 500);|
|random-float|Decimal entre 0 e 10|8.753240|**rep** - Quantos valores diferentes serão gerados;**min** - O valor minimo do numero a ser gerado(Deve ser maior que 0);**max** - O numero maximo a ser gerado(Deve ser menor que 10);|
|boolean|Verdadeiro ou falso|True|rep - Quantos valores diferentes serão gerados|

##### 3.1.2 Pessoa
|Chave|Descrição|Exemplo|Parâmetros opcionais|
|---|---|---|---|
name|Nome(homem por padrão)|Gabriel Leles|**rep** - Quantos valores diferentes serão gerados;**gender** - Genero do nome, só aceita "male" e "female" como valores|
first-name|Nome(homem por padrão)|Gabriel Leles|**rep** - Quantos valores diferentes serão gerados;**gender** - Genero do nome, só aceita "male" e "female" como valores|
last-name|Nome(homem por padrão|Lopes|**rep** - Quantos valores diferentes serão gerados;**gender** - Genero do nome, só aceita "male" e "female" como valores|
middle-name|Nome(homem por padrão|Pires|**rep** - Quantos valores diferentes serão gerados;**gender** - Genero do nome, só aceita "male" e "female" como valores|
username|Nome de usuário|Gabriel-lpl|**rep** - Quantos valores diferentes serão gerados|
email|Endereço de email(domínio padrão loremock.com)|gabrielleles@loremock.com|**rep** - Quantos valores diferentes serão gerados;**dominio** - dominio do email, como "gmail.com"|
social-media|Link de conta de mídia social|https://facebook.com/gabrielleles.1042|**rep** - Quantos valores diferentes serão gerados;**midia** - Rede social gerado, aceita como valores "facebook" e "instagram"|
blood-type|Tipo sanguíneo|O+|**rep** - Quantos valores diferentes serão gerados|
job|Emprego|Engenheiro Civil|**rep** - Quantos valores diferentes serão gerados|
degree|Formação acadêmica|Doutorado|**rep** - Quantos valores diferentes serão gerados|
phone|Número de telefone|+1-(063)-278-5412|**rep** - Quantos valores diferentes serão gerados;**format**- Escolhe a formatação do numero, usando # para os dígitos como por exemplo: "(+#)-###-####"|

##### 3.1.3 [Endereço](https://github.com/felipelagares/software-design-2021/tree/dev/Loremmock/geracao_de_dados/Endereco.md)
|Chave|Descrição|Exemplo|Parâmetros|
|---|---|---|---|
|address|Endereço|Rua Riachuelo|**rep** - Quantos valores diferentes serão gerados|
|postal_code|CEP|69900-809|**rep** - Quantos valores diferentes serão gerados|
|number|Número da casa, do prédio|768|**rep** - Quantos valores diferentes serão gerados|
|floor_number|Número do andar de um prédio|10|**rep** - Quantos valores diferentes serão gerados|
|apartment_number|Número do apartamento de um prédio|1003|**rep** - Quantos valores diferentes serão gerados|
|neighbourhood|Bairro|José Augusto|**rep** - Quantos valores diferentes serão gerados|
|city|Cidade|Rio Branco|**rep** - Quantos valores diferentes serão gerados|
|state_code|Sigla do estado|AC|**rep** - Quantos valores diferentes serão gerados|
|coordinates|Coordenadas|{'longitude':-9.96337570564154, 'latitude':-67.80888950056246}|**rep** - Quantos valores diferentes serão gerados|

##### 3.1.4 [Texto](https://github.com/felipelagares/software-design-2021/tree/dev/Loremmock/geracao_de_dados/Texto.md)
|Chave|Descrição|Exemplo|Parâmetros|
|---|---|---|---|
|text|Sentença|Isto é um exemplo de texto|número de sentenças, máx: 20|
|word|Palavra|['Pneumoultramicroscopicossilicovulcanoconiótico']|número de palavras, máx:20|
|quote|Citação aleatória|Não tenha medo de tentar nem se culpe quando fizer algo que não dê certo|Sem parâmetros|
|lorem|Lorem Ipsum|Lorem ipsum dolor sit amet, consectetur adipiscing elit|número de palavras no lorem, máx:20|

##### 3.1.5 [Data](https://github.com/felipelagares/software-design-2021/tree/dev/Loremmock/geracao_de_dados/Data.md)
|Chave|Descrição|Exemplo|Parâmetros|
|---|---|---|---|
|date|Data no formato YYYY-MM-DD|2022-03-06|Sem parâmetros|
|time|Tempo no formato 24h|16:33:30|Sem parâmetros|
|month|Mês|Março|Sem parâmetros|
|year|Ano|2022|Sem parâmetros|

#### 3.1.6 Hardware
|Chave|Descrição|Exemplo|Parâmetros|
|---|---|---|---|
|cpu|modelo de CPU|Intel Core I7-8550U|Sem parâmetros|
|graphic|modelo da placa de vídeo|NVIDIA GeForce MX150|Sem parâmetros|
|model|modelo do hardware|Lenovo ideapad 330|Sem parâmetros|

#### 3.1.7 Comida
|Chave|Descrição|Exemplo|Parâmetros|
|---|---|---|---|
|fruit|nome de fruta|Goiaba|Sem parâmetros|
|dish|nome da refeição|Feijão tropeiro|Sem parâmetros|
|spice|nome de um tempero ou especiaria|Pimenta do reino|Sem parâmetros|
|vegetable|nome de verduras ou legumes|Couve|Sem parâmetros|
|drink|nome de bebida|Suco de tamarindo|Sem parâmetros|

#### 3.1.8 [Arquivo](https://github.com/felipelagares/software-design-2021/tree/dev/Loremmock/geracao_de_dados/Endereco.md)
|Chave|Descrição|Exemplo|Parâmetros|
|---|---|---|---|
|extension|extensão do arquivo|.png|dependerá do tipo do arquivo. tipos disponiveis: source, text, data, audio, video, image, executable, compressed|
|mime_type|MIME type|application/json|dependerá do tipo do arquivo. tipos disponiveis: application, audio, image, message, text, video|
|filename|nome do arquivo|design.md|dependerá do tipo do arquivo. tipos disponiveis: source, text, data, audio, video, image, executable, compressed|

##### 3.1.9 Negocios
|Chave|Descrição|Exemplo|Parâmetros|
|---|---|---|---|
|company|nome da empresa|Panificadora Alegria|Sem parâmetros|
|company_type|tipo da empresa|Microempresa|Sem parâmetros|
|copyright|copyright|© Mott's, LLP|Sem parâmetros|
|company_catch_phrase|frase de  efeito/lema da empresa|Tecnologia intiutiva nossa especialidade|Sem parâmetros|
|cryptocurrency|codigo da criptomoeda|ETH|Sem parâmetros|
|currency|codigo da moeda|BRL|Sem parâmetros|

##### 3.1.10 Pagamento
|Chave|Descrição|Exemplo|Parâmetros|
|---|---|---|---|
|btc_adress|endereço bitcoin|1EvbUtfMRodWmHFiEhV2SkCAZFHkAcer33|Sem parâmetros|
|eth_adress|endereço etherium|0x4d136b9C4d7229FEf5d09afCBDF609c29Ec2ca66|Sem parâmetros|
|cc_network|marca do cartão de crédito|Inter|Sem parâmetros|
|cc_vality|data de validade do cartão de crédito|07/22|Sem parâmetros|
|cc_number|numero do cartão de crédito|4716 6347 0036 2497|bandeira do cartao, cc_number_visa, tipos disponiveis: mastercard, visa, elo|
|cc_provider|bandeira do cartão de crédito|Elo|Sem parâmetros|

##### 3.1.11 Códigos
|Chave|Descrição|Exemplo|Parâmetros|
|---|---|---|---|
|uuid|UUID|13c2052e-e604-42d0-8c10-e9bb6d48fcfc|Sem parâmetros|
|pin|código|9660|4 Digitos|
|imei|Identificador de Dispositivo Movel|353258073166594|Sem parâmetros|
|hex_color|Cor|6cfc7f|Sem Parâmetros|
|rgb_color|Cor em RGB|rgb(87, 229, 215)|Sem Parâmetros|
|hsv_color|Cor em HSV|hsv(14, 89, 67)|Sem Parâmetros|
|color|Cor|Vermelho|Sem Parâmetros|
|language|Linguagem de programação|java|Sem Parâmetros|

##### 3.1.12 Web
|Chave|Descrição|Exemplo|Parâmetros|
|---|---|---|---|
|ipv4|endereço ipv4|9.151.218.226|Sem parâmetros|
|ipv6|endereço ipv6|a865:90ef:b48d:ec88:a66c:758a:ed1e:5423|Sem parâmetros|
|mac_adress|endereço mac|38:29:5a:85:45:8e|Sem parâmetros|

#### 3.2 Modelo de Dados(?)

### 4. Gestão de Usuários
#### 4.1 Interface

#### 4.2 Persisntência de Dados dos Usuários

### 5. Protótipos
<< colocar umas imagens de exemplo>>
