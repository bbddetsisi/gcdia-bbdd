---
marp        : true
size        : 4:3
# auto-scaling:
#     - true
#     - fittingHeader
#     - math
#     - code
paginate    : true
theme       : hegel
title       : Base de Datos I
author      : Raúl Lara Cabrera
description : Presentación de la asignatura Bases de Datos
---
<style>

   .cite-author {
      text-align        : right;
   }
   .cite-author:after {
      color             : orangered;
      font-size         : 125%;
      /* font-style        : italic; */
      font-weight       : bold;
      font-family       : Cambria, Cochin, Georgia, Times, 'Times New Roman', serif;
      padding-right     : 130px;
   }
   .cite-author[data-text]:after {
      content           : " - "attr(data-text) " - ";
   }

   .cite-author p {
      padding-bottom : 40px
   }

</style>

<!-- _class: titlepage -->
![bg left:33%](https://upload.wikimedia.org/wikipedia/commons/9/91/Cabinet_Asile.jpg)

<div class="title">Bases de Datos I</div>
<div class="subtitle">Grado en Ciencia de Datos e Inteligencia Artificial</div>
<div class="author">Raúl Lara Cabrera</div>
<div class="date">Curso 2021/2022</div>
<div class="organization">Departamento de Sistemas Informáticos</div>

---

# Descripción de la asignatura

La asignatura tiene como objetivo que los alumnos aprendan los conceptos necesarios para diseñar e implementar bases de datos **relacionales** desde el diseño usando el *Modelo Relacional* y el *Modelo Entidad/Relación*, así como la transformación del Modelo ER a bases de datos relacionales y su implementación en un gestor relacional.

---

# Descripción de la asignatura

Se estudia el lenguaje **SQL** como lenguaje de acceso a bases de datos, se analiza cómo realizar una aplicación en la que se construya y acceda a una base de datos y se estudian aspectos básicos de seguridad y acceso a bases de datos. Todos los conceptos analizados en teoría se complementan con realización de trabajos y laboratorios prácticos.

---

# Profesorado

Raúl Lara Cabrera
Despacho 1230
raul.lara@upm.es

## Tutorías

Reservar en: <https://calendly.com/raul-lara/tutoria-online>

---

# Temario

1. Introducción a las bases de datos
2. Diseño conceptual y paso al diseño lógico
3. El lenguaje SQL
4. Acceso programático a bases de datos
5. Seguridad y acceso a bases de datos
6. Diseño relacional

---

# Diseño conceptual y paso a tablas

<div class="columns">
<div>

- Modelo Entidad-Relación
- Introducción al modelo relacional
- Paso a tablas del modelo E/R
- Integridad referencial

</div>
<div>

![](img/mysql_workbench.png)
![](img/diagrams.png)

</div>
</div>

---

# El lenguaje SQL

<div class="columns">
<div>

- Introducción a un SGBD<sup>1</sup> relacional
- Operaciones DDL<sup>2</sup>
- Operaciones DML<sup>3</sup>
- Procedimientos almacenados y triggers

</div>
<div>

![MySQL Workbench](img/mysql_workbench.png)
![MySQL](img/mysql.png)

</div>
</div>

> <sup>1</sup> Sistema Gestor de Bases de Datos
> <sup>2</sup> Data Definition Language
> <sup>3</sup> Data Moficiation Language

---

# Acceso programático a BBDD

- Introducción: ODBC y JDBC
- Acceso a un SGBC con Python
  - Conexión al servidor y realización de peticiones
  - Gestión de los resultados
  - Manejo de errores
  - Consultas parametrizadas
  - Otras funcionalidades del conector
- Gestión de transacciones

![SQL Alchemy](https://www.sqlalchemy.org/img/sqla_logo.png) ![Python](https://www.python.org/static/img/python-logo.png)

---

# Seguridad y acceso a bases de datos

- Introducción a la seguridad en sistemas distribuidos
- Modelos de seguridad en Internet: seguridad en el nivel de transporte (SSL)
- Plataforma OpenSSL
- Gestión de usuarios
- Acceso SSL a un SGBD

![MySQL Workbench](img/mysql_workbench.png) ![MySQL](img/mysql.png) ![OpenSSL](img/openssl.png)

---

# Diseño relacional

- Fundamentos del Modelo Relacional
- Álgebra relacional
- Formas normales y normalización

![RelaX](img/relax.png)

---

# Evaluación continua

- Exámenes parciales:
  1. Modelo E/R y paso a tablas<sup>1</sup> *20%*; SQL<sup>1</sup> *20%*
  2. Acceso programático<sup>2</sup> *10%*; acceso seguro<sup>2</sup> *10%*; modelo relacional<sup>1</sup> *20%*
- Prácticas<sup>2</sup>:
  1. Proyecto/entrega acceso programático *10%*
  2. Proyecto/entrega acceso seguro: *10%*

> <sup>1</sup> Nota mínima 4 sobre 10 en cada bloque **para aprobar la asignatura**
> <sup>2</sup> Nota mínima 3 sobre 10 en cada bloque/práctica **para aprobar la asignatura**

---

# Evaluación solo prueba final

La evaluación por prueba final en la convocatoria ordinaria sólo puede realizarse por aquellos alumnos que **de forma extraordinaria** no puedan realizar la evaluación continua y realicen una **petición por escrito** durante los **primeros 15 días** del curso.

Examen final excluyente con evaluación continua, en el cual será necesario obtener **al menos 5 puntos sobre 10 en cada bloque temático** para aprobar la asignatura.

---

# Convocatoria extraordinaria

Examen final con las mismas características y requisitos que la evaluación por prueba final.

**Importante**: la nota de los bloques aprobados durante la evaluación continua se mantiene para la evaluación final, por lo que no será necesario examinarse de aquellos bloques aprobados previamente.

---

# Recursos didácticos

1. **Moodle de la asignatura**.
2. **Principles of Data Base Systems**, Jeffrey D. Ullman, Ed. Computer Science Press,Rockville, Maryland, 1982.
3. **Relational Database Design**, I.T. Hawryszkiewycz, Prentice-Hall Australia, 1990
4. **First Course in Database Systems**, Jeffrey D. Ullman, Jennifer Widom, 2007.
5. **Database Systems: The Complete Book**, Hector Garcia-Molina, Jeff Ullman, and Jennifer Widom, 2008.
6. **Relational Database Theory**, Atzeni & V. De Antonellis, The Benjamin/Cummings Publishing Company Inc., 1993.

---
# Recursos didácticos

<div class="columns">
<div>

<center>

![h:450](https://images-na.ssl-images-amazon.com/images/I/910tnSEJ9sL.jpg)

<figcaption align="center">
Primera edición (2009).
</figcaption>

</center>

</div>
<div>

### The manga guide to databases

Muy recomendable para quien quiera aprender los conceptos básicos de bases de datos relacionales.

Incluído en la suscripción institucional de la UPM a [O'Reilly](https://www.amazon.com/gp/product/0198245971/ref=ox_sc_act_image_2?smid=A1ZZFT5FULY4LN&psc=1)

</div>
</div>
