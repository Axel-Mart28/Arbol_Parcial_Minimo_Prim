#En este programa el usuario puede ingresar un grafo manualmente para simular el algoritmo de Prim paso a paso.
import networkx as nx
import matplotlib.pyplot as plt

def crear_grafo_usuario(): #Función para crear un grafo basado en la entrada del usuario
    G = nx.Graph()
    print("\n--- CONFIGURACIÓN DEL GRAFO ---")
    print("Ingresa las conexiones en el formato: Origen Destino Peso")
    print("Ejemplo: 0 1 5 (Conecta nodo 0 con 1, peso 5)")
    print("Escribe 'fin' cuando termines de agregar aristas.\n")

    while True: #Bucle para ingresar aristas
        entrada = input(">> Ingresa arista (u v w): ")
        if entrada.lower() == 'fin':
            break
        
        try:
            # Separamos el texto por espacios
            datos = entrada.split()
            if len(datos) != 3:
                print("Error: Debes ingresar 3 valores (origen destino peso).")
                continue
            
            u = int(datos[0])
            v = int(datos[1])
            w = int(datos[2])
            
            # Agregamos la arista al grafo
            G.add_edge(u, v, weight=w)
            print(f"   Arista agregada: {u} --({w})-- {v}")
            
        except ValueError: #Captura errores de conversion
            print("Error: Por favor ingresa números enteros.")

    return G

def simulador_prim_manual(): #Función principal para simular Prim con entrada del usuario
    # 1. LLAMAMOS A LA FUNCIÓN DE INGRESO MANUAL
    G = crear_grafo_usuario()
    
    if len(G.nodes) == 0: #Verificamos si el grafo tiene nodos
        print("El grafo está vacío. Saliendo...")
        return

    # Posiciones fijas para los nodos
    pos = nx.spring_layout(G, seed=42) 

    # --- 2. PREPARACIÓN DE VISUALIZACIÓN ---
    plt.ion() 
    fig, ax = plt.subplots(figsize=(10, 7))
    
    # Preguntamos nodo inicial
    try:
        start_node = int(input(f"\n¿En qué nodo quieres iniciar? (Nodos disponibles: {list(G.nodes)}): "))
        if start_node not in G.nodes:
            raise ValueError
    except:
        start_node = list(G.nodes())[0] # Si falla, agarra el primero que encuentre
        print(f"Entrada inválida. Iniciando en nodo {start_node} por defecto.")

    mst_edges = [] 
    visited = {start_node}  
    all_nodes = set(G.nodes())
    
    print(f"\n{'='*40}")
    print(f"INICIO DEL ALGORITMO DE PRIM (Manual)")
    print(f"{'='*40}\n")

    # --- 3. BUCLE PRINCIPAL DE PRIM  ---
    step = 1
    while len(visited) < len(all_nodes):
        ax.clear()
        ax.set_title(f"Simulación de Prim - Paso {step}", fontsize=15)

        # Dibujar grafo base
        edge_labels = nx.get_edge_attributes(G, 'weight')
        nx.draw(G, pos, ax=ax, with_labels=True, node_color='lightblue', 
                edge_color='gray', node_size=700, font_weight='bold', style='dashed')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, ax=ax)

        # Logica Greedy, que ayuda a encontrar la arista minima
        min_edge = None
        min_weight = float('inf')
        possible_edges = []

        # Buscar arista mas barata que cruce la frontera
        found_connection = False
        for u in visited:
            for v in G.neighbors(u):
                if v not in visited:
                    found_connection = True
                    weight = G[u][v]['weight']
                    possible_edges.append((u, v, weight))
                    if weight < min_weight:
                        min_weight = weight
                        min_edge = (u, v)

        # Si el grafo no es conexo (hay islas), Prim se detiene
        if not found_connection:
            print("¡ALERTA! No hay más conexiones posibles. El grafo no es conexo.")
            break

        # Consola
        print(f"--- Paso {step} ---")
        print(f"Visitados: {visited}")
        print(f"Candidatos: {possible_edges}")
        
        if min_edge: # Si encontramos una arista minima
            u, v = min_edge
            print(f" >> ELEGIDA: ({u}-{v}) peso {min_weight}")
            mst_edges.append((u, v))
            visited.add(v)
            
            # Dibujar selección
            nx.draw_networkx_edges(G, pos, edgelist=mst_edges, edge_color='green', width=3, ax=ax)
            nx.draw_networkx_edges(G, pos, edgelist=[min_edge], edge_color='red', width=4, ax=ax)
            nx.draw_networkx_nodes(G, pos, nodelist=list(visited), node_color='#90EE90', node_size=700, ax=ax)
        
        print("")
        plt.pause(2)
        step += 1

    # --- 4. RESULTADO FINAL ---
    ax.clear()
    total_cost = sum([G[u][v]['weight'] for u,v in mst_edges])
    ax.set_title(f"Árbol Parcial Mínimo Completado\nCosto Total: {total_cost}", fontsize=15, color='green')
    
    nx.draw(G, pos, ax=ax, with_labels=True, node_color='lightgray', edge_color='lightgray', style='dotted')
    nx.draw_networkx_edges(G, pos, edgelist=mst_edges, edge_color='green', width=3)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    nx.draw_networkx_nodes(G, pos, nodelist=list(visited), node_color='#90EE90', node_size=700)
    
    print(f"FIN. Costo Total: {total_cost}")
    plt.ioff()
    plt.show()

if __name__ == "__main__":
    simulador_prim_manual()