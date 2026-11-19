
from pathlib import Path
import subprocess
import sys


# Ruta principal del proyecto
ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"

# Scripts que se ejecutarán en orden
SCRIPTS = [
    "convertir_parquet.py",
    "analisis_spearman.py",
    "validacion_medidas_tableau.py",
]


def main():
    for nombre in SCRIPTS:
        archivo = SRC / nombre

        print(f"\n{'=' * 60}")
        print(f"Ejecutando: {nombre}")
        print("=" * 60)

        subprocess.run(
            [sys.executable, str(archivo)],
            cwd=ROOT,
            check=True
        )

    print("\nFlujo de trabajo completado correctamente.")


if __name__ == "__main__":
    main()
