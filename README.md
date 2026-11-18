# Conexión social y digital en México

## Propósito

Este proyecto analiza la relación entre la conexión digital y la conexión humana en México, explorando cómo el uso de tecnologías y redes sociales se relaciona con distintas dimensiones del bienestar social.

A partir de los datos de la Encuesta Nacional de Bienestar Autorreportado (ENBIARE) 2021, se busca identificar patrones y diferencias entre grupos de población, así como explorar la posible relación entre la interacción digital y las experiencias de conexión social.

## Cómo reproducir

El proyecto utiliza Python para procesar los microdatos de la ENBIARE 2021 y generar los resultados del análisis de correlación de Spearman. Las visualizaciones interactivas se desarrollaron en Tableau.

Para reproducir el análisis:

1. Clonar este repositorio.
2. Instalar las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
3. Ejecutar el procesamiento:
   ```bash
   python src/analisis_spearman.py
   ```

Los resultados se guardan en `data/processed/`.

Para consultar las visualizaciones, abrir el archivo `tableau/PIA_Conexion_social_digital.twbx` con Tableau Desktop.

Los datos originales utilizados se encuentran en `data/raw/`.

## Datos

La fuente de información es:

- **Institución:** Instituto Nacional de Estadística y Geografía (INEGI).
- **Encuesta:** Encuesta Nacional de Bienestar Autorreportado (ENBIARE) 2021.
- **Periodo de levantamiento:** 3 de junio al 23 de julio de 2021.
- **Tipo de información:** Microdatos de uso público.

Los datos se utilizarán con fines académicos y se dará el crédito correspondiente a la institución productora.

## Herramientas

- Python para el procesamiento y análisis de datos.
- Tableau para la elaboración de visualizaciones interactivas.
- Git y GitHub para el control de versiones y documentación del proyecto.

## Estado del proyecto

En desarrollo.
