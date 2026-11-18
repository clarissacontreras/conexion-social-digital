# Resultados del análisis de correlación de Spearman

## 1. Descripción general

Se realizó un análisis de correlación de Spearman para explorar la relación entre la frecuencia de comunicación mediante cinco plataformas digitales y tres dimensiones de satisfacción personal y social, utilizando microdatos de la ENBIARE 2021.

El análisis comprendió:

- **Observaciones:** 31,166.
- **Variables:** 8.
- **Método:** correlación de rangos de Spearman.
- **Valores faltantes:** no se identificaron valores faltantes en las variables seleccionadas.
- **Ponderación:** cálculo no ponderado.

## 2. Correlación entre plataformas digitales

Se identificaron asociaciones positivas entre las frecuencias de comunicación mediante distintas plataformas.

| Relación | Coeficiente de Spearman |
|---|---:|
| Facebook – WhatsApp/Telegram | 0.585860 |
| Twitter – Instagram | 0.448513 |
| Instagram – TikTok | 0.386516 |

La asociación más alta de estos tres pares se presentó entre Facebook y WhatsApp/Telegram (ρ = 0.586). Esto indica que, en las observaciones analizadas, una mayor frecuencia de comunicación mediante una de estas plataformas tiende a acompañarse de una mayor frecuencia mediante la otra.

Estos resultados sugieren que la comunicación digital mediante distintas plataformas puede coexistir y presentar patrones de frecuencia relacionados.

## 3. Correlación entre plataformas digitales y satisfacción

Se analizaron las asociaciones entre la frecuencia de comunicación digital y las dimensiones de satisfacción consideradas.

| Relación | Coeficiente de Spearman |
|---|---:|
| Facebook – Relaciones personales | 0.082209 |
| WhatsApp/Telegram – Relaciones personales | 0.125060 |
| WhatsApp/Telegram – Vida social | 0.120588 |

Los coeficientes observados son positivos, pero de magnitud débil. Esto indica que existe una asociación monotónica positiva limitada entre la frecuencia de comunicación mediante estas plataformas y las dimensiones de satisfacción correspondientes.

Por lo tanto, los resultados no muestran una asociación fuerte entre la frecuencia de comunicación digital y la satisfacción personal o social en los pares examinados.

## 4. Correlación entre dimensiones de satisfacción

También se identificaron asociaciones positivas entre las tres dimensiones de satisfacción:

| Relación | Coeficiente de Spearman |
|---|---:|
| Relaciones personales – Vida social | 0.521928 |
| Relaciones personales – Vida familiar | 0.457835 |
| Vida social – Vida familiar | 0.464089 |

La asociación más alta se presentó entre la satisfacción con las relaciones personales y la satisfacción con la vida social (ρ = 0.522).

Estos resultados muestran que las dimensiones de satisfacción consideradas presentan una relación positiva moderada entre sí dentro de las observaciones analizadas.

## 5. Hallazgos principales

A partir de los coeficientes examinados, destacan tres observaciones:

1. Las frecuencias de comunicación mediante distintas plataformas digitales presentan asociaciones positivas, especialmente entre Facebook y WhatsApp/Telegram.
2. Las asociaciones entre comunicación digital y satisfacción son positivas, pero débiles en los pares revisados.
3. Las dimensiones de satisfacción personal, social y familiar presentan asociaciones positivas moderadas entre sí.

En conjunto, los resultados permiten explorar la coexistencia de la conexión digital y distintas dimensiones de bienestar social, sin asumir que una necesariamente produce cambios en la otra.

## 6. Limitaciones

- El análisis utiliza datos de la ENBIARE 2021, por lo que describe información correspondiente al periodo de levantamiento de esa encuesta.
- Los coeficientes se calcularon sin aplicar factores de expansión o ponderadores de la encuesta.
- La correlación de Spearman identifica asociaciones monotónicas, pero no establece relaciones causales.
- Los resultados documentados corresponden a los pares de variables revisados y no sustituyen el análisis completo de la matriz.

## 7. Archivo de resultados y reproducción

La matriz completa de correlaciones se encuentra en:

`data/processed/matriz_spearman.csv`

El resumen del número de observaciones y variables se encuentra en:

`data/processed/resumen_spearman.csv`

Para reproducir el análisis desde la carpeta raíz del repositorio:

```bash
pip install -r requirements.txt
python src/analisis_spearman.py
```

El script genera nuevamente los archivos de resultados a partir de los datos originales.