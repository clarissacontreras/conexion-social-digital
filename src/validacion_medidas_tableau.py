
from pathlib import Path

import pandas as pd


# Rutas del proyecto
ROOT = Path(__file__).resolve().parents[1]
INPUT_FILE = ROOT / "data" / "raw" / "TENBIARE.csv"
OUTPUT_DIR = ROOT / "results"

# Variables de frecuencia y porcentajes mostrados en Tableau
PLATAFORMAS = {
    "Facebook": {
        "variable": "PC2_1",
        "porcentaje_tableau": 61.35
    },
    "Twitter": {
        "variable": "PC2_2",
        "porcentaje_tableau": 9.70
    },
    "Instagram": {
        "variable": "PC2_3",
        "porcentaje_tableau": 16.87
    },
    "WhatsApp/Telegram": {
        "variable": "PC2_4",
        "porcentaje_tableau": 75.43
    },
    "TikTok": {
        "variable": "PC2_5",
        "porcentaje_tableau": 10.62
    }
}


def main():
    # Leer la base de datos original
    df = pd.read_csv(
        INPUT_FILE,
        encoding="utf-8-sig",
        low_memory=False
    )

    resultados = []

    # Calcular y validar cada plataforma
    for plataforma, datos in PLATAFORMAS.items():

        variable = datos["variable"]
        porcentaje_tableau = datos["porcentaje_tableau"]

        respuestas = pd.to_numeric(
            df[variable],
            errors="coerce"
        )

        respuestas_validas = respuestas.dropna()

        total = len(respuestas_validas)

        usuarios = (respuestas_validas != 1).sum()

        porcentaje = (usuarios / total) * 100

        coincide = round(porcentaje, 2) == porcentaje_tableau

        resultados.append({
            "plataforma": plataforma,
            "variable": variable,
            "total_observaciones": total,
            "usuarios": usuarios,
            "porcentaje_pandas": porcentaje,
            "porcentaje_tableau": porcentaje_tableau,
            "coincide": coincide
        })

    # Crear tabla de resultados
    resultados_df = pd.DataFrame(resultados)

    # Mostrar resultados
    print("VALIDACIÓN DE MEDIDAS DE TABLEAU CON PANDAS")
    print("=" * 65)

    print(
        resultados_df.to_string(
            index=False,
            formatters={
                "porcentaje_pandas": "{:.4f}%".format,
                "porcentaje_tableau": "{:.2f}%".format
            }
        )
    )

    # Guardar resultados
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    output_file = OUTPUT_DIR / "validacion_medidas_tableau.csv"

    resultados_df.to_csv(
        output_file,
        index=False,
        encoding="utf-8-sig",
        float_format="%.6f"
    )

    # Resumen de validación
    validadas = resultados_df["coincide"].sum()
    total_medidas = len(resultados_df)

    print("\nRESUMEN")
    print(f"Medidas validadas: {validadas}/{total_medidas}")

    if validadas == total_medidas:
        print("Todas las medidas coinciden con Tableau.")
    else:
        print("Se encontraron diferencias que deben revisarse.")

    print(f"\nResultados guardados en: {output_file}")


if __name__ == "__main__":
    main()
