from pathlib import Path
from datetime import datetime, timezone
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq


# Rutas del proyecto
ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = ROOT / "data" / "raw"
OUTPUT_DIR = ROOT / "data" / "processed"

# Archivos originales de ENBIARE 2021
ARCHIVOS = [
    "TENBIARE",
    "THOGAR",
    "TSDEM",
    "TVIVIENDA",
]


def convertir_archivo(nombre):
    archivo_csv = RAW_DIR / f"{nombre}.csv"
    archivo_parquet = OUTPUT_DIR / f"{nombre}.parquet"

    if not archivo_csv.exists():
        raise FileNotFoundError(
            f"No se encontró el archivo: {archivo_csv}"
        )

    # Leer datos conservando los tipos identificados
    df = pd.read_csv(
        archivo_csv,
        encoding="utf-8-sig",
        low_memory=False
    )

    # Convertir a tabla Arrow
    tabla = pa.Table.from_pandas(
        df,
        preserve_index=False
    )

    # Agregar metadatos de procedencia
    metadatos = {
        b"fuente": b"INEGI",
        b"encuesta": b"ENBIARE 2021",
        b"archivo_original": archivo_csv.name.encode("utf-8"),
        b"periodo_recoleccion": b"3 de junio al 23 de julio de 2021",
        b"descripcion": (
            b"Microdatos originales de uso publico "
            b"de la ENBIARE 2021"
        ),
        b"codificacion_original": b"UTF-8 con BOM",
        b"fecha_conversion_utc": (
            datetime.now(timezone.utc)
            .isoformat()
            .encode("utf-8")
        ),
    }

    esquema = tabla.schema.with_metadata(metadatos)
    tabla = tabla.cast(esquema)

    # Guardar Parquet
    pq.write_table(
        tabla,
        archivo_parquet,
        compression="snappy"
    )

    print(f"\nArchivo generado: {archivo_parquet.name}")
    print(f"Filas: {tabla.num_rows:,}")
    print(f"Columnas: {tabla.num_columns}")
    print(f"Tamaño: {archivo_parquet.stat().st_size:,} bytes")


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    for nombre in ARCHIVOS:
        convertir_archivo(nombre)

    print("\nConversión de los cuatro archivos completada.")


if __name__ == "__main__":
    main()
