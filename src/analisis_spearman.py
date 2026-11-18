from pathlib import Path
import pandas as pd


# Rutas del proyecto
ROOT = Path(__file__).resolve().parents[1]
INPUT_FILE = ROOT / "data" / "raw" / "TENBIARE.csv"
OUTPUT_DIR = ROOT / "data" / "processed"

# Variables utilizadas en el análisis
VARIABLES = [
    "PC2_1",
    "PC2_2",
    "PC2_3",
    "PC2_4",
    "PC2_5",
    "PA3_04",
    "PA3_05",
    "PA3_06",
]


def main():
    # Leer los datos originales
    df = pd.read_csv(
        INPUT_FILE,
        encoding="utf-8-sig",
        low_memory=False
    )

    # Verificar que existan todas las variables
    faltantes = [col for col in VARIABLES if col not in df.columns]

    if faltantes:
        raise ValueError(
            f"No se encontraron estas variables: {faltantes}"
        )

    # Seleccionar las variables y calcular Spearman
    datos = df[VARIABLES]

    if datos.isna().any().any():
        raise ValueError(
            "Existen valores faltantes en las variables seleccionadas."
        )

    matriz = datos.corr(method="spearman")

    # Crear carpeta de resultados si no existe
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Guardar matriz de correlaciones
    matriz.to_csv(
        OUTPUT_DIR / "matriz_spearman.csv",
        encoding="utf-8-sig",
        float_format="%.12f"
    )

    # Guardar número de observaciones utilizadas
    resumen = pd.DataFrame({
        "indicador": ["observaciones", "variables"],
        "valor": [len(datos), len(VARIABLES)]
    })

    resumen.to_csv(
        OUTPUT_DIR / "resumen_spearman.csv",
        index=False,
        encoding="utf-8-sig"
    )

    print("Análisis de Spearman completado.")
    print(f"Observaciones: {len(datos):,}")
    print(f"Variables: {len(VARIABLES)}")
    print("\nMatriz de correlaciones:")
    print(matriz.round(6).to_string())
    print(f"\nArchivos guardados en: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()