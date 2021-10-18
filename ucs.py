import networkx as nx
from networkx.classes.function import is_empty
from networkx.classes.reportviews import NodeView
from queue import PriorityQueue

from networkx.linalg.laplacianmatrix import _transition_matrix


metro = nx.Graph()
metro.add_nodes_from([  "Arad","Zerind","Oradea","Sibiu","Fagaras",
                        "Timisoara","Lugoj","Mehadia","Drobeta","Craiova",
                        "Rimnicu Vilcea","Pitesti","Bucharest","Giurgiu",
                        "Urziceni","Hirsova","Eforie","Vaslui","Iasi","Neamt"
])
metro.add_edges_from(  #23 edges
                    [   ("Arad","Zerind",{'cost':75}),
                        ("Arad","Timisoara",{'cost':118}),
                        ("Arad","Sibiu",{'cost':140}),
                        ("Zerind","Oradea",{'cost':71}),
                        ("Sibiu","Fagaras",{'cost':99}),
                        ("Sibiu","Oradea",{'cost':151}),
                        ("Sibiu","Rimnicu Vilcea",{'cost':80}),
                        ("Timisoara","Lugoj",{'cost':111}),
                        ("Lugoj","Mehadia",{'cost':70}),
                        ("Mehadia","Drobeta",{'cost':75}),
                        ("Drobeta","Craiova",{'cost':120}),
                        ("Craiova","Rimnicu Vilcea",{'cost':146}),
                        ("Craiova","Pitesti",{'cost':138}),
                        ("Fagaras","Bucharest",{'cost':211}),
                        ("Rimnicu Vilcea","Pitesti",{'cost':97}),
                        ("Pitesti","Bucharest",{'cost':101}),
                        ("Bucharest","Giurgiu",{'cost':90}),
                        ("Bucharest","Urziceni",{'cost':85}),
                        ("Urziceni","Hirsova",{'cost':98}),
                        ("Hirsova","Eforie",{'cost':86}),
                        ("Urziceni","Vaslui",{'cost':142}),
                        ("Vaslui","Iasi",{'cost':92}),
                        ("Iasi","Neamt",{'cost':87})
                        
])
def uniformCostSearch(grafo, nodoInicial = "Arad", meta = "Bucharest"):
    costo = 0
    frontera = PriorityQueue() #meter los nodos frontera de nodoInicial
    nodosExplorados = list()
    frontera.put((0,nodoInicial))
    while(True):
        nodoActual = frontera.get()
        for x in grafo.adj[nodoActual[1]]:
            if x[1] in nodosExplorados:
                nodoActual = nodoActual #no hace nada
            else:
                frontera.put((grafo.edges[nodoActual[1],x]['cost'],x))
        #if frontera is empty return fail
        if(frontera.empty()):
            print("Fail")
            break
        #if goal is nodoActual return solution
        print(nodoActual[1])
        if nodoActual[1] == meta:
            print("Costo",nodoActual[0],"ruta: ",nodoActual[1])
            return nodoActual #necesita retornar el camino
        else:
            nodosExplorados.append(nodoActual[1])

uniformCostSearch(metro,"Bucharest","Arad")
