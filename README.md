# Calcanim
Este es un repositorio donde encontrarás todos los códigos usados para generar las animaciones de la lista de reproducción Calcanim de nuestro canal de YouTube [Animathica](https://www.youtube.com/channel/UCzkyH2bxpesubzc87VxqDiA). Las animaciones están hechas con [Manim](https://github.com/3b1b/manim).

¡Te invitamos a descargar y modificar nuestros archivos! Para que puedas generar tus videos después de modificar un archivo, será necesario que tengas una instalación completa y estable de Manim. Te recomendamos los siguientes tutoriales:

### Windows:
  - https://www.youtube.com/watch?v=ZltiKHFWmv8 
  - https://www.youtube.com/watch?v=M8PNyubthVE&t=845s&ab_channel=TheLazyAZ
  - https://manim.readthedocs.io/en/latest/installation/windows.html
### Linux:
  - https://www.youtube.com/watch?v=z_WJaHYH66M
  - https://manim.readthedocs.io/en/latest/installation/linux.html
### macOS:
  - https://www.youtube.com/watch?v=uZj_GQc6pN4
  - http://bhowell4.com/manic-install-tutorial-for-mac/
  
Para que nuestros archivos se puedan ejecutar bien, es necesario que instales la **última versión de Manim**. Además, en el archivo *tex_template.tex* en la carpeta *manimlib*, debes modificar el paquete `babel` de `english` a `spanish`.

Si lo prefieres, puedes usar esta aplicación en línea que te permitirá generar tus videos: 
https://eulertour.com/gallery

# Temario
## Introducción al cálculo multivariable:
  - Motivación, ¿de donde sale la necesidad de utilizar funciones de múltiples variables?

## Espacios vectoriales:
  - [Operaciones con vectores](https://www.youtube.com/watch?v=FYrhEXUZR2M) ([operaciones.py](https://github.com/animathica/calcanim/blob/master/Espacios%20vectoriales/operaciones.py))
  - [Conmutatividad con vectores](https://www.youtube.com/watch?v=D0vHXaN5VyU) ([conmutatividad.py](https://github.com/animathica/calcanim/blob/master/Espacios%20vectoriales/conmutatividad.py))
  - [Asociatividad de vectores](https://www.youtube.com/watch?v=7rZmyzy6DJo) ([asociatividad.py](https://github.com/animathica/calcanim/blob/master/Espacios%20vectoriales/asociatividad.py))
  - [Propiedad distributiva en un espacio vectorial](https://www.youtube.com/watch?v=KB6rhZ854OI) ([distributiva.py](https://github.com/animathica/calcanim/blob/master/Espacios%20vectoriales/distributiva.py))
  - [Inverso aditivo de un vector](https://www.youtube.com/watch?v=RJrFM0sV9Os) ([inverso_aditivo.py](https://github.com/animathica/calcanim/blob/master/Espacios%20vectoriales/inverso_aditivo.py))
  - [Bases de espacios vectoriales](https://www.youtube.com/watch?v=E-fkJo8f7pI) ([bases.py](https://github.com/animathica/calcanim/blob/master/Espacios%20vectoriales/bases.py))
  - [Norma euclideana y sus propiedades](https://www.youtube.com/watch?v=HXG0XtM1kmM) ([norma_euclidea.py](https://github.com/animathica/calcanim/blob/master/Espacios%20vectoriales/norma_euclidea.py))
  - [Diferentes tipos de normas](https://www.youtube.com/watch?v=u0plZWFAor0) ([tipos_normas.py](https://github.com/animathica/calcanim/blob/master/Espacios%20vectoriales/tipos_normas.py))
  - [Producto interno de vectores](https://www.youtube.com/watch?v=eEABVOd5myc) ([prod_interno.py](https://github.com/animathica/calcanim/blob/master/Espacios%20vectoriales/prod_interno.py))
  - **Vector proyección de x sobre y** ([proyeccion.py](https://github.com/animathica/calcanim/blob/master/Espacios%20vectoriales/proyeccion.py))
  - [Métrica](https://www.youtube.com/watch?v=3FDLM-HpvPY) ([metrica.py](https://github.com/animathica/calcanim/blob/master/Espacios%20vectoriales/metrica.py))
  
## Sucesiones:
  - Definición de sucesiones
  - Sucesiones acotadas
  - Subsucesiones
  - Ejemplos de sucesiones
  - Defición de límite de sucesiones
  - Teorema puente de sucesiones
  - Sucesiones de Cauchy
  - Teorema de rectángulos anidados
  - Teorema de Bolzano Weiestrass
  
## Topología de R^n:
  - Bolas y vecindades
  - Tipos de puntos
  - Conjuntos abiertos
  - COnjuntos cerrados
  - Ni abierto, ni cerrado
  - Cerradura de un conjunto
  - Puntos aislados, de acumulación y conjunto derivado
  - Cubierta de un conjunto
  - Conjuntos compactos
  - Número de Lebesge
  - Conjuntos conexos y disconexos
  - Conjuntos convexos
  
## Límite y continuidad en funciones multivariable:
  - Definición de gráficas
  - Ejemplos de gráficas 
  - Imagen inversa
  - Definición de conjuntos de nivel
  - Ejemplo de curvas de nivel
  - Existencia del límite de funciones de R^n a R^m en x_0
  - Ejemplo de límite en campos
  - Límites direccionales
  - Existencia del límite en infinito de funciones de R a R^n
  - Existencia del límite en infinito de funciones de R^n a R
  - Divergencia a infinito de funciones de R a R^n en un punto t_0
  - Divergencia a infinito del límite de funciones de R^n a R en
  un punto a
  - Divergencia a infinito de funciones de R a R^n en infinito
  - Divergencia a infinito del límite de funciones de R^n a R en infinito.
  - Continuidad con sucesiones
  - Teorema de operaciones para funciones continuas
  - Funciones continuas y abiertos  
  - Teorema fuerte: las funciones continuas son acotadas en compactos
  - Teorema de valor extremo (parte 1)
  - Teorema del Valor Intermedio  

## Calculo diferencial en curvas:
  - Curvas en el plano
  - Tipos de curvas (curvas simples y simples cerradas)
  - Vector velocidad, rápidez y derivabilidad
  - **Teorema puente: derivabilidad de curvas**
  - **Tangente y vector tangente unitario**
  - Reparametrización de curvas 
  - Curvas regulares y picos
  - Curvas rectificables
  - Curvas no rectificables
  - Curvas suaves y cruces
  - Vector aceleración y aceleración tangencial
  - Curvatura
  - **Curvas en el espacio**
  - **Vector binormal**
  - **Torsión**
  - **Teorema Fundamental de Curvas**

## Cálculo diferencial de superficies
  - Translaciones y Hometecias en Superficies
  - **Función tipo Dirichlet**
  - Límite de cocientes de funciones de dos variables
  - **Límites iterados**
  - Planos y su inclinación
  - Plano tangente y derivadas direccionales
  - **Parciales y diferenciabilidad**
  - **Teorema de operaciones: diferenciabilidad de superficies
  - Derivada direccional**
  - **Parciales cruzadas**
  - Máximos y mínimos
  - **Multiplicadores de Lagrange**
  - **Máximos y mínimos globales**
  - **Teorema de Taylor para superficies**
  - Teorema de la función implícita
  - Teoremas de diferenciabilidad
  - **Corte de una superficie con un plano**
  - Plano tangente a una superficie 
  - **Gradiente**
  - Funciones de R^2 en R^3: superficies parametrizadas

## Extra:
  - Gráficas en R^4
  
## Funciones de R^n a R^m:
  - Coordenadas Polares y Cartesianas
  - Campos lineales y Cambios de Coordenadas
  - **Campos diferenciables en R^2**
  - Funciones de R^2 en R^3: superficies parametrizadas

## Teoremas de diferenciabilidad:
  - Teorema de la función inversa
  - Regla de la cadena 

## Integral de volumen:
  - Definición
  - **Criterio de Lebesgue**
  - **Fubini**
  - Cambio de variable

## Integral de línea:
  - **Definición**
  - **Teoremas fundamentales**
  - **Rotacional en R^2**
  - **Teorema de Green**
  - **Rotacional en R^3**

## Integral de superficie:
  - **Definición**
  - **Stokes**
  - **Divergencia**
  - **Gauss**

  
