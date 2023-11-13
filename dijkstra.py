pais = {}
custos = {}
grafo = {}
grafo['inicio'] = {}
grafo['a'] = {}
grafo['b'] = {}
grafo['c'] = {}
grafo['d'] = {}
grafo['inicio']['a'] = 5
grafo['inicio']['b'] = 2
grafo['a']['c'] = 4
grafo['a']['d'] = 2
grafo['b']['a'] = 8
grafo['b']['d'] = 7
grafo['c']['d'] = 6
grafo['c']['fim'] = 3
grafo['d']['fim'] = 1
custos['a'] = 5
custos['b'] = 2
custos['c'] = float('inf')
custos['d'] = float('inf')
custos['fim'] = float('inf')
pais['a'] = 'inicio'
pais['b'] = 'inicio'
pais['c'] = None
pais['d'] = None
pais['fim'] = None
processados = []

def ache_no_custo_mais_baixo(custos):
    custo_mais_baixo = float('inf')
    nodo_custo_mais_baixo = None

    for nodo in custos:
        custo = custos[nodo]
        if custo < custo_mais_baixo and nodo not in processados:
            custo_mais_baixo = custo
            nodo_custo_mais_baixo = nodo
        processados.append(nodo)
        return nodo_custo_mais_baixo

nodo = ache_no_custo_mais_baixo(custos)

while nodo is not None:
    custo = custos[nodo]
    vizinhos = grafo[nodo]
    for n in vizinhos.keys():
        novo_custo = custo + vizinhos[n]
        if custos[n] > novo_custo:
            custos[n] = novo_custo
            pais[n] = nodo
    processados.append(nodo)
    nodo = ache_no_custo_mais_baixo(custos)
    print(nodo)

print(processados)
