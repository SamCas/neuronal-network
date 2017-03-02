'''
 Universidad Autonoma de Nuevo Leon
 Fac. de Ingenieria Mecanica y Electrica
 Administracion y Sistemas
 Ingenieria en Tecnologias de Software
 
 Programacion de Sistemas Adaptativos
 Redes neuronales: Perceptron
 Programa un perceptron para que clasifique el suelo en apto o no apto para la agricultura
'''

#Esqueleto perceptron

'''
  Recibe: pesos   - lista con pesos del perceptron
          entrada - lista con las caracteristicas del ejemplo a procesar
  Salida: suma de la multiplicacion de cada peso por cada caracteristica
'''
#def funcion_nucleo(pesos, entrada):
#PROGRAMA AQUI LA FUNCION DE NUCLEO (QUITA EL "#" DE LA LINEA ANTERIOR)

'''
  Recibe: resultado_nucleo - valor que representa el resultado de la funcion de nucleo (g(X))
  Salida: devuelve 1 si resultado_nucleo es mayor o igual a cero; en caso contrario, devuelve un 0
'''
#def funcion_activacion(resultado_nucleo):
#PROGRAMA AQUI LA FUNCION DE ACTIVACION (QUITA EL "#" DE LA LINEA ANTERIOR)

		
max_iter=50
tasa_aprendizaje=0.1
pesos=[1,0,0,0,0,0,0]
entradas=[[[-1,1,0,1,0,0,0], 1], [[-1,1,0,1,1,0,0], 1], [[-1,1,0,1,0,1,0], 1] 
, [[-1,1,1,0,0,1,1], 1], [[-1,1,1,1,1,0,0], 1], [[-1,1,0,0,0,1,1], 1], [[-1,1,0,0,0,1,0], 0] 
, [[-1,0,1,1,1,0,1], 1], [[-1,0,1,1,0,1,1], 0], [[-1,0,0,0,1,1,0], 0], [[-1,0,1,0,1,0,1], 0], 
[[-1,0,0,0,1,0,1], 0], [[-1,0,1,1,0,1,1], 0], [[-1,0,1,1,1,0,0], 0]]

iter=0
pincorrectos=1.0

#(Activa este codigo cuando ya tengas la implementacion)
#Mientras que el porcentaje de entradas incorrectas sea mayor al 20% y el num. de iteraciones sea menor a 50
#while(pincorrectos>0.2 and iter<max_iter):

	#incorrectos=0
	

	#AQUI VA EL CODIGO PARA CALCULAR LA SALIDA (y)
	
		#if y!=d: #Checa que esta linea esta mas identada que el resto (cuidado ¡!)
		#	incorrectos=incorrectos+1
		#	print("ACTUALIZANDO PESOS")
			#AQUI VA EL CODIGO PARA ACTUALIZAR LOS PESOS

	#pincorrectos=incorrectos*1.0/len(entradas) #Calculamos el porcentaje de entradas procesadas incorrectamente
	#print(str(pincorrectos*100)+"% de entradas procesadas incorrectamente")
	#iter=iter+1