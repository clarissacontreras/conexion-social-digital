# Metodología del análisis de correlación

## 1. Fuente de datos

El análisis utiliza los microdatos de la **Encuesta Nacional de Bienestar Autorreportado (ENBIARE) 2021**, publicada por el Instituto Nacional de Estadística y Geografía (INEGI).

- **Institución:** Instituto Nacional de Estadística y Geografía (INEGI).
- **Encuesta:** ENBIARE 2021.
- **Periodo de levantamiento:** 3 de junio al 23 de julio de 2021.
- **Archivo utilizado:** `TENBIARE.csv`.
- **Ubicación:** `data/raw/`.
- **Tipo de información:** microdatos de uso público.

## 2. Variables analizadas

Se seleccionaron ocho variables de la base de datos para explorar la relación entre la comunicación mediante plataformas digitales y distintas dimensiones de satisfacción.

| Código | Descripción |
|---|---|
| `PC2_1` | Frecuencia de comunicación mediante Facebook |
| `PC2_2` | Frecuencia de comunicación mediante Twitter |
| `PC2_3` | Frecuencia de comunicación mediante Instagram |
| `PC2_4` | Frecuencia de comunicación mediante WhatsApp o Telegram |
| `PC2_5` | Frecuencia de expresión mediante TikTok |
| `PA3_04` | Satisfacción con las relaciones personales |
| `PA3_05` | Satisfacción con la vida social (amistades) |
| `PA3_06` | Satisfacción con la vida familiar |

Las descripciones se documentaron tomando como referencia los materiales de la ENBIARE 2021 publicados por el INEGI.

## 3. Escalas de medición

### 3.1. Frecuencia de comunicación digital

Las variables `PC2_1` a `PC2_5` utilizan una escala ordinal de cinco categorías:

| Código | Categoría |
|---:|---|
| 1 | Nunca |
| 2 | Rara vez |
| 3 | Alguna vez |
| 4 | Con frecuencia |
| 5 | Con mucha frecuencia |

Estas preguntas hacen referencia a la frecuencia con que la persona se expresó o comunicó mediante las plataformas correspondientes durante la semana anterior a la entrevista.

### 3.2. Satisfacción

Las variables `PA3_04`, `PA3_05` y `PA3_06` utilizan una escala numérica de 0 a 10:

- **0:** Totalmente insatisfecho(a).
- **10:** Totalmente satisfecho(a).

Los valores intermedios representan los niveles de satisfacción entre ambos extremos.

## 4. Procedimiento de procesamiento

El procesamiento se realiza mediante un script de Python ubicado en `src/analisis_spearman.py`.

El procedimiento comprende las siguientes etapas:

1. Lectura del archivo original `TENBIARE.csv` mediante la biblioteca pandas.
2. Selección de las ocho variables de interés.
3. Verificación de la existencia de las variables y de los valores faltantes.
4. Cálculo de la matriz de correlación mediante el método de Spearman.
5. Exportación de los resultados en formato CSV.

En la ejecución verificada se utilizaron **31,166 observaciones y ocho variables**. No se encontraron valores faltantes en las variables seleccionadas.

## 5. Método estadístico

Se utilizó el coeficiente de correlación de rangos de Spearman, una medida no paramétrica que permite evaluar la asociación monotónica entre dos variables.

Los coeficientes se encuentran entre -1 y 1:

- **Cercano a 1:** asociación positiva.
- **Cercano a -1:** asociación negativa.
- **Cercano a 0:** asociación monotónica débil o inexistente.

El análisis permite explorar asociaciones entre la frecuencia de comunicación digital y las dimensiones de satisfacción consideradas. Sin embargo, una correlación no demuestra causalidad.

### Consideración sobre la ponderación

El cálculo reproducido mediante pandas utiliza las observaciones sin aplicar factores de expansión o ponderadores de la encuesta. Por lo tanto, los coeficientes obtenidos corresponden a un análisis no ponderado y no deben interpretarse como estimaciones ponderadas de la población mexicana.

## 6. Resultados generados

Los resultados se almacenan en `data/processed/`:

| Archivo | Contenido |
|---|---|
| `matriz_spearman.csv` | Matriz de correlaciones entre las ocho variables. |
| `resumen_spearman.csv` | Número de observaciones y variables utilizadas. |

Los coeficientes se exportan con doce decimales para conservar precisión numérica.

## 7. Reproducción del análisis

Para reproducir el procedimiento desde la carpeta raíz del repositorio, se requiere Python y las dependencias especificadas en `requirements.txt`.

Instalar las dependencias:

```bash
pip install -r requirements.txt
```

Ejecutar el análisis:

```bash
python src/analisis_spearman.py
```

El script genera nuevamente los archivos de resultados en `data/processed/`, sin modificar los datos originales.

## 8. Fuentes y referencias

- Instituto Nacional de Estadística y Geografía (INEGI). [Encuesta Nacional de Bienestar Autorreportado (ENBIARE) 2021](https://www.inegi.org.mx/programas/enbiare/2021/).
- INEGI. [Catálogo de la ENBIARE 2021 en la Red Nacional de Metadatos](https://www.inegi.org.mx/rnm/index.php/catalog/730).
- INEGI. [Materiales relacionados de la ENBIARE 2021](https://www.inegi.org.mx/rnm/index.php/catalog/730/related-materials).

Los datos se utilizan con fines académicos, reconociendo al INEGI como institución productora.