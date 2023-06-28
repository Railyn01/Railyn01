
import requests
import webbrowser
from datetime import date

cedula= input("Introduzca su cedula : ")

api= "https://api.adamix.net/apec/cedula/ " + cedula
datos= requests.get(api).json()

n = (datos['Nombres'])
a1= (datos['Apellido1'])
a2= (datos['Apellido2'])
fn= (datos['FechaNacimiento'][:10])
ft= (datos['foto'])
s = (datos['IdSexo'])

a= int(fn[0:4])
m= int(fn[5:7])
d= int(fn[8:10])

da= date.today().day 
ma= date.today().month
aa= date.today().year

edad = aa - a
if d > da and m > ma:
    edad -=1
elif d <= da and m > ma:
    edad -= 1

z=[ "Capricornio", "Acuario", "Piscis", "Aries", "Tauro", "Géminis", "Cáncer", "Leo", "Virgo", "Libra", "Escorpio", "Sagitario "]
f=[20 , 19 , 20 , 20 , 21 , 21 , 22 , 22 , 22 , 22 , 22 , 21]
m-=1
if d > f[m]:
    m += 1
if m==12:
    m=0

x = open ('index.html', 'w')

html= """
<html>
<head>
<Title> Datos </Title>  
<link rel="stylesheet" href="css.css">
</head>
<div id = "css"> 
<body>

<center> <h2> Datos de la Persona : </h2> </center>
<br>
<img src="#ft" height = " 170 " width = " 175 " >

<ul>
    <li> <h4>Nombres : #n  </h4></li>
    <li> <h4> Apellidos : #a1  #a2 </h4>  </li>
    <li> <h4> Fecha de Nacimiento : #fn </h4>  </li>
    <li> <h4> Edad : #e </h4> </li>
    <li> <h4> Signo zodiacal : #z </h4>  </li>
    <li> <h4> Sexo : #s </h4> </li>
</ul>
</body>
</div>
</html>
"""

html= html.replace('#n' , n)
html= html.replace('#a1', a1)
html= html.replace('#a2', a2)
html= html.replace('#fn', fn)
html= html.replace('#ft', ft)
html= html.replace('#s',  s)
html= html.replace('#e', str (edad))
html= html.replace('#z', str (z[m]))
x.write(html)
x.close()

input (" Presione Enter para continuar... ")

webbrowser.open(' index.html ')
