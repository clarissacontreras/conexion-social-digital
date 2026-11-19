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

3. Ejecutar el análisis de Spearman:

   ```bash
   python src/analisis_spearman.py
   ```

4. Ejecutar la validación de las medidas de Tableau con pandas:

   ```bash
   python src/validacion_medidas_tableau.py
   ```

Los resultados del análisis de Spearman se guardan en `data/processed/`, mientras que los resultados de la validación se generan en `results/`.

Para consultar las visualizaciones, abrir el archivo `tableau/PIA_Conexion_social_digital.twbx` con Tableau Desktop.

Los datos originales utilizados se encuentran en `data/raw/`.

## Validación de medidas con pandas

Para verificar la consistencia de los indicadores de uso de plataformas digitales presentados en Tableau, se desarrolló un proceso de validación independiente utilizando Python y la biblioteca pandas.

El proceso calcula el porcentaje de personas que reportaron utilizar cada plataforma al menos alguna vez, excluyendo las respuestas correspondientes a «Nunca» y los valores nulos. Posteriormente, compara los resultados obtenidos con los porcentajes presentados en Tableau.

Se validaron cinco indicadores:

| Plataforma | Porcentaje de uso |
|---|---:|
| Facebook | 61.35 % |
| Twitter | 9.70 % |
| Instagram | 16.87 % |
| WhatsApp/Telegram | 75.43 % |
| TikTok | 10.62 % |

**Resultado:** las cinco medidas coincidieron con los valores mostrados en Tableau (5 de 5 medidas validadas).

El código de validación se encuentra en `src/validacion_medidas_tableau.py`, y los resultados detallados se generan en `results/validacion_medidas_tableau.csv`.

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
