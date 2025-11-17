def calcular_consumo(power, use_time):
    return power * use_time

#Example of aplpliance
fridge = {
    "name": "Nevera",
    "power": 200,
    "use_time": 5,
    "consumption": 0

}
#Calculo del consumo
fridge["consumption"] = calcular_consumo(fridge["power"], fridge["use_time"])

#Array
appliances = [fridge]

while True:
    operation = input("Ingrese la operacion: (Ingresar, Ver Electrodomesticos, Ver Consumo Total, Salir): " )
    operation = operation.lower()
    
    if operation == "ingresar":
        name = (input("Ingrese el electrodomestico: "))
        if len(name) == 0:
            print("Debes ingresar un nombre")
            continue
        power = float(input("Ingrese la potencia (solo num): "))
        if power <= 0: 
            print("Debe ingresar un numero (positivo)")
            continue
        use_time = float(input("Ingrese el tiempo de uso (solo num): " ))
        if use_time <= 0: 
            print("Debe ingresar un numero (positivo)")
            continue

        newAppliance = {
            "name": name,
            "power": power,
            "use_time": use_time,
            "consumption": 0
        };

        newAppliance["consumption"] = calcular_consumo(newAppliance["power"], newAppliance["use_time"])

        appliances.append(newAppliance)
        print("Electrodomestico añadido")

    elif operation == "ver electrodomesticos":
        for a in appliances: 
            print(f"El/la {a['name']}, de potencia {a['power']}, que se usa {a['use_time']}h al dia, consume {a['consumption']}Wh/dia")
    elif operation == "ver consumo total":
        counterTotal = 0

        for a in appliances: 
            counterTotal += a["consumption"]

        print(f"El consumo total diario por todos los electrodomesticos es {counterTotal}Wh/Dia")
    elif operation == "salir":
        break
    else: 
        print("Ingrese una operacion valida")