# Conexión social y digital en México

## Propósito

Este proyecto analiza la relación entre la conexión digital y la conexión humana en México, explorando cómo el uso de tecnologías y redes sociales se relaciona con distintas dimensiones del bienestar social.

A partir de los datos de la Encuesta Nacional de Bienestar Autorreportado (ENBIARE) 2021, se busca identificar patrones y diferencias entre grupos de población, así como explorar la posible relación entre la interacción digital y las experiencias de conexión social.

## Pregunta de investigación

¿Qué relación existe entre el uso de plataformas digitales y la satisfacción con las relaciones personales, la vida social y la vida familiar?

## Gran idea

Explorar cómo la frecuencia de uso de plataformas digitales se relaciona con distintas dimensiones de satisfacción social y familiar en México, identificando patrones de asociación y posibles diferencias entre grupos de población, sin asumir que el uso de estas plataformas causa cambios en el bienestar social.

## Estructura del repositorio

```text
conexion-social-digital/
├── data/
│   ├── raw/                 # Microdatos originales de ENBIARE 2021
│   └── processed/           # Archivos Parquet y resultados del análisis
├── docs/
│   ├── reporte_conexion_social_digital.pdf
│   ├── dashboards_tableau.pdf
│   └── modelo_datos_tableau.png
├── results/                 # Resultados de validación de medidas
├── src/                     # Scripts de procesamiento y análisis
├── tableau/                 # Libro de trabajo de Tableau
├── CITATION.cff             # Información para citar el proyecto
├── LICENSE                  # Licencia MIT
├── README.md
└── requirements.txt         # Dependencias de Python con versiones fijadas
```

## Cómo reproducir el proyecto

El proyecto utiliza Python para procesar los microdatos de la ENBIARE 2021, generar archivos Parquet y calcular los resultados del análisis de correlación de Spearman. Las visualizaciones interactivas se desarrollaron en Tableau.

### Requisitos

- Python.
- Dependencias especificadas en `requirements.txt`.
- Tableau Desktop para consultar y explorar las visualizaciones interactivas.

### Instrucciones

1. Clonar este repositorio:

```bash
git clone https://github.com/clarissacontreras/conexion-social-digital.git
cd conexion-social-digital
```

2. Instalar las dependencias:

```bash
python -m pip install -r requirements.txt
```

3. Ejecutar el flujo completo de procesamiento y análisis con un solo comando:

```bash
python src/ejecutar_pipeline.py
```

El flujo ejecuta automáticamente las siguientes tareas:

- Convierte los archivos CSV originales en archivos Parquet con metadatos de procedencia.
- Calcula la matriz y el resumen de correlaciones de Spearman.
- Valida las cinco medidas de frecuencia de uso de plataformas digitales de Tableau mediante pandas.

Los archivos Parquet y los resultados del análisis se guardan en `data/processed/`. Los resultados de la validación se generan en `results/`.

Los datos originales utilizados se encuentran en `data/raw/`.

Para consultar las visualizaciones interactivas, abrir el archivo `tableau/PIA_Conexion_social_digital.twbx` con Tableau Desktop.

## Modelo de datos y visualización

El análisis y las visualizaciones se desarrollaron en Tableau Desktop, como adaptación de la herramienta Power BI contemplada originalmente en la rúbrica.

Los archivos originales de la ENBIARE 2021 incluyen cuatro tablas: TENBIARE, THOGAR, TSDEM y TVIVIENDA. Todas se conservan y convierten a formato Parquet mediante el flujo de procesamiento en Python.

El modelo de datos en Tableau integra estas cuatro tablas mediante relaciones establecidas a partir de campos identificadores compartidos, como FOLIO, VIV_SEL y HOGAR. TENBIARE funciona como tabla principal para el análisis de la frecuencia de uso de plataformas digitales y la satisfacción con las relaciones personales, la vida social y la vida familiar, mientras que las otras tablas complementan la información del hogar, la vivienda y las características sociodemográficas.

Adicionalmente, el libro de trabajo utiliza una fuente de datos independiente:

- **Matriz_Spearman:** contiene los resultados de las correlaciones calculadas previamente con Python y se utiliza exclusivamente para construir la visualización de la matriz de correlaciones. Se mantiene separada del modelo relacional de la ENBIARE.

La matriz de correlaciones utiliza el coeficiente de Spearman para explorar la asociación entre la frecuencia de uso de cinco plataformas digitales (PC2_1 a PC2_5) y tres dimensiones de satisfacción: relaciones personales (PA3_04), vida social (PA3_05) y vida familiar (PA3_06).

Los coeficientes toman valores entre -1 y 1: los valores positivos indican una asociación directa, los negativos una asociación inversa y los cercanos a cero una asociación monotónica débil o inexistente.

Las medidas de frecuencia de uso de plataformas digitales se calcularon en Tableau y se contrastaron con resultados independientes obtenidos mediante pandas. La matriz de correlaciones también se verificó comparando los resultados de Python con los visualizados en Tableau.

Debido a que el análisis utiliza datos de una encuesta transversal correspondiente a 2021, no se requiere una tabla de fechas ni un modelo dimensional temporal.

## Validación de medidas con pandas

Para verificar la consistencia de los indicadores de uso de plataformas digitales presentados en Tableau, se desarrolló un proceso de validación independiente utilizando Python y la biblioteca pandas.

El proceso calcula el porcentaje de personas que reportaron utilizar cada plataforma al menos alguna vez, excluyendo las respuestas correspondientes a «Nunca» y los valores nulos. Posteriormente, compara los resultados obtenidos con los porcentajes presentados en Tableau.

Cada indicador se calcula dividiendo el número de respuestas distintas de «Nunca» entre el total de respuestas válidas de cada plataforma y multiplicando el resultado por 100. Los valores nulos se excluyen del cálculo.

### Resultados de validación

| Plataforma | Porcentaje de uso |
|---|---:|
| Facebook | 61.35 % |
| Twitter | 9.70 % |
| Instagram | 16.87 % |
| WhatsApp/Telegram | 75.43 % |
| TikTok | 10.62 % |

### Definición de las medidas

Las cinco medidas calculan el porcentaje de personas que reportaron utilizar cada plataforma digital al menos alguna vez, considerando como uso las respuestas distintas de «Nunca» y excluyendo los valores nulos.

- **Facebook:** porcentaje de uso de Facebook (PC2_1).
- **Twitter:** porcentaje de uso de Twitter (PC2_2).
- **Instagram:** porcentaje de uso de Instagram (PC2_3).
- **WhatsApp/Telegram:** porcentaje de uso de WhatsApp o Telegram (PC2_4).
- **TikTok:** porcentaje de uso de TikTok (PC2_5).

La unidad de medida es el porcentaje (%).

**Resultado:** las cinco medidas coincidieron con los valores mostrados en Tableau (5 de 5 medidas validadas).

El código de validación se encuentra en `src/validacion_medidas_tableau.py`, y los resultados detallados se generan en `results/validacion_medidas_tableau.csv`.

## Datos

La fuente de información es:

- **Institución:** Instituto Nacional de Estadística y Geografía (INEGI).
- **Encuesta:** Encuesta Nacional de Bienestar Autorreportado (ENBIARE) 2021.
- **Periodo de levantamiento:** 3 de junio al 23 de julio de 2021.
- **Tipo de información:** Microdatos de uso público.

Los datos se utilizan con fines académicos y se reconoce al INEGI como institución productora de la información.

## Documentación y visualizaciones

El proyecto cuenta con los siguientes documentos complementarios:

- [Reporte del proyecto en PDF](docs/reporte_conexion_social_digital.pdf): presenta la pregunta de investigación, metodología, resultados, visualizaciones, conclusiones y limitaciones del análisis.
- [Dashboards de Tableau en PDF](docs/dashboards_tableau.pdf): reúne las tres visualizaciones principales del proyecto.
- [Evidencia del modelo de datos en Tableau](docs/modelo_datos_tableau.png): muestra las relaciones entre las tablas utilizadas en el análisis.

El libro de trabajo interactivo también está disponible en `tableau/PIA_Conexion_social_digital.twbx`.

## Herramientas

- **Python:** procesamiento, transformación y análisis de datos.
- **pandas:** manipulación de datos y validación independiente de medidas.
- **NumPy:** operaciones numéricas.
- **PyArrow:** conversión y almacenamiento de datos en formato Parquet, incluyendo metadatos.
- **Tableau Desktop:** elaboración de visualizaciones interactivas y dashboards.
- **Git y GitHub:** control de versiones, documentación y publicación del proyecto.

## Alcance y limitaciones

El análisis se basa en los microdatos de la ENBIARE 2021, por lo que sus resultados corresponden al contexto y periodo de levantamiento de dicha encuesta.

Las correlaciones de Spearman permiten identificar asociaciones monotónicas entre variables, pero no establecen relaciones causales.

Asimismo, las respuestas autorreportadas reflejan las percepciones de las personas encuestadas y deben interpretarse considerando las características y limitaciones de la fuente de información.

## Buenas prácticas

- Conservar los datos originales en `data/raw/` sin modificarlos directamente.
- Utilizar el flujo automatizado de Python para generar los archivos procesados.
- Mantener las dependencias documentadas y con versiones fijadas en `requirements.txt`.
- Utilizar mensajes de commit claros y descriptivos.
- Documentar los cambios relevantes y conservar los resultados de validación.

## Licencia

Este proyecto se distribuye bajo la licencia **MIT**, especificada en el archivo `LICENSE`.

La licencia permite utilizar, modificar y distribuir el código del proyecto, conservando los avisos de derechos de autor y la licencia correspondiente.

Los microdatos utilizados pertenecen al INEGI y deben respetarse sus condiciones de uso y atribución, independientemente de la licencia del código de este repositorio.

## Cómo citar

Si utilizas este proyecto en un trabajo académico, puedes generar la referencia bibliográfica desde GitHub mediante el botón **Cite this repository**, disponible en la página principal del repositorio.

La información bibliográfica del proyecto se encuentra en el archivo `CITATION.cff`, que permite generar referencias en distintos formatos, como APA y BibTeX.

## Estado del proyecto

Análisis, procesamiento de datos, validación de medidas, visualizaciones y documentación completados.