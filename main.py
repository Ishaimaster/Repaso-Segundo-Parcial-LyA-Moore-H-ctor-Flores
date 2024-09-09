from Moore import MooreMachine

machine = MooreMachine()

# Entrada con separadores '&'
input_data ="Hector Flores&53497769&99525127-k&ishaiflores10@gmail.com&09/09/25&23:12PM&Hola,"

input_data1 = "Johny Bravo Asturias Vasquez&Esto esta mal;&46110238&215233125-9&ejemplo@domain.edu.gt&12/12/12&19:22PM"

input_data2 = "Juan&Probando maquina de moore.&53304760&08712-2&est@url.edu.ch&01/03/95&12:59AM"

#Para añadir una cadena,se instancia un string y luego se guarda el resultado llamando a la funcion machine.process(ejemplo)
result = machine.process(input_data)

#Luego, se inicializa un ciclo para imprimir los resultados, similiar al ejemplo de abajo
for res in result:
    print(res)

print("---------------------------------------------------------------")

result = machine.process(input_data1)

for res1 in result:
    print(res1)

print("---------------------------------------------------------------")

result = machine.process(input_data2)

for res2 in result:
    print(res2)