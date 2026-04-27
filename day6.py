pokedex = []

print("=== Pokedex v1.0 ===")
print("1. ver todo los pokemon")
print("2.capturar pokemon")
print("3. buscar pokemon por nombre")
print("4. salir")


while True:
    opcion = input("\nElige una opcion 1-4:")
    
    if opcion =="1":
        print("\n=== TU POKEDEX ===")
        if len(pokedex) == 0:
            print("aun no capturas ningun pokemon")
        else:
            for i, poke in enumerate(pokedex, 1):
                print(f"{i}.{poke['nombre']} | tipo: {poke['tipo']} | hp:{poke['ataque']}")
    
    elif opcion == "2":
        print("\n--- capturando pokemon ---")
        nombre = input("nombre:")
        tipo = input("tipo")
        hp = int(input("hp:"))
        ataque = int(input("ataque"))
        
        nuevo_pokemon ={
            "nombre": nombre,
            "tipo": tipo,
            "hp": hp,
            "ataque": ataque
        } 
        
        pokedex.append(nuevo_pokemon)
        print("{nombre} fue agfregado a la pokedex")
        
        
    elif opcion == "3":
        if len(pokedex) == 0:
            print("tu pokedex esta vacia")
        else:
            buscar = input("nombre del pokemon a buscar:")
            encontrado = False 
            
            for poke in pokedex:
                if poke['nombre'].lower() == buscar.lower():
                    print(f"\nencontrado")
                    print(f"nombre: {poke['nombre']}")
                    print(f"tipo: {poke['tipo']}")
                    print(f"hp: {poke['hp']}")
                    print(f"ataque: {poke['ataque']}")
                    encontrado = True
                    break
            if not encontrado:
                print("ese pokemon no esta en tu pokedex")
                
                
    elif opcion == "4":
        print("guardando pokedex... Hasta la proxima, entrenador")
        break
    
    else:
        print("opcion no valida. usa 1, 2, 3, o 4")
        