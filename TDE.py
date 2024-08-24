def leituraConjunto(linha):
    return set(linha.strip().split(','))

def efetuarOperacao(operacao, conjunto1, conjunto2):
    if operacao == 'U':
        return conjunto1.union(conjunto2)
    elif operacao == 'I':
        return conjunto1.intersection(conjunto2)
    elif operacao == 'D':
        return conjunto1.difference(conjunto2)
    elif operacao == 'C':
        return {(x, y) for x in conjunto1 for y in conjunto2}
    else:
        raise ValueError(f"Operação inválida!")

def main(diretório):
    with open(diretório, 'r') as arquivo:
        linhas = arquivo.readlines()
        
    numeroOperacoes = int(linhas[0].strip())
    resultados = []
    
    linhaAtual = 1
    for i in range(numeroOperacoes):
        operacao = linhas[linhaAtual].strip()
        conjunto1 = leituraConjunto(linhas[linhaAtual + 1])
        conjunto2 = leituraConjunto(linhas[linhaAtual + 2])
        
        resultado = efetuarOperacao(operacao, conjunto1, conjunto2)
        resultados.append(f"Resultados de {operacao}: {resultado}")
        
        linhaAtual += 3
    
    for resultado in resultados:
        print(resultado)

if __name__ == "__main__":
    diretório = "Coloque seu caminho aqui\\Conjuntos.txt"
    main(diretório)
