
<h1 align="center">AISLAMIENTO DE VOZ ESPECIFICA EN AUDIO MIXTO</h1>

<p align="center"> Problema:  Fiesta de cóctel</p>
<br />
<div align="center">
 <img src="FIESTA.jpg" alt="Fiesta" width="300" height="300">
</div>

<br />
En un evento tipo coctel, se instalaron varios micrófonos para escuchar lo que
las personas estaban hablando; una vez terminó la fiesta, se solicitó a los
ingenieros que entregaran el audio de la voz de uno de los participantes.
Los ingenieros analizaron las señales grabadas por los micrófonos eran mezclas
de señales que provenían de diferentes fuentes (personas) para todos los casos
y se encontraron con el problema de aislar la voz de interés.



## Tabla de contenidos:
---

- [OBJETIVO](#objetivo)
- [MONTAJE](#montaje)
- [PROCESAMIENTO DE LAS SEÑALES](#procesamiento)
- [Guía de instalación](#guía-de-instalación)
- [Cómo contribuir](#cómo-contribuir)
- [Código de conducta](#código-de-conducta)
- [Autor/es](#autores)
- [Información adicional](#información-adicional)
- [Licencia](#licencia)
- [Limitación de responsabilidades - Solo BID](#limitación-de-responsabilidades)

## Objetivo
---
En este trabajo, se propuso abordar el desafiante problema de la 'fiesta de cóctel'. Simulando un escenario real, se configuró un arreglo de múltiples micrófonos para capturar simultáneamente las señales de varias fuentes sonoras. Al igual que en una reunión social, las grabaciones resultantes fueron una mezcla compleja de voces superpuestas, representando el típico desafío de aislar una señal de interés en un entorno acústicamente ruidoso. El objetivo principal fue desarrollar y evaluar técnicas de procesamiento de señales para abordar este problema, explorando algoritmos de separación de fuentes que permitieran aislar la voz de una persona específica a partir de una mezcla de múltiples hablantes. A través de este experimento, se buscó comprender los desafíos inherentes a la separación de fuentes y evaluar la eficacia de diferentes enfoques para resolver el problema de la 'fiesta de cóctel'.





## Montaje
---
Se implementó un montaje en el que se utilizaron tres micrófonos con una frecuencia de muestreo de 44 kHz, asegurada por la aplicación RecForge II. Las tres personas encargadas de emitir las voces se ubicaron en sillas a diferentes distancias respecto a los micrófonos, que estuvieron colocados en el mismo punto. Como primer paso, se realizó una grabación del ruido ambiente, que fue mínimo gracias a que el experimento se llevó a cabo en un cuarto insonorizado, cuyo objetivo es minimizar la reflexión del sonido. Después, cada persona recitó un trabalenguas, el cual fue captado por los micrófonos. Estos audios se guardaron y usaron como archivos .wav. 

<br />
<div align="center">
 <img src="MONTAJE.jpeg" alt="Montaje" width="250" height="250">
</div>



## Procesamiento
---
...
hola

...

 	
## Guía de instalación
---
Paso a paso de cómo instalar la herramienta digital. En esta sección es recomendable explicar la arquitectura de carpetas y módulos que componen el sistema.

Según el tipo de herramienta digital, el nivel de complejidad puede variar. En algunas ocasiones puede ser necesario instalar componentes que tienen dependencia con la herramienta digital. Si este es el caso, añade también la siguiente sección.

La guía de instalación debe contener de manera específica:
- Los requisitos del sistema operativo para la compilación (versiones específicas de librerías, software de gestión de paquetes y dependencias, SDKs y compiladores, etc.).
- Las dependencias propias del proyecto, tanto externas como internas (orden de compilación de sub-módulos, configuración de ubicación de librerías dinámicas, etc.).
- Pasos específicos para la compilación del código fuente y ejecución de tests unitarios en caso de que el proyecto disponga de ellos.

### Dependencias
Descripción de los recursos externos que generan una dependencia para la reutilización de la herramienta digital (librerías, frameworks, acceso a bases de datos y licencias de cada recurso). Es una buena práctica describir las últimas versiones en las que ha sido probada la herramienta digital. 

    Puedes usar este estilo de letra diferenciar los comandos de instalación.

## Cómo contribuir
---
Esta sección explica a desarrolladores cuáles son las maneras habituales de enviar una solicitud de adhesión de nuevo código (“pull requests”), cómo declarar fallos en la herramienta y qué guías de estilo se deben usar al escribir más líneas de código. También puedes hacer un listado de puntos que se pueden mejorar de tu código para crear ideas de mejora.

## Código de conducta 
---
El código de conducta establece las normas sociales, reglas y responsabilidades que los individuos y organizaciones deben seguir al interactuar de alguna manera con la herramienta digital o su comunidad. Es una buena práctica para crear un ambiente de respeto e inclusión en las contribuciones al proyecto. 

La plataforma Github premia y ayuda a los repositorios dispongan de este archivo. Al crear CODE_OF_CONDUCT.md puedes empezar desde una plantilla sugerida por ellos. Puedes leer más sobre cómo crear un archivo de Código de Conducta (aquí)[https://help.github.com/articles/adding-a-code-of-conduct-to-your-project/]

## Autor/es
---
Nombra a el/los autor/es original/es. Consulta con ellos antes de publicar un email o un nombre personal. Una manera muy común es dirigirlos a sus cuentas de redes sociales.

## Información adicional
---
Esta es la sección que permite agregar más información de contexto al proyecto como alguna web de relevancia, proyectos similares o que hayan usado la misma tecnología.

## Licencia 
---

La licencia especifica los permisos y las condiciones de uso que el desarrollador otorga a otros desarrolladores que usen y/o modifiquen la herramienta digital.

Incluye en esta sección una nota con el tipo de licencia otorgado a esta herramienta digital. El texto de la licencia debe estar incluído en un archivo *LICENSE.md* o *LICENSE.txt* en la raíz del repositorio.

Si desconoces qué tipos de licencias existen y cuál es la mejor para cada caso, te recomendamos visitar la página https://choosealicense.com/.

Si la herramienta que estás publicando con la iniciativa Código para el Desarrollo ha sido financiada por el BID, te invitamos a revisar la [licencia oficial del banco para publicar software](https://github.com/EL-BID/Plantilla-de-repositorio/blob/master/LICENSE.md)

## Limitación de responsabilidades
Disclaimer: Esta sección es solo para herramientas financiadas por el BID.

El BID no será responsable, bajo circunstancia alguna, de daño ni indemnización, moral o patrimonial; directo o indirecto; accesorio o especial; o por vía de consecuencia, previsto o imprevisto, que pudiese surgir:

i. Bajo cualquier teoría de responsabilidad, ya sea por contrato, infracción de derechos de propiedad intelectual, negligencia o bajo cualquier otra teoría; y/o

ii. A raíz del uso de la Herramienta Digital, incluyendo, pero sin limitación de potenciales defectos en la Herramienta Digital, o la pérdida o inexactitud de los datos de cualquier tipo. Lo anterior incluye los gastos o daños asociados a fallas de comunicación y/o fallas de funcionamiento de computadoras, vinculados con la utilización de la Herramienta Digital.
