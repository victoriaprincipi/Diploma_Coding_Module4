import matplotlib.pyplot as plt

def contar_frecuencias(texto):
    palabras = texto.lower().split()
    frecuencias = {}

    for palabra in palabras:
        frecuencias[palabra] = frecuencias.get(palabra, 0) + 1

    return frecuencias
def main():
    try:
        with open("texto_integradora.txt", "r", encoding="utf-8") as archivo:
            texto = archivo.read()
    except FileNotFoundError:
        print("No se encontró el archivo texto_integradora.txt.")
        return

    frecuencias = contar_frecuencias(texto)
    top10 = sorted(frecuencias.items(), key=lambda x: x[1], reverse=True)[:10]
    palabras = [palabra for palabra, frecuencia in top10]
    valores = [frecuencia for palabra, frecuencia in top10]

    plt.figure(figsize=(10, 6))
    plt.barh(palabras[::-1], valores[::-1], color="steelblue")
    plt.title("Las 10 palabras más frecuentes")
    plt.xlabel("Frecuencia")
    plt.tight_layout()
    plt.savefig("grafico_frecuencias.png", dpi=150, bbox_inches="tight")
    plt.show()


if __name__ == "__main__":
    main()