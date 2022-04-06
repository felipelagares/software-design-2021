1. Gerar uma chave* de bitcoin com 26-32 digitos (selecionando aleatoriomente) e transformar em numero hexadecimal.
2. Gerar uma chave* privada de 64 digitos, depois gerar uma publcia com 128 digitos e usar keccak-256 para tornar essas chaves no endereço.
3. Gera uma bandeira aleatoria baseado num numero* entre 1 e 3 e logo apos procura na lista de BIN da respectiva bandeira.
4. Escolher um mes e um ano aleatoriamente gerado pela Data.
5. Gerar um numero de digitos* aleatorios baseado na bandeira e no BIN do cartão, se não for dado uma bandeira, gerar um numero* entre 1 e 3 para definir a bandeira, os 4 primeiros digitos são definidos pela bandeira, o BIN sera definido aleatoriamente por um numero* equivalente ao numero total de BINs da bandeira, a lista de BINs deve ser recebida usando a API de dev da Elo, Visa ou Mastercard. O ultimo digito sera definido verificado o numero do cartão com o algoritmo de Luhn e criar o ultimo digito para agradar o algoritmo.

* Os números aleatórios serão gerado usando a geração de números deste software (classe Random do Java).
