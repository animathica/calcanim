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
  - [Motivación, ¿de donde sale la necesidad de utilizar funciones de múltiples variables?](https://youtu.be/x9pDiAbOZKk)

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
  - [Vector proyección de x sobre y](https://www.youtube.com/watch?v=Kktc8_Q6C0I) ([proyeccion.py](https://github.com/animathica/calcanim/blob/master/Espacios%20vectoriales/proyeccion.py))
  - [Métrica](https://www.youtube.com/watch?v=3FDLM-HpvPY) ([metrica.py](https://github.com/animathica/calcanim/blob/master/Espacios%20vectoriales/metrica.py))
  
## Sucesiones:
  - [Definición de sucesiones](https://youtu.be/4ZLPARmmyXw) ([definicion.py](https://github.com/animathica/calcanim/blob/master/Sucesiones/definicion.py))
  - [Sucesiones acotadas](https://youtu.be/qdRRx_2LE6Y) ([acotadas.py](https://github.com/animathica/calcanim/blob/master/Sucesiones/acotadas.py))
  - [Subsucesiones](https://youtu.be/FxwZYd1dwgU) ([subsucesiones.py](https://github.com/animathica/calcanim/blob/master/Sucesiones/subsucesiones.py))
  - [Ejemplos de sucesiones](https://youtu.be/L7gi9ypWROQ) ([ejemplos.py](https://github.com/animathica/calcanim/blob/master/Sucesiones/ejemplos.py))
  - [Defición de límite de sucesiones](https://youtu.be/gckzpzsLdso) ([limite.py](https://github.com/animathica/calcanim/blob/master/Sucesiones/limite.py))
  - [Teorema puente de sucesiones](https://youtu.be/HUcMlULQyDk) ([teo_puente.py](https://github.com/animathica/calcanim/blob/master/Sucesiones/teo_puente.py))
  - [Sucesiones de Cauchy](https://youtu.be/FUaPUN98cWA) ([cauchy.py](https://github.com/animathica/calcanim/blob/master/Sucesiones/cauchy.py))
  - [Teorema de rectángulos anidados](https://youtu.be/e3elst62Tho) ([rectangulos_anidados.py](https://github.com/animathica/calcanim/blob/master/Sucesiones/rectangulos_anidados.py))
  - [Teorema de Bolzano Weiestrass](https://youtu.be/40SytFua38c) ([bolzano-weierstrass.py](https://github.com/animathica/calcanim/blob/master/Sucesiones/bolzano-weierstrass.py))
  
## Topología de R^n:
  - [Bolas y vecindades](https://youtu.be/rlVvklg52sE) ([bolas.py](https://github.com/animathica/calcanim/blob/master/Topologia/bolas.py))
  - [Tipos de puntos](https://youtu.be/wu67J58H8SE) ([tipos_puntos.py](https://github.com/animathica/calcanim/blob/master/Topologia/tipos_puntos.py))
  - [Conjuntos abiertos](https://youtu.be/UH8UvU2ms8c) ([abiertos.py](https://github.com/animathica/calcanim/blob/master/Topologia/abiertos.py))
  - [Conjuntos cerrados](https://youtu.be/D9czG7Qy6pk) ([cerrados.py](https://github.com/animathica/calcanim/blob/master/Topologia/cerrados.py))
  - [Ni abierto, ni cerrado](https://youtu.be/bBtV_er1b5s) ([noabierto_nocerrado.py](https://github.com/animathica/calcanim/blob/master/Topologia/noabierto_nocerrado.py))
  - [Cerradura de un conjunto](https://youtu.be/GkkZASMDEUY) ([cerradura.py](https://github.com/animathica/calcanim/blob/master/Topologia/cerradura.py))
  - [Puntos aislados, de acumulación y conjunto derivado](https://youtu.be/Ubn2WAfWHMI) ([aislados_acumulacion.py](https://github.com/animathica/calcanim/blob/master/Topologia/aislados_acumulacion.py))
  - [Cubierta de un conjunto](https://youtu.be/z7akWs73nxw) ([cubierta.py](https://github.com/animathica/calcanim/blob/master/Topologia/cubierta.py))
  - [Conjuntos compactos](https://youtu.be/N-U-dZYctMc) ([compactos.py](https://github.com/animathica/calcanim/blob/master/Topologia/compactos.py))
  - [Número de Lebesgue](https://youtu.be/G0xexlvnzIw) ([lebesgue.py](https://github.com/animathica/calcanim/blob/master/Topologia/lebesgue.py))
  - [Conjuntos conexos y disconexos](https://youtu.be/53B--2zUB8w) ([conexidad.py](https://github.com/animathica/calcanim/blob/master/Topologia/conexidad.py))
  - [Conjuntos convexos](https://youtu.be/e41cFOJbiPc) ([convexos.py](https://github.com/animathica/calcanim/blob/master/Topologia/convexos.py))
  
## Límite y continuidad en funciones multivariable:
  - [Definición de gráficas](https://youtu.be/6gValeBGu5s) ([definicion_grafica.py](https://github.com/animathica/calcanim/blob/lim_cont/L%C3%ADmite%20y%20continuidad%20en%20funciones%20multivariable/definicion_grafica.py))
  - [Ejemplos de gráficas](https://youtu.be/XNtniowm-mI) ([visualizacion.py](https://github.com/animathica/calcanim/blob/lim_cont/L%C3%ADmite%20y%20continuidad%20en%20funciones%20multivariable/visualizacion.py))
  - [Imagen inversa](https://youtu.be/bci1v1ex7RY) ([imagen_inversa.py](https://github.com/animathica/calcanim/blob/lim_cont/L%C3%ADmite%20y%20continuidad%20en%20funciones%20multivariable/imagen_inversa.py))
  - [Definición de conjuntos de nivel](https://youtu.be/X0tkDP7R1IE) ([conjunto_nivel.py](https://github.com/animathica/calcanim/blob/lim_cont/L%C3%ADmite%20y%20continuidad%20en%20funciones%20multivariable/conjunto_nivel.py))
  - [Ejemplo de curvas de nivel](https://youtu.be/u1yuqaeZAbU) ([curva_nivel.py](https://github.com/animathica/calcanim/blob/lim_cont/L%C3%ADmite%20y%20continuidad%20en%20funciones%20multivariable/curva_nivel.py))
  - [Existencia del límite de funciones de R^n a R^m en x_0](https://youtu.be/-oNl2FKUc1s) ([existencia_x0.py](https://github.com/animathica/calcanim/blob/lim_cont/L%C3%ADmite%20y%20continuidad%20en%20funciones%20multivariable/existencia_x0.py))
  - Ejemplo de límite en campos ([campos.py](https://github.com/animathica/calcanim/blob/lim_cont/L%C3%ADmite%20y%20continuidad%20en%20funciones%20multivariable/campos.py))
  - Límites direccionales ([direccionales.py](https://github.com/animathica/calcanim/blob/lim_cont/L%C3%ADmite%20y%20continuidad%20en%20funciones%20multivariable/direccionales.py))
  - [Existencia del límite en infinito de funciones de R a R^n](https://youtu.be/hb6wAc47Heg) ([limite_infinito_R-Rn.py](https://github.com/animathica/calcanim/blob/lim_cont/L%C3%ADmite%20y%20continuidad%20en%20funciones%20multivariable/limite_infinito_R-Rn.py))
  - [Existencia del límite en infinito de funciones de R^n a R](https://youtu.be/jFkIez1VNps) ([limite_infinito_Rn-R.py](https://github.com/animathica/calcanim/blob/lim_cont/L%C3%ADmite%20y%20continuidad%20en%20funciones%20multivariable/limite_infinito_Rn-R.py))
  - [Divergencia a infinito de funciones de R a R^n en un punto t_0](https://youtu.be/eWlEpjGsdb8) ([divergencia_R-Rn_punto.py](https://github.com/animathica/calcanim/blob/lim_cont/L%C3%ADmite%20y%20continuidad%20en%20funciones%20multivariable/divergencia_R-Rn_punto.py))
  - [Divergencia a infinito del límite de funciones de R^n a R en un punto a](https://youtu.be/O9Ak-U7WRms) ([divergencia_Rn-R_punto.py](https://github.com/animathica/calcanim/blob/lim_cont/L%C3%ADmite%20y%20continuidad%20en%20funciones%20multivariable/divergencia_Rn-R_punto.py))
  - [Divergencia a infinito de funciones de R a R^n en infinito](https://youtu.be/u9m-0a2eChM) ([divergencia_R-Rn_infinito.py](https://github.com/animathica/calcanim/blob/lim_cont/L%C3%ADmite%20y%20continuidad%20en%20funciones%20multivariable/divergencia_R-Rn_infinito.py))
  - [Divergencia a infinito del límite de funciones de R^n a R en infinito](https://youtu.be/ghVhDdAfY88) ([divergencia_Rn-R_infinito.py](https://github.com/animathica/calcanim/blob/lim_cont/L%C3%ADmite%20y%20continuidad%20en%20funciones%20multivariable/divergencia_Rn-R_infinito.py))
  - [Continuidad con sucesiones](https://youtu.be/j3xyulVd-BY) ([continuas_sucesiones.py](https://github.com/animathica/calcanim/blob/lim_cont/L%C3%ADmite%20y%20continuidad%20en%20funciones%20multivariable/continuas_sucesiones.py))
  - [Teorema de operaciones para funciones continuas](https://youtu.be/7kpPhGtckMo) ([operaciones_continuas.py](https://github.com/animathica/calcanim/blob/lim_cont/L%C3%ADmite%20y%20continuidad%20en%20funciones%20multivariable/operaciones_continuas.py))
  - [Funciones continuas y abiertos](https://youtu.be/-nlctRUPh7U) ([continuas_abiertos.py](https://github.com/animathica/calcanim/blob/lim_cont/L%C3%ADmite%20y%20continuidad%20en%20funciones%20multivariable/continuas_abiertos.py))
  - [Teorema fuerte: las funciones continuas son acotadas en compactos](https://youtu.be/0vRiS8It7CQ) ([continua_acotada.py](https://github.com/animathica/calcanim/blob/lim_cont/L%C3%ADmite%20y%20continuidad%20en%20funciones%20multivariable/continua_acotada.py))
  - [Teorema de valor extremo (parte 1)](https://youtu.be/GuqeijJncTg) ([valor_extremo.py](https://github.com/animathica/calcanim/blob/lim_cont/L%C3%ADmite%20y%20continuidad%20en%20funciones%20multivariable/valor_extremo.py))
  - [Teorema del Valor Intermedio](https://youtu.be/IR5fTCz4ZVI) ([valor_intermedio.py](https://github.com/animathica/calcanim/blob/lim_cont/L%C3%ADmite%20y%20continuidad%20en%20funciones%20multivariable/valor_intermedio.py))

## Calculo diferencial en curvas:
  - Curvas en el plano ([plano.py](https://github.com/animathica/calcanim/blob/Curvas/Calculo%20diferencial%20en%20curvas/plano.py))
  - [Tipos de curvas: simples y simples cerradas](https://www.youtube.com/watch?v=inWeRDKCbJE) ([tipos.py](https://github.com/animathica/calcanim/blob/Curvas/Calculo%20diferencial%20en%20curvas/tipos.py))
  - Vector velocidad, rápidez y  ([vel_rapidez.py](https://github.com/animathica/calcanim/blob/Curvas/Calculo%20diferencial%20en%20curvas/vel_rapidez.py))
  - **Teorema puente: derivabilidad de curvas**
  - **Tangente y vector tangente unitario**
  - [Reparametrización de curvas](https://www.youtube.com/watch?v=pXDnFBIundA) ([reparametrizacion.py](https://github.com/animathica/calcanim/blob/Curvas/Calculo%20diferencial%20en%20curvas/reparametrizacion.py))
  - [Curvas regulares y picos](https://www.youtube.com/watch?v=2PRSPgs7hQE) ([regulares.py](https://github.com/animathica/calcanim/blob/Curvas/Calculo%20diferencial%20en%20curvas/regulares.py))
  - [Curvas rectificables](https://www.youtube.com/watch?v=Nkgcjfh0Faw&t=47s) ([rectificables.py](https://github.com/animathica/calcanim/blob/Curvas/Calculo%20diferencial%20en%20curvas/rectificables.py))
  - Curvas no rectificables ([no_rectificables.py](https://github.com/animathica/calcanim/blob/Curvas/Calculo%20diferencial%20en%20curvas/no_rectificables.py))
  - Curvas suaves y cruces ([suaves_y_cruces](https://github.com/animathica/calcanim/blob/Curvas/Calculo%20diferencial%20en%20curvas/suaves_y_cruces.py))
  - **Vector aceleración y aceleración tangencial**
  - **Circulo osculador**
  - **Curvas en el espacio**
  - **Vector binormal**
  - **Torsión**
  - **Teorema Fundamental de Curvas**

## Cálculo diferencial de superficies
  - Translaciones y Hometecias en Superficies ([composicion.py](https://github.com/animathica/calcanim/blob/C%C3%A1lculo-diferencial-de-superficies/C%C3%A1lculo%20diferencial%20de%20superficies/composicion.py))
  - **Función tipo Dirichlet**
  - Límite de cocientes de funciones de dos variables ([cociente.py](https://github.com/animathica/calcanim/blob/C%C3%A1lculo-diferencial-de-superficies/C%C3%A1lculo%20diferencial%20de%20superficies/cociente.py))
  - **Límites iterados**
  - [Planos y su inclinación](https://www.youtube.com/watch?v=ZJZ4fO8v7Ns&t=17s) ([inclinacion.py](https://github.com/animathica/calcanim/blob/C%C3%A1lculo-diferencial-de-superficies/C%C3%A1lculo%20diferencial%20de%20superficies/inclinacion.py))
  - Plano tangente y derivadas direccionales ([tangente.py](https://github.com/animathica/calcanim/blob/C%C3%A1lculo-diferencial-de-superficies/C%C3%A1lculo%20diferencial%20de%20superficies/tangente.py))
  - **Parciales y diferenciabilidad**
  - **Teorema de operaciones: diferenciabilidad de superficies**
  - **Derivada direccional**
  - **Parciales cruzadas**
  - Máximos y mínimos
  - **Multiplicadores de Lagrange**
  - **Máximos y mínimos globales**
  - **Teorema de Taylor para superficies**
  - Teorema de la función implícita ([implicita.py](https://github.com/animathica/calcanim/blob/C%C3%A1lculo-diferencial-de-superficies/C%C3%A1lculo%20diferencial%20de%20superficies/implicita.py))
  - Teoremas de diferenciabilidad ([teo_dif.py](https://github.com/animathica/calcanim/blob/C%C3%A1lculo-diferencial-de-superficies/C%C3%A1lculo%20diferencial%20de%20superficies/teo_dif.py))
  - **Corte de una superficie con un plano**
  - **Gradiente**
  - [Funciones de R^2 en R^3: superficies parametrizadas](https://www.youtube.com/watch?v=7F2uIrlOFj0&t=5s) ([superficies_parametrizadas.py](https://github.com/animathica/calcanim/blob/funciones_Rn_a_Rm/Funciones%20de%20Rn%20a%20Rm/superficies_parametrizadas.py))

## Extra:
  - Gráficas en R^4 ([graf_R4.py](https://github.com/animathica/calcanim/blob/C%C3%A1lculo-diferencial-de-superficies/C%C3%A1lculo%20diferencial%20de%20superficies/graf_R4.py))
  
## Funciones de R^n a R^m:
  - [Coordenadas Polares y Cartesianas](https://www.youtube.com/watch?v=hnNhcPwL16U) ([polares_cartesianas.py](https://github.com/animathica/calcanim/blob/funciones_Rn_a_Rm/Funciones%20de%20Rn%20a%20Rm/polares_cartesianas.py))
  - Campos lineales y Cambios de Coordenadas ([campos_lineales.py](https://github.com/animathica/calcanim/blob/funciones_Rn_a_Rm/Funciones%20de%20Rn%20a%20Rm/campos_lineales.py))
  - **Campos diferenciables en R^2**
  - [Funciones de R^2 en R^3: superficies parametrizadas](https://www.youtube.com/watch?v=7F2uIrlOFj0&t=5s) ([superficies_parametrizadas.py](https://github.com/animathica/calcanim/blob/funciones_Rn_a_Rm/Funciones%20de%20Rn%20a%20Rm/superficies_parametrizadas.py))

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

  
