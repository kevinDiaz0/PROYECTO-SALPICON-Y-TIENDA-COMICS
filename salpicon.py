frutas = [
    {"id": 1, "nombre": "Manzana", "precio": 1500, "cantidad": 10},
    {"id": 2, "nombre": "Banano", "precio": 800, "cantidad": 15},
    {"id": 3, "nombre": "Naranja", "precio": 1000, "cantidad": 20},
    {"id": 4, "nombre": "Pera", "precio": 2500, "cantidad": 12},
    {"id": 5, "nombre": "Uva", "precio": 1200, "cantidad": 8},
    {"id": 6, "nombre": "Kiwi", "precio": 2500, "cantidad": 10},
    {"id": 7, "nombre": "Fresa", "precio": 1800, "cantidad": 18},
    {"id": 8, "nombre": "Mango", "precio": 2200, "cantidad": 9},
    {"id": 9, "nombre": "Piña", "precio": 1400, "cantidad": 14},
    {"id": 10, "nombre": "Sandía", "precio": 3000, "cantidad": 6}
]

#FUNCION PARA OCTENER LOS ATRIBUTOS DE LAS FRUTAS ELEJIDAS POR EL USUARIO
def obtener_nombre_por_id(frutasElejidas):
    for fruta in frutas:
        if fruta['id'] == frutasElejidas:
            return fruta
    return "Fruta no encontrada"

i=True
while(i):
    print("*********************")
    print(" WELCOME TO SALPICON")
    print("*********************")
    print("1.Salpicon")
    resUser = int(input("digite servicio a solicitar: "))
    if resUser == 1:
        cFrutas = int(input("dijite la cantidad de frutas a elegir para su salpicon (Max. 10): "))
        if cFrutas > 0 and cFrutas < 11:
            print("                                                        ")
            for fruta in frutas:
                print(f"ID: {fruta['id']:2} | Nombre: {fruta['nombre']:8} | Precio: ${fruta['precio']:4.2f} | Cantidad: {fruta['cantidad']:3}")
            def eleccionFrutas():
                vlrFrutas = 0   
                frutasOrdenadas=[]
                for i in range(0,cFrutas):
                    print("                                                    ")
                    frutasElejidas = int(input("dijite id de las fruta a elejir: "))
                    oId = obtener_nombre_por_id(frutasElejidas)
                    vlrFrutas += oId["precio"]
                    frutasOrdenadas.append(oId)
                    def frutasdMayor_aMmenor():    
                        mayorA_menor = sorted(frutasOrdenadas, key=lambda x: x["precio"], reverse=True)
                        for fruta in mayorA_menor:
                            print(f"Nombre: {fruta['nombre']:8} | Precio: ${fruta['precio']:4.2f}")
                    def frutaMasBarata():    
                        frutaMayorAmenor = sorted(frutasOrdenadas, key=lambda x: x["precio"])
                        primeraFruta = frutaMayorAmenor[0]
                        print(f"Nombre: {primeraFruta['nombre']:8} | Precio: ${primeraFruta['precio']:4.2f}")    
                    print(f"{oId["nombre"]} agregada exitosamente, Precio: {oId["precio"]}")
                res = int(input("Desea modificar las frutas seleccionadas?\n 1.Si \n 2.No\n"))
                if res != 2:
                    eleccionFrutas()
                print("***SALPICON CREADO EXITOSAMENTE***")
                print("   Valor total Salpicon: " , vlrFrutas)
                respuestaMaM = int(input("desea imprimir las frutas seleccionadas de mayor a menor??\n 1.Si\n2.No\n "))
                if respuestaMaM != 2:
                    print("-----FRUTAS DE MAYOR A MENOR-----")
                    frutasdMayor_aMmenor()
                respuestaMaM = int(input("desea imprimir la fruta mas barata??\n 1.Si\n2.No\n "))
                if respuestaMaM != 2:
                    print("-----FRUTA MAS BARATA-----")
                    frutaMasBarata()
                
            eleccionFrutas()  
            res = int(input("Desea solicitar otro servicio?\n 1.Si\n2.No\n "))       
            if res != 1:
                print("GRACIAS POR TU COMPRA, VUELVE PRONTO!!")
                i=False
        else:
            print("Digite un numero dentro del rango")        
    else:
        print("Digite la opcion correcta")
