<h1> En este repositorio de encuentra un simulador paso a paso del algoritmo de Arbol Parcial minimo de Pim, en el cuál el usuario ingresa el grafo con los nodos y pesos, y se muestra gráficamente como se va resolviendo paso a paso </h1>
<h2> Ejemplo de ejecución: </h2>


<h3> --- CONFIGURACIÓN DEL GRAFO ---
    Ingresa las conexiones en el formato: Origen Destino Peso
    Ejemplo: 0 1 5 (Conecta nodo 0 con 1, peso 5)
    Escribe 'fin' cuando termines de agregar aristas.

    >> Ingresa arista (u v w): 0 1 10
   Arista agregada: 0 --(10)-- 1
    >> Ingresa arista (u v w): 1 2 5
   Arista agregada: 1 --(5)-- 2
    >> Ingresa arista (u v w): 2 3 4
   Arista agregada: 2 --(4)-- 3
    >> Ingresa arista (u v w): 3 4 8
   Arista agregada: 3 --(8)-- 4
    >> Ingresa arista (u v w): 4 5 17
   Arista agregada: 4 --(17)-- 5
    >> Ingresa arista (u v w): 5 6 20
   Arista agregada: 5 --(20)-- 6
    >> Ingresa arista (u v w): 6 7 1
   Arista agregada: 6 --(1)-- 7
    >> Ingresa arista (u v w): 2 6 4
   Arista agregada: 2 --(4)-- 6
    >> Ingresa arista (u v w): 3 5 2
   Arista agregada: 3 --(2)-- 5
    >> Ingresa arista (u v w): 1 7 5
   Arista agregada: 1 --(5)-- 7
    >> Ingresa arista (u v w): fin

    ¿En qué nodo quieres iniciar? (Nodos disponibles: [0, 1, 2, 3, 4, 5, 6, 7]): 0

    ========================================
    INICIO DEL ALGORITMO DE PRIM (Manual)
    ========================================

    --- Paso 1 ---
    Visitados: {0}
    Candidatos: [(0, 1, 10)]
     >> ELEGIDA: (0-1) peso 10

    --- Paso 2 ---
    Visitados: {0, 1}
    Candidatos: [(1, 2, 5), (1, 7, 5)]
     >> ELEGIDA: (1-2) peso 5

    --- Paso 3 ---
    Visitados: {0, 1, 2}
    Candidatos: [(1, 7, 5), (2, 3, 4), (2, 6, 4)]
     >> ELEGIDA: (2-3) peso 4

    --- Paso 4 ---
    Visitados: {0, 1, 2, 3}
    Candidatos: [(1, 7, 5), (2, 6, 4), (3, 4, 8), (3, 5, 2)]
     >> ELEGIDA: (3-5) peso 2

    --- Paso 5 ---
    Visitados: {0, 1, 2, 3, 5}
    Candidatos: [(1, 7, 5), (2, 6, 4), (3, 4, 8), (5, 4, 17), (5, 6, 20)]
     >> ELEGIDA: (2-6) peso 4

    --- Paso 6 ---
    Visitados: {0, 1, 2, 3, 5, 6}
    Candidatos: [(1, 7, 5), (3, 4, 8), (5, 4, 17), (6, 7, 1)]
    >> ELEGIDA: (6-7) peso 1

    --- Paso 7 ---
    Visitados: {0, 1, 2, 3, 5, 6, 7}
    Candidatos: [(3, 4, 8), (5, 4, 17)]
     >> ELEGIDA: (3-4) peso 8

    FIN. Costo Total: 34
</h3>