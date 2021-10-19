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
    print("empieza")
    ##(costo, último nodo de la ruta, ruta)
    nodoRaiz = (0,nodoInicial,"")
    frontera = PriorityQueue()
    frontera.put(nodoRaiz)
    explorados = list()
    while( True):
        bandera = 0 
        
        if(frontera.empty()):
            print("frontera vacia")
            break
        nodo=frontera.get()
        if(nodo[1]==meta):
            print("llegaste a la meta")
            break
        explorados.append(nodo[1])
        
        for x in grafo.adj[nodo[1]]:
            #frontera, ponle el costo acumulado(grafo.edges...), el nodo actual (x) y la ruta hasta antes del nodo 
            nodoHijo = (grafo.edges[nodo[1],x]['cost']+nodo[0],x,nodo[2]+' '+nodo[1])
            if (x not in explorados):
                
                for each in list(frontera.queue):
                    if each[1] == x :
                        bandera = 1
                if bandera == 0:
                    frontera.put(nodoHijo)
            # elif
        
    # print(explorados)
            
    print("Costo: ",nodo[0],"Ruta:",nodo[2],nodo[1])
        
        

uniformCostSearch(metro,"Bucharest","Arad")
