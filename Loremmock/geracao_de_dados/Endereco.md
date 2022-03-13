1. Gerar um cep válido para a chave postal_code
    * Como sugestão, usar o webservice [ViaCEP](https://viacep.com.br/)
2. Preencher a chave address, neighbourhood, city e state_code definido pelo CEP
3. Gerar um número inteiro aleatório entre 1 e 999 para a chave number
4. Escolher aleatoriamente se o endereço vai ser de uma casa ou um prédio, com as chances de 55% para casas e 45% para prédios
    * Se o prédio for escolhido gerar um número inteiro aleatório entre 2 e 163 para a chave floor_number, com as chances de 90% para a faixa (>=2;<=30), 8% para a faixa(>=31;<=100) e 2% para a faixa(>=101;<=163)
        * Gerar um número inteiro aleatório para a chave apartment_number seguindo o modelo XXYY, onde XX representa o número do andar e YY é um número que pode variar de 1 até 10
    * Se a casa for escolhida as chaves floor_number e apartment_number serão vazias
5. Pegar as coordenadas do endereço para preencher a chave coordinates