# Criando uma função que irá calcular a escala de fibonnaci
def fibonnaci(numero):
    
    # Definindo a sequencia que sera utilizada
    sequencia = [0,1]

    # Criando um laço de repetição
    while len(sequencia) < numero:

        # Atribuindo a variavel o próximo número
        proximoNumero = sequencia[-1] + sequencia[-2]
        sequencia.append(proximoNumero)

    return sequencia

# Atribuindo a variavel o valor para calculo
numero = 10

# Trazendo o resultado da função
resultadoFuncao = fibonnaci(numero)

# Escrevendo o resultado na tela
print(resultadoFuncao)


