# Librerias que se importaron
import os
from pyswip import Prolog

# Es laconexion con el archivo .pl
prolog =Prolog()
prolog.consult("habilidades.pl")

# Menu principal
def menu():
	os.system('cls')
	print ("_________________________________________")
	print ("Sistema Experto de Seleccion de Carreras")
	print ("")
	print ("Selecciona una opción ...")
	print ("\t1 - Ver lista de estudiantes")
	print ("\t2 - Ver habilidades de estudiantes")
	print ("\t3 - Seleccion de Carreras")
	print ("\t4 - Cordinador de carreras")
	print ("\t5 - Integrantes")	
	print ("\t0 - salir")
 
while True:
	# Para mostrar el menu
	menu()
 
	# solicituamos una opción al usuario
	opcionMenu = input("inserta un numero valor >> ")
	print("-----------------------------------")
	if opcionMenu=="1":
		print ("\t1 - miguel")
		print ("\t2 - francisco")
		print ("\t2 - javier")
		print ("\t3 - jesus")
		print ("\t4 - alejandra")
		print ("\t5 - roxana")
		print ("\t6 - emmanuel")
		print ("\t7 - rodrigo")
		print ("\t8 - angel")
		print ("\t9 - enrique")
		print ("\t10 - gonzalo")
		print ("\t11 - fatima")
		print ("\t12 - guadalupe")
		print("")
		# Es una consulta para obtener datos de los alumnos 
		result1 =list(prolog.query("alumnos(X)"))
		print(result1)
		print('-------------------------------------------------------------------------------')

		input("Oprima tecla [Enter] para continuar: ")

	elif opcionMenu=="2":
		# Es una consulta pero especificamente para saber si el dato que digitaron esta en el archivo .pl
		# donde devolvera true o false.
		X =input("Escribe un nombre: ")
		result =bool(list(prolog.query("seleccion("+ X +", Y)")))
		# Si devuelve true se ejecuta la segunda consulta y es para sabar la habilidad que tiene o posee el estudiante.
		print('¿ Esta en la lista ?: ', result)
		for dato in prolog.query("seleccion("+ X + ", Y)"):
			print('Es habil en:', dato["Y"])
		print("")
		input("Oprima tecla [Enter] para continuar:")

	elif opcionMenu=="3":
		# Es una consulta pero especificamente para saber si el dato que digitaron esta en el archivo .pl
		# donde devolvera true o false.
		X =input("Escribe un nombre: ")
		result =bool(list(prolog.query("seleccion("+ X +", Y)")))
		print('¿ Esta en la lista ?: ', result)
		# Si devuelve true se ejecuta la segunda consulta y es para sabar la carrera que se le asignara.
		for dato in prolog.query("asignacion("+ X + ", Y)"):
			print('La carrera que seleccion el sistema es:', dato["Y"])
		print("")
		input("Oprima tecla [Enter] para continuar:")

	elif opcionMenu=="4":
		# Es una consulta pero especificamente para saber si el dato que digitaron esta en el archivo .pl
		# donde devolvera true o false.		
		print("OJO: Si son mas de dos palabras se usa el _    Ejemplo(sistemas_computacionales)")
		X =input("Escribe carrera: ")
		result =bool(list(prolog.query("academia("+ X +", Y)")))
		print('¿ Esta en la lista ?: ', result)	
		print("")
		# Si devuelve true se ejecuta la segunda consulta y es para saber quien es el coordinadir de la carrera.
		for dato in prolog.query("profesor_materias("+ X + ", Y, Z)"):
			print(dato["Y"], dato["Z"])
		print("")		
		input("Oprima tecla [Enter] para continuar:")
	
	elif opcionMenu=="5":
		#Integrantes
		print("Miguel G. Tuz Cahum")
		print("Francisco J. Cen Hau")
		print("")
		input("Oprima tecla [Enter] para continuar:")
	elif opcionMenu=="0":
		break
	else:
		print ("")
		input("No se selecciono ninguna opción correcta...\nOprima tecla [Enter] para continuar")


