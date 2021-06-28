barrado = {
    '584'
}

def buscar_barrado (codBarrado):
    barradoResultado = any(codBarrado in item for item in barrado)
    if barradoResultado == True:
        print('Vendedor barrado')
    else:
        print('Vendedor liberado')
    return barradoResultado

    

