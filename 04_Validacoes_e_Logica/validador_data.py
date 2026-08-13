# Exercícios Python 
# Receba do usuário uma data no formato AAAAMMDD e exiba-a como DD/MM/AAAA.
data = input("Digite uma data no formato AAAAMMDD:")
# Validar se tem 8 dígitos: 
# len() verifica se a data tem o número correto de digítos e 
# data.isdigit() verifica se a entrada foi difitada como números de 0 a 9 
if not (len(data) == 8 and data.isdigit()):
    print("A data está com formatação errada!") 
else:   
    ano = data[0:4]
    mes = data[4:6]
    dia = data[6:8]

    # Validar limites de caracteres para mês e dia: 
    # Esse bloco de código verifica se a entrada do usuário está 
    # dentro dos limites de datas reais
    # 1   <=   int(mes)   <=   12
    #(Mínimo)     (Valor)     (Máximo)
    if not (1 <= int(mes) <= 12 and 1 <= int(dia) <= 31):
        print("Dia ou mês inválido!")
    else: print(dia + '/' + mes + '/' + ano)





