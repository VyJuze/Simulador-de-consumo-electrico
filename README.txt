README — Simulador de Consumo Eléctrico en Python Básico
Descripción del proyecto
Este programa simula el consumo eléctrico diario de dispositivos en un hogar o negocio pequeño. Permite registrar electrodomésticos con su potencia y tiempo de uso, calcular su consumo energético y visualizar el total diario. Está desarrollado en Python básico, sin librerías externas, como solución funcional a un problema cotidiano desde una perspectiva ingenieril.

Objetivo
Desarrollar un programa en Python básico que permita registrar dispositivos eléctricos, simular su uso diario y calcular el consumo energético total, con el fin de ofrecer una solución sencilla y funcional para el monitoreo del consumo eléctrico en hogares o pequeños negocios.

Requisitos
- Tener instalado Python 3.x
- Usar cualquier editor de texto o entorno como VS Code, IDLE, Thonny o Replit

Instrucciones de uso
- Descarga o copia el archivo consumo_electrico.py.
- Abre una terminal o consola en la carpeta donde esté el archivo.
- Ejecuta el programa con el siguiente comando:
python consumo_electrico.py
- Interactúa con el menú escribiendo una de las siguientes operaciones:
- ingresar: Añade un nuevo electrodoméstico.
- ver electrodomesticos: Muestra todos los dispositivos registrados y su consumo diario.
- ver consumo total: Muestra el consumo total diario de todos los dispositivos.
- salir: Finaliza el programa.

Estructura del código
- calcular_consumo(power, use_time): función que calcula el consumo diario en Wh.
- Menú interactivo con validaciones básicas.
- Diccionarios para representar cada dispositivo.
- Lista appliances para almacenar todos los dispositivos registrados.

Fuentes y referencias
- Fórmula de consumo eléctrico: Consumo Electrico(Wh) = Potencia(W) * Tiempo(H)

No se utilizaron librerías externas ni datasets reales.
