class RepresentacionGrafo:
    def __init__(self, num_vertices, aristas):
        self.n = num_vertices
        self.aristas = aristas
        self.m = len(aristas)

    def matriz_adyacencia(self):
        # Inicializar matriz n x n con ceros
        A = [[0] * self.n for _ in range(self.n)]
        for u, v, _ in self.aristas:
            A[u][v] = 1
            A[v][u] = 1 # Asumiendo grafo no dirigido
        return A

    def matriz_incidencia(self):
        # Inicializar matriz n (vértices) x m (aristas) con ceros
        I = [[0] * self.m for _ in range(self.n)]
        for indice_arista, (u, v, _) in enumerate(self.aristas):
            I[u][indice_arista] = 1
            I[v][indice_arista] = 1
        return I

    def matriz_pesos(self):
        # Inicializar con infinito para no conectados, 0 en la diagonal
        inf = float('inf')
        W = [[inf] * self.n for _ in range(self.n)]
        for i in range(self.n):
            W[i][i] = 0
            
        for u, v, peso in self.aristas:
            W[u][v] = peso
            W[v][u] = peso
        return W

    def matriz_laplaciana(self):
        # L = D - A
        A = self.matriz_adyacencia()
        L = [[0] * self.n for _ in range(self.n)]
        
        # Calcular grados para la diagonal principal
        for i in range(self.n):
            grado = sum(A[i])
            L[i][i] = grado
            
            # Llenar el resto con -A
            for j in range(self.n):
                if i != j and A[i][j] == 1:
                    L[i][j] = -1
        return L
    
def imprimir_matriz(M):
    for fila in M:
        print(fila)   



# --- Ejemplo de uso ---
# 3 Vértices (0, 1, 2)
# Arista 0-1 con peso 5, Arista 1-2 con peso 3
aristas_ejemplo = [(0, 1, 5), (1, 2, 3)]
grafo = RepresentacionGrafo(3, aristas_ejemplo)

print("Matriz de Adyacencia:")
imprimir_matriz(grafo.matriz_adyacencia())

print("\nMatriz de Incidencia:")
imprimir_matriz(grafo.matriz_incidencia())

print("\nMatriz de Pesos:")
imprimir_matriz(grafo.matriz_pesos())

print("\nMatriz Laplaciana:")
imprimir_matriz(grafo.matriz_laplaciana())