regioes = {
    '111': 'Centro-oeste',
    '333': 'Nordeste',
    '555': 'Norte',
    '888': 'Sudeste',
    '000': 'Sul'
}

def buscar_regiao(codigo):
    tipoResultado = any(codigo in item for item in regioes)
    if tipoResultado == False:
        print('Região inválida')
        return tipoResultado
    else:
        return regioes[codigo]
