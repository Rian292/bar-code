
def ordem(codigoDeBarras):
	regiaoOrigem = codigoDeBarras[0:3]
	regiaoDestino = codigoDeBarras[3:6]
	codigoLoggi = codigoDeBarras[6:9]
	codigoVendedor = codigoDeBarras[9:12]
	tipoProduto = codigoDeBarras[12:15]
	return regiaoOrigem,regiaoDestino, codigoLoggi, codigoVendedor,tipoProduto

