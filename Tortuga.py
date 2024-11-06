import turtle
# PROGRAMA SONY GOMEZ ENRIQUE GONZALEZ 31456812 SONY GOMEZ 31268878

# triángulo dado un conjunto de vértices, un color y un objeto Turtle.
def dibujar_triangulo(vertices, color, tortuga):
    # color de relleno del triángulo
    tortuga.fillcolor(color)
    # lápiz para moverlo al primer vértice sin dibujar
    tortuga.up()
    tortuga.goto(vertices[0][0], vertices[0][1])
    # lápiz para comenzar a dibujar
    tortuga.down()
    # relleno del triángulo
    tortuga.begin_fill()
    # triángulo conectando los tres vértices
    tortuga.goto(vertices[1][0], vertices[1][1])
    tortuga.goto(vertices[2][0], vertices[2][1])
    tortuga.goto(vertices[0][0], vertices[0][1])
    # fin del relleno del triángulo
    tortuga.end_fill()

# Calcula el punto medio entre dos puntos dados.
def obtener_punto_medio(punto1, punto2):
    # Calcula las coordenadas del punto medio en el eje X e Y
    return ((punto1[0] + punto2[0]) / 2, (punto1[1] + punto2[1]) / 2)

# Función recursiva para crear el triángulo de Sierpinski.
# Cada nivel de recursión reduce la profundidad y subdivide el triángulo en partes más pequeñas.
def sierpinski(vertices, profundidad, tortuga):
    # lista de colores para cada nivel de profundidad
    colores = ['#8A2BE2', '#5F9EA0', '#FF4500', '#2E8B57', '#DAA520', '#FF6347', '#4682B4']
    # triángulo con el color correspondiente al nivel de profundidad actual
    dibujar_triangulo(vertices, colores[profundidad], tortuga)
    
    # Si la profundidad es mayor que 0, continúa subdividiendo el triángulo
    if profundidad > 0:
        # Llamada recursiva para el triángulo superior izquierdo
        sierpinski([vertices[0], 
                    obtener_punto_medio(vertices[0], vertices[1]), 
                    obtener_punto_medio(vertices[0], vertices[2])],
                   profundidad - 1, tortuga)
        
        # Llamada recursiva para el triángulo superior derecho
        sierpinski([vertices[1], 
                    obtener_punto_medio(vertices[0], vertices[1]), 
                    obtener_punto_medio(vertices[1], vertices[2])],
                   profundidad - 1, tortuga)
        
        # Llamada recursiva para el triángulo inferior
        sierpinski([vertices[2], 
                    obtener_punto_medio(vertices[2], vertices[1]), 
                    obtener_punto_medio(vertices[0], vertices[2])],
                   profundidad - 1, tortuga)

# Función principal que inicializa la pantalla y configura los parámetros iniciales.
def main():
    # Crea el objeto Turtle para dibujar
    tortuga = turtle.Turtle()
    # ventana donde se visualizará el dibujo
    ventana = turtle.Screen()
    
    # Define los vértices del triángulo inicial para la forma deseada
    vertices_iniciales = [[-120, -80], [0, 120], [120, -80]]
    # Llama a la función sierpinski para comenzar a dibujar el triángulo de Sierpinski
    sierpinski(vertices_iniciales, 3, tortuga)
    
    # ventana abierta hasta que se haga clic
    ventana.exitonclick()

main()
