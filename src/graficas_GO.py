import os
import matplotlib.pyplot as plt

class GraficadorTopTerminos:
    """
    Clase para crear y guardar las gráficas de los términos GO más significativos.
    Esta clase genera una gráfica para cada categoría de GO (GO:BP, GO:MF, GO:CC).
    
    Parámetros:
        output_dir (str): Directorio donde se guardarán las gráficas.
    """

    def __init__(self, output_dir):
        """
        Inicializa el objeto GraficadorTopTerminos.
        
        Parámetros:
            output_dir (str): Directorio donde se guardarán las gráficas.
        """
        self.output_dir = output_dir
        
        # Extraer solo el directorio de la ruta completa, sin el nombre de archivo
        output_dir_path = os.path.dirname(self.output_dir)
        
        # Crear el directorio si no existe
        if not os.path.exists(output_dir_path):
            os.makedirs(output_dir_path)
        
        # Ahora crear la carpeta 'graphs' dentro del directorio de salida
        self.output_graph_dir = os.path.join(output_dir_path, 'graphs')
        
        # Verificar si el directorio para los gráficos existe, si no, crearlo
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
            #query_sizes = [termino['query_size'] for termino in terminos]
            
            # Crear la figura
            plt.figure(figsize=(10, 6))
            
            # Crear un gráfico de barras horizontales con p-values
            plt.barh(nombres, p_values, color='skyblue')
            
            # Agregar etiquetas y título
            plt.xlabel('p-value')
            plt.title(f'Top {categoria} Términos más Representados')
            
            # Invertir el eje Y para que el término más significativo esté en la parte superior
            plt.gca().invert_yaxis()  
            
            # Aplicar escala logarítmica al eje Y si los p-values son pequeños
            plt.yscale('log')  # Escala logarítmica en el eje Y
            
            # Guardar la gráfica en un archivo PNG dentro del directorio de gráficos
            output_file = os.path.join(self.output_graph_dir, f"{categoria}_top_terms.png")
            plt.savefig(output_file)
            plt.close()




