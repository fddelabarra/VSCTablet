mi_ataque = int(input())
mi_vida = int(input())
evento = input()

while evento != "FIN":
    if evento == "cartel":
        cartel = input()
        if cartel == "->":
            print("Debo ir a la izquierda! no sere enganado")
        elif cartel == "<-":
            print("Debo ir a la derecha! no sere enganado")
        elif cartel == "<->":
            print("Debo ir hacia delante!")
        else:
            print("Me he equivocado! debo volver")
    elif evento == "asalto":
        num_soldados = int(input())
        for i in range(num_soldados):
            ataque_soldado = int(input())
            if mi_vida > 0:
                if ataque_soldado > mi_ataque:
                    mi_vida -= ataque_soldado - mi_ataque
        if mi_vida > 0:
            print("Logre superar el asalto!, seguire avanzando")
        else:
            print("Tal y como se menciona, nadie que haya entrado ha vuelto a salir...")
    if mi_vida > 0:
        evento = input()
    else:
        evento = "FIN"