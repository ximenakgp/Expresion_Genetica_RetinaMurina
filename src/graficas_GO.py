

# =========================================================================== 
# =                            Imports 
# =========================================================================== 
import os
import matplotlib.pyplot as plt

# =========================================================================== 
# =                              Functions
# =========================================================================== 

class GraficadorTopTerminos:
    """
    Clase para crear y guardar las gráficas de los términos GO más significativos.
    Esta clase genera una gráfica para cada categoría de GO (GO:BP, GO:MF, GO:CC).
    
    Parámetros:
        output_dir (str): Directorio donde se guardarán las gráficas.
    """

    def __init__(self):
        """
        Inicializa el objeto GraficadorTopTerminos
        Las gráficas se guardarán en una carpeta 'graphs' en el directorio de ejecución actual.
        """
        # Obtener el directorio de ejecución actual
        base_dir = os.getcwd()
        print(f"Directorio de ejecución actual: {base_dir}")

        # Crear la carpeta 'graphs' dentro del directorio actual
        self.output_graph_dir = os.path.join(base_dir, 'graphs')
        print(f"Directorio para gráficos: {self.output_graph_dir}")

        # Crear el directorio para gráficos si no existe
        if not os.path.exists(self.output_graph_dir):
            os.makedirs(self.output_graph_dir)
        
    def graficar(self, top_terminos):
        """
        Crea y guarda gráficas de los términos más significativos por categoría GO (GO:BP, GO:MF, GO:CC).
        
        Parámetros:
            top_terminos (dict): Diccionario con los términos más significativos por categoría GO.
        """
        # Categorías a graficar
        categorias = ['GO:BP', 'GO:MF', 'GO:CC']
        
        for categoria in categorias:
            terminos = top_terminos.get(categoria, [])
            if not terminos:
                continue

            # Extraer nombres, p-values y tamaños de las consultas
            nombres = [termino['name'] for termino in terminos]
            p_values = [termino['p_value'] for termino in terminos]

            # Crear la figura
            plt.figure(figsize=(10, 6))
            
            # Crear un gráfico de barras horizontales con p-values
            plt.barh(nombres, p_values, color='skyblue')

            # Agregar etiquetas y título
            plt.xlabel('p_values')
            plt.ylabel('Categorías sobrerrepresentadas')
            plt.title(f'Top {categoria} Términos más Representados')
            
            # Invertir el eje Y para que el término más significativo esté en la parte superior
            plt.gca().invert_yaxis()
            
            # Guardar la gráfica en un archivo PNG dentro del directorio de gráficos
            output_file = os.path.join(self.output_graph_dir, f"{categoria.replace(':', '_')}_top_terms.png")
            print(f"Guardando gráfica en: {output_file}")
            plt.savefig(output_file)
            plt.show()
            plt.close()


# Bloque principal para pruebas
if __name__ == "__main__":
    graficador = GraficadorTopTerminos()

    # Datos de prueba
    top_terminos = {
        'GO:BP': [
            {'name': 'Proceso 1', 'p_value': 0.001},
            {'name': 'Proceso 2', 'p_value': 0.005},
        ],
        'GO:MF': [
            {'name': 'Función 1', 'p_value': 0.01},
            {'name': 'Función 2', 'p_value': 0.02},
        ],
    }

    graficador.graficar(top_terminos)

