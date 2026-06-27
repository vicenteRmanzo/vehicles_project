# Vehicle Data Dashboard

## Descripción del proyecto
Este proyecto consiste en una aplicación web desarrollada con Streamlit para visualizar y explorar datos de anuncios de venta de vehículos utilizando el dataset vehicles_us.csv.

La aplicación permite generar visualizaciones interactivas para analizar la distribución y relación entre variables del conjunto de datos.

## Funcionalidades
- Visualización mediante histograma.
- Visualización mediante gráfico de dispersión.
- Interacción mediante botones o controles de Streamlit.
- Exploración básica de datos.

## Estructura del proyecto

vehicles_project/

- app.py → aplicación web principal.
- vehicles_us.csv → conjunto de datos utilizado.
- requirements.txt → dependencias necesarias.
- notebooks/EDA.ipynb → análisis exploratorio inicial.
- README.md → documentación del proyecto.

## Ejecución local

Instalar dependencias:

```bash
pip install -r requirements.txt
```

Ejecutar aplicación:

```bash
streamlit run app.py
```

## Aplicación desplegada

https://vehicles-project-1-ks63.onrender.com