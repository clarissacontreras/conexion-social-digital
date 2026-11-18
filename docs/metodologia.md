
# Metodología del análisis de correlación

## Fuente de datos

El análisis utiliza los microdatos de la Encuesta Nacional de Bienestar Autorreportado (ENBIARE) 2021, publicada por el Instituto Nacional de Estadística y Geografía (INEGI).

El archivo de entrada es `TENBIARE.csv`, ubicado en `data/raw/`.

## Variables analizadas

Se seleccionaron ocho variables de la base de datos:

| Variable | Descripción |
|---|---|
| PC2_1 | Frecuencia de uso de Facebook |
| PC2_2 | Frecuencia de uso de Twitter |
| PC2_3 | Frecuencia de uso de Instagram |
| PC2_4 | Frecuencia de uso de WhatsApp/Telegram |
| PC2_5 | Frecuencia de uso de TikTok |
| PA3_04 | Satisfacción personal |
| PA3_05 | Satisfacción con las amistades |
| PA3_06 | Satisfacción familiar |

## Procedimiento

1. Se importó el archivo original `TENBIARE.csv` mediante pandas.
2. Se seleccionaron las ocho variables de interés.
3. Se verificó la ausencia de valores faltantes en las variables seleccionadas.
4. Se calculó la matriz de correlación mediante el coeficiente de Spearman.
5. Se exportaron los resultados en formato CSV para su consulta y reutilización.

## Método estadístico

Se utilizó el coeficiente de correlación de Spearman, una medida no paramétrica que permite evaluar la asociación monotónica entre dos variables.

Los coeficientes se encuentran entre -1 y 1:

- Valores cercanos a 1 indican una asociación positiva.
- Valores cercanos a -1 indican una asociación negativa.
- Valores cercanos a 0 indican una asociación monotónica débil o inexistente.

## Resultados generados

El análisis utiliza 31,166 observaciones y ocho variables.

Los archivos generados se guardan en `data/processed/`:

- `matriz_spearman.csv`: matriz de correlaciones.
- `resumen_spearman.csv`: número de observaciones y variables utilizadas.

## Reproducción

Desde la carpeta raíz del repositorio, ejecutar:

```bash
pip install -r requirements.txt
python src/analisis_spearman.py
```

El procedimiento genera nuevamente los archivos de resultados sin modificar los datos originales.