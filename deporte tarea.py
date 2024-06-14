equipo1 = input("Ingresa el nombre del primer equipo: ")
equipo2 = input("Ingresa el nombre del segundo equipo: ")

goles1 = int(input(f"Ingresa la cantidad de goles de {equipo1}: "))
goles2 = int(input(f"Ingresa la cantidad de goles de {equipo2}: "))

print("\nResultados del partido:")
print(f"{equipo1}: {goles1}")
print(f"{equipo2}: {goles2}")

if goles1 > goles2:
  print(f"\n{equipo1} ganó el partido!")
elif goles2 > goles1:
  print(f"\n{equipo2} ganó el partido!")
else:
  print("\nEl partido terminó en empate!")