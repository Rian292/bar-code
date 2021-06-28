from regiao import buscar_regiao
from ordem import ordem
from tipo import buscar_tipo
from barrado import buscar_barrado

ordemDoCodigoDeBarras = ordem(codigoDeBarras=input('Coloque o código de barras: '))
resultadoRegiaoOrigem = buscar_regiao(ordemDoCodigoDeBarras[0])
resultadoRegiaoDestino = buscar_regiao(ordemDoCodigoDeBarras[1])
resultadoCodigoLoggi = ordemDoCodigoDeBarras[2]
resultadoCodigoDoVendedor = ordemDoCodigoDeBarras[3]
resultadoTipoDeProduto = buscar_tipo(ordemDoCodigoDeBarras[4])

print(f'Região de origem: {resultadoRegiaoOrigem}')
print(f'Região de destino: {resultadoRegiaoDestino}')
print(f'Código Loggi: {resultadoCodigoLoggi}')
print(f'Código do vendedor: {resultadoCodigoDoVendedor}')
print(f'Tipo de produto: {resultadoTipoDeProduto}')
