tipo = {
    '000': 'Jóias',
    '111': 'Livros',
    '333': 'Eletrônicos',
    '555': 'Bebidas',
    '888': 'Brinquedos'
}

def buscar_tipo(codigoTipo):
    tipoResultado = any(codigoTipo in item for item in tipo)
    if tipoResultado == False:
        print('Não enviamos produto desse tipo')
        return tipoResultado
    else:
        return tipo[codigoTipo]