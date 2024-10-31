import turtle

# dibuja un triángulo dado un conjunto de puntos, un color y un objeto Turtle.
def dibujarTriangulo(puntos, color, miTortuga):
    # color de relleno del triángulo
    miTortuga.fillcolor(color)
    # lápiz a la primera coordenada del triángulo sin dejar rastro
    miTortuga.up()
    miTortuga.goto(puntos[0][0], puntos[0][1])
    # Baja el lápiz para empezar a dibujar
    miTortuga.down()
    # rellenar la figura con el color especificado
    miTortuga.begin_fill()
    # triángulo conectando los tres puntos dados
    miTortuga.goto(puntos[1][0], puntos[1][1])
    miTortuga.goto(puntos[2][0], puntos[2][1])
    miTortuga.goto(puntos[0][0], puntos[0][1])
    # fin del relleno del triángulo
    miTortuga.end_fill()

# Esta función obtiene el punto medio entre dos puntos dados.
def obtenerMitad(p1, p2):
    # Calcula las coordenadas del punto medio en el eje X e Y
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)

# Función recursiva para crear el triángulo de Sierpinski.
# Cada nivel de recursión reduce el grado y divide el triángulo en partes más pequeñas.
def sierpinski(puntos, grado, miTortuga):
    # Definimos una lista de colores para cada nivel de profundidad
    colormap = ['purple', 'cyan', 'lime', 'pink', 'gold', 'orange', 'aqua']
    # Dibuja un triángulo con el color correspondiente al grado de profundidad actual
    dibujarTriangulo(puntos, colormap[grado], miTortuga)
    
    # Si el grado es mayor que 0, continuamos dividiendo el triángulo en subtriángulos
    if grado > 0:
        # Llamada recursiva para el triángulo superior izquierdo
        sierpinski([puntos[0], 
                    obtenerMitad(puntos[0], puntos[1]), 
                    obtenerMitad(puntos[0], puntos[2])],
                   grado - 1, miTortuga)
        
        # Llamada recursiva para el triángulo superior derecho
        sierpinski([puntos[1], 
                    obtenerMitad(puntos[0], puntos[1]), 
                    obtenerMitad(puntos[1], puntos[2])],
                   grado - 1, miTortuga)
        
        # Llamada recursiva para el triángulo inferior
        sierpinski([puntos[2], 
                    obtenerMitad(puntos[2], puntos[1]), 
                    obtenerMitad(puntos[0], puntos[2])],
                   grado - 1, miTortuga)

# Función principal que inicializa la pantalla y configura los parámetros iniciales.
def main():
    # Crea el objeto Turtle para dibujar
    miTortuga = turtle.Turtle()
    # Crea la ventana donde se visualizará el dibujo
    miVentana = turtle.Screen()
    
    # Define los puntos del triángulo inicial, modificados para cambiar la forma del triángulo
    misPuntos = [[-120, -80], [0, 120], [120, -80]]
    # Llama a la función sierpinski para comenzar a dibujar el triángulo de Sierpinski
    sierpinski(misPuntos, 3, miTortuga)
    
    # Mantiene la ventana abierta hasta que se haga clic
    miVentana.exitonclick()

# Llama a la función principal para ejecutar el programa
main()
