1. Gerar um cep válido para a chave _postal_code_
    * Como sugestão, usar o webservice [ViaCEP](https://viacep.com.br/)
2. Preencher a chave _address_, _neighbourhood_, _city_ e _state_code_ definido pelo CEP
3. Gerar um número inteiro aleatório entre 1 e 999 para a chave _number_
4. Escolher aleatoriamente se o endereço vai ser de uma casa ou um prédio, com as chances de 55% para casas e 45% para prédios
    * Se o prédio for escolhido gerar um número inteiro aleatório entre 2 e 163 para a chave _floor_number_, com as chances de 90% para a faixa (>=2;<=30), 8% para a faixa(>=31;<=100) e 2% para a faixa(>=101;<=163)
        * Gerar um número inteiro aleatório para a chave _apartment_number_ seguindo o modelo XXYY, onde XX representa o número do andar e YY é um número que pode variar de 1 até 10
    * Se a casa for escolhida as chaves _floor_number_ e _apartment_number_ serão vazias
5. Pegar as coordenadas do endereço para preencher a chave _coordinates_
