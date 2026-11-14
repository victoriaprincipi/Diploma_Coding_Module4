# Mi analizador de frecuencias
El script lee texto_integradora.txt y cuenta la frecuencia de cada palabra.
Las mayúsculas y minúsculas se cuentan como la misma palabra.
Si el archivo no existe, muestra un mensaje.
Genera y guarda un gráfico de las 10 palabras más frecuentes en grafico_frecuencias.png.
Requiere Python y las bibliotecas matplotlib y pytest.
Para instalar las bibliotecas: `python -m pip install matplotlib pytest`.
Desde la terminal, ubicada en esta carpeta, ejecutar: `python analizador.py`.
Para ejecutar las tres pruebas automáticas: `python -m pytest test_analizador.py`.