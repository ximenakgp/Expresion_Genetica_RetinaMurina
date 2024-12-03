# Casos de prueba o escenarios *grafias_GO.py*
Este documento describe los casos de prueba para el script de Python *grafias_GO.py* desarrollado para crear y guardar las gráficas de los términos GO más significativos.

Los casos de prueba se han diseñado teniendo en cuenta las diferentes funcionalidades del script así como los posibles errores que puedan surgir.

Los casos de prueba cubren las características clave del programa y prueban varias condiciones para garantizar la robustez y fiabilidad del script.

La ejecución exitosa de estos casos de prueba asegura que el script está listo para su uso y puede manejar diferentes condiciones de entrada y situaciones de error.

A continuación, presentamos los detalles de los casos de prueba. Cada caso de prueba incluye una descripción del caso de prueba, los datos de entrada utilizados y el resultado esperado.


#### **Caso 1: Datos Completo con Dos Categorías**

**Entrada:**

```python
graficador = GraficadorTopTerminos()

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
```

**Salida Esperada:**

- Archivos generados:
  - `graphs/GO_BP_top_terms.png`
  - `graphs/GO_MF_top_terms.png`

- Los gráficos muestran barras horizontales:
  - En el eje Y, los nombres de los procesos/funciones.
  - En el eje X, los valores de `p_value`.

---

#### **Caso 2: Diccionario Vacío**

**Entrada:**

```python
graficador = GraficadorTopTerminos()

top_terminos = {}

graficador.graficar(top_terminos)
```

**Salida Esperada:**

- No se generan gráficos.
- Consola:
  - No hay errores ni advertencias.
  - Mensaje indicando que no hay datos para graficar.

---

#### **Caso 3: Categorías con Listas Vacías**

**Entrada:**

```python
graficador = GraficadorTopTerminos()

top_terminos = {
    'GO:BP': [],
    'GO:MF': [
        {'name': 'Función 1', 'p_value': 0.01},
        {'name': 'Función 2', 'p_value': 0.02},
    ],
    'GO:CC': [],
}

graficador.graficar(top_terminos)
```

**Salida Esperada:**

- Archivo generado:
  - `graphs/GO_MF_top_terms.png`
- Categorías `GO:BP` y `GO:CC` no producen gráficos ni errores.

---

#### **Caso 4: Verificación de Creación Automática de Carpeta**

**Entrada:**

```python
# Asegúrate de que la carpeta graphs no exista antes de ejecutar este caso
import shutil
if os.path.exists('graphs'):
    shutil.rmtree('graphs')

graficador = GraficadorTopTerminos()

top_terminos = {
    'GO:BP': [{'name': 'Proceso 1', 'p_value': 0.001}],
}

graficador.graficar(top_terminos)
```

**Salida Esperada:**

- Carpeta `graphs` creada automáticamente.
- Archivo generado:
  - `graphs/GO_BP_top_terms.png`.

---

#### **Caso 5: Formato de Valores de `p_value`**

**Entrada:**

```python
graficador = GraficadorTopTerminos()

top_terminos = {
    'GO:BP': [
        {'name': 'Proceso A', 'p_value': 0.1},
        {'name': 'Proceso B', 'p_value': 0.000456},
        {'name': 'Proceso C', 'p_value': 0.05},
    ],
}

graficador.graficar(top_terminos)
```

**Salida Esperada:**

- Archivo generado:
  - `graphs/GO_BP_top_terms.png`.
- El gráfico muestra valores de `p_value` correctamente representados en el eje X.

---

#### **Caso 6: Nombres con Caracteres Especiales**

**Entrada:**

```python
graficador = GraficadorTopTerminos()

top_terminos = {
    'GO:MF': [
        {'name': 'Función 1 (α)', 'p_value': 0.02},
        {'name': 'Función 2: "Especial"', 'p_value': 0.03},
    ],
}

graficador.graficar(top_terminos)
```

**Salida Esperada:**

- Archivo generado:
  - `graphs/GO_MF_top_terms.png`.
- Los caracteres especiales (`(α)`, `"Especial"`) aparecen correctamente en el gráfico.
