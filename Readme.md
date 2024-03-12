# Análisis de Siniestralidad de la Cuidad De Buenos Aires

<img src="02.%20imagenes/Banner_Buenos_Aires.JPG" alt="BA" width="100%">

# 1. Descripción del Proyecto

El objetivo de este proyecto fue realizar un análisis de datos para el Observatorio de Movilidad y Seguridad Vial (OMSV) con el propósito de generar un Informe sobre la situación actual e histórica de los siniestros y victimas fatales en la Cuidad de Buenos Aires para el período 2016 a 2021.<br>

La finalidad del análisis fue la creación de:

1. Un Informe Final con recomendaciones
2. Un Dashboard para el seguimiento y gestión de los objetivos principales del **Plan de Seguridad Vial 2020-2023**.

# 2. Introducción

En Argentina se registra un promedio de 4.798 víctimas fatales por siniestros viales al año, lo que equivale a una tasa de mortalidad de 10,73 cada 100.000 habitantes. Mientras que en la Ciudad Autónoma de Buenos Aires se registra un promedio de 119 víctimas fatales anuales, lo que representa una tasa de mortalidad de 3,87 cada 100.000 habitantes. En conjunto, para el periodo 2016-2021 la Ciudad registró un total de 717 víctimas fatales por siniestros viales.

**El 82% de las víctimas fatales fueron usuarios vulnerables de la vía (42% motociclistas, 37% peatones y 3% ciclistas)**

# 3. Desarrollo del Proyecto

Comenzamos por entender la estructura de los datos, su forma, contenido.

### Dataset del Proyecto

El Dataset del proyecto se extrajo de la página de [Secretaría de Transporte y Obras Públicas](https://data.buenosaires.gob.ar/organization/transporte-y-obras-publicas) de la Cuidad de Buenos Aires.
Consiste en un archivo .xls con varias hojas.
Para el desarrollo del proyecto nos centramos en la hoja homicidios y complementamos la información con la hoja de victimas.

## 3.1. ETL

### 3.1 ETL Homicidios

Durante el ETL procuramos explorar cada una de las variables del Dataset para eliminar valores duplicados, erroneos, o vacíos y preparar la data para el proceso de EDA.

Para ver en detalle el paso a paso de este proceso se puede consultar:

[ETL y EDA de homicidios](01.%20ETL_EDA_homicidios.ipynb)
En este notebook encontrarán el proceso completo con sus paso, transformaciones y al tiempo que se desarrollan descripciones y conclusiones de lo analizado y hallado para cada variable.

### 3.2 ETL Victimas

En el notebook [ETL Victimas](02.%20ETL_victimas.ipynb) pueden encontrar el paso a paso detallado de las transformaciones realizadas al dataset homicidios en la hoja victimas.<br>
Este dataframe es luego guardado en victimas_etl.csv para ser utilizado en el EDA de Homicidios.hechos como complementario a hechos_df.<br>

## 3.2 EDA - Resumen del Análisis Exploratorio de Datos (EDA) sobre Siniestros Viales en la Ciudad de Buenos Aires

Durante el Análisis Exploratorio de Datos (EDA) del proyecto realicé un análisis detallado de las variables disponibles, sus relaciones y sus tendencias.
En el notebook [ETL_EDA_homicidios](01.%20ETL_EDA_homicidios.ipynb) se encuentra el paso a paso, detalle, desarrollo, hallazgos y conclusiones de todo lo trabajado durante el desarrollo del EDA.

A continuación, resumo los hallazgos más importantes del EDA:

1. **Análisis Univariable de Homicidios**
   Realicé un análisis univariable para cada variable del dataset, destacando los siguientes puntos:

- Analisis de la distribución de siniestros por año, mes y día.
- Observaciones de una tendencia a la baja en la cantidad de siniestros, con fluctuaciones debido a eventos como la pandemia de COVID-19.
- No encontré patrones claros en la distribución de siniestros por mes o día de la semana.

2. **Análisis Multivariable de Homicidios**
   Exploramos la relación entre variables y cómo afectan a la cantidad de siniestros:

- Se observó que la mayoría de los siniestros ocurrieron en intersecciones de calles.
- Las Avenidas fueron el tipo de calle con más siniestros.
- Los motociclistas y peatones fueron las víctimas más comunes en los siniestros, seguidos por los conductores de autos.
- Hubo una ligera tendencia a un mayor número de muertes durante los fines de semana en comparación con los días laborables.

3. **Evolución de la Cantidad de Siniestros**

- Analicé la evolución de la cantidad de siniestros por año y por tipo de calle.
- Observando una tendencia a la baja en la cantidad de siniestros en general, aunque con fluctuaciones debido a eventos externos como la pandemia.
- Las muertes de motociclistas representaron la mayoría de las muertes, seguidas por peatones y conductores de autos.

4. **Distribución de Muertes por Edad y Género**

- Se observa que el rango etario de 30-49 años representaron la mayor cantidad de muertes.
- Las fatalidad en los hombres es significativamente mayor que en las mujeres para todos los años y combinaciones analizados.
- Se realizó un análisis detallado de la distribución de muertes por edad y género, destacando diferencias significativas entre grupos de edad y género.

5. **Ocurrencia de Muertes por Franja Horaria**

<div style="text-align:center;">
    <img src="02.%20imagenes/Franja_horaria.JPG" alt="Franja_Horaria" width="40%">
</div>

- Identificamos los momentos del día con mayor frecuencia de muertes, tanto para motociclistas como para peatones: - Las _tardes de miércoles y viernes_ son periodos críticos con una alta incidencia de muertes.

#### Conclusiones EDA

Nuestro análisis proporciona una comprensión detallada de los siniestros viales en la Ciudad de Buenos Aires, destacando patrones, tendencias y factores de riesgo asociados. Estos hallazgos pueden ser utilizados para informar políticas públicas, campañas de seguridad vial y medidas de prevención para reducir la incidencia de siniestros y salvar vidas.

## 3.3 Datasets Complementarios:

Utilizamos la página de Estadísticas y Censo de la Cuidad de Buenos Aires para obtener información sobre la población, su distribución a lo largo de los años, el género y rango etario, para poder utilizarla luego en combinación con los dataset creados para la generación y construcción métricas, relaciones y desarrollo de KPIs y objetivos en el Dashboard.

Para ello, creamos las siguientes tablas a partir de los datos de Censo y Estadísticas:

1. Población Total por Año desde 2016 y proyecciones hasta 2025
2. Población Total por Género Año desde 2016 y proyecciones hasta 2025
3. Población Total por Rango Etario y Año desde 2016 y proyecciones hasta 2025

Todas estos Dataframes también se exportaron a MySQL y forman parte de la Base de Datos creada para el Proyecto.

El proceso y pasos se encuentra a detalle en [Data Adicional](03.%20Data%20Adicional.ipynb)

## 4. Creación de un DataBase con motor MySQL desde Python y Conexión con Power BI

Todo lo relativo a la creación de la base de Datos en MySQL desde Python y su posterior conexión con Power BI para la creación del Dashboard interactivo se encuentra detallado en :
[Creación de Database desde Python a MYSQL y Conexión de MySQL con Power BI](06.%20Connection_msql.ipynb)

Primero guardamos, luego del proceso de ETL y EDA detallado, los Dataframe resultantes en formato .csv.

Estos son:

1. **homicidios_etl.csv** : son los registros de los homicidios por número de siniestro y toda la información relevante, luego de la limpieza y transformacion de los datos.
2. **victimas_completo.csv**: es el dataframe donde se vinculan las victimas cada una identificada y asociada a su id de siniestro con la informacion adicional del género, edad y rango etario definido como información más relevante y complementaria a homicidios.

Segundo, creamos en MySQL Workbench la Database, que llamamos proyecto_individual_02.

El tercer paso fue conectar Python con MySQL, para que desde Python, con la base de datos ya creada, pudieramos crear y migrar con tan sólo unas pocas líneas de codigo las Tablas que serían nuestra base de Datos y posterior recursos en Power Bi.

Luego, tocó conectar la Base de Datos de MySQL con Power BI, en el notebook [Connection_mysql](06.%20Connection_msql.ipynb) se encuentra el instructivo para replicar lo que es la creación y la conexión en caso de que quisieran utilizarla o explorarla.
Con esto quedamos listos para comenzar a crear el Dashboard y todas las visualizaciones.

## 5. Desarrollo del Dashboard

En este punto no hay desarrollo del proceso para presentar, por lo que explicaré sinteticamente lo que podrán ver en detalle en el Dashboard que se presenta como el principal Entregable del Proyecto:

[Dashboard_Siniestros_Viales_2021](07.%20Dashboard.pbix)

<div style="text-align:center;">
    <img src="02.%20imagenes/Dashboard.JPG" alt="Dashboard" width="50%">
</div>

Acompaña a este Dashboard el [Informe](09.%20%20Informe.pdf) donde se presenta el Proyecto:

#### 1. Presentación

Se presentan un panorama preliminar y descriptivo de los Siniestros en la Cuidad de Buenos Aires y para mayor referencia se los ubica en el marco de los datos de siniestros Viales a nivel país, para toda Argentina.

La Ciudad Autónoma de Buenos Aires (CABA) es el centro administrativo y comercial del país. Tiene 3 millones de habitantes y cada día se producen cerca de 8,8 millones de viajes.
Durante 2019, casi el 50% de esos viajes se realizaron en transporte público, el 22% se hicieron en vehículos particulares y el 4% en bicicleta.

#### 2. Contexto

**Disminución de la Tasa de Mortalidad** <br>
La Ciudad de Buenos Aires propone en el Plan de Seguridad Vial 2020-2023 una reducción del 50% en las víctimas fatales para el año 2030.
Pero en este mismo contexto, se observa que para los peatones y mas en particular los motociclistas la evalución de la tasa de mortalidad no desciende como sería esperable para alcanzar los objetivos planteados.

#### 3. Descripción de la Brecha

En la Ciudad, 7 de cada 10 víctimas fatales son de género masculino, y 6 de cada 10 tienen entre 15 y 34 años de edad. Las características demográficas de las víctimas varían según el tipo de usuario. Entre los motociclistas y ocupantes de automóvil, la participación masculina es superior al 70%, mientras que, entre los peatones, su participación cae al 63%.
En cuanto a la edad, en el caso de los peatones las franjas que superan los 55 años de edad reúnen a la mayor cantidad de víctimas. Para los motociclistas y ocupantes de automóvil fallecidos, prevalece la franja de los 25 a 34 años.

Es por eso, que continuando con nuestro análisis y proceso, nos concentramos en este segmento de los datos, profundizando y focalizando el análisis.

#### 4. Motociclistas y Peatones

- El 75% de los accidentes de los motociclistas ocurren en calle y Avenidas, y en particular en la intersección o cruce.
- La fraja horaria donde se concentra la mayor cantidad de siniestros con motociclistas es entre las 6 y 7 am. Que es coincidente con el inicio de la jornada laboral.
- Esto representa el 50% del total de los accidentes fatales.

#### 5. Perfil de las Victimas de Siniestros fatales Motociclistas

**Perfil de Motociclistas**:

- **Distribución por Género**: Aproximadamente el **70%** de las víctimas de accidentes de motocicleta son **hombres** de entre **18 y 49 años**.
- **Grupos de Edad**: El mayor número de víctimas ocurre en el grupo de edad de **18 a 29 años**.
- **Tipo de Vehículos involucrados en los siniestros**: La mayoría de los accidentes involucran colisiones con **autos**, seguidos de **vehículos de pasajeros**, **vehículos de carga** (cargas) y otros tipos de vehículos.
- **Tasa de Mortalidad**: La tasa de mortalidad para motocicletas es de **9.82**¹.

#### 6. Plan de Seguridad Vial

En el año 2020, se lanzó un Segundo plan de Seguridad Vial en la Cuidad de Buenos Aires, manteniendo el anterior objetivo de **reducir un 20% las víctimas fatales por siniestros viales en la Ciudad para 2023**

Alineado con este objetivo, dispusimos de los siguientes 3 objetivos de plazo intermedio, para el seguimiento del Plan:

<div style="text-align:center;">
    <img src="02.%20imagenes/Objetivos.JPG" alt="Objetivos" width="50%">
</div>

## 1. Reducir un 10% la tasa de muertes en siniestros viales de los últimos seis meses contra el semestre anterior

La tasa de muertes en la Cuidad de Buenos Aires es un tercio de la Tasa de Mortalidad en siniestros viales de Argentina y la mitad que la de la Provincia de Buenos Aires.
También continua siendo baja incluso si la comparamos contra la tasa de mortalidad de Ciudades como Madrid, que es de 2.2.en el 2021, contra un 1.85 para la Cuidad de Buenos Aires

## 2. Reducir un 7% la cantidad de accidentes mortales de motocilistas en el último año versus el año anterior

Siendo que el 47% de los accidentes que ocurren involucran a motociclistas como víctimas o participes, enfocarse en reducir la cantidad de accidentes de este grupo con políticas y campañas acorde tendrá un impacto directo en el total de la tasa de mortalidad también, por eso sumamos este objetivo al plan de trabajo.

## 3. Alcanzar una reducción del 10% en la cantidad de muertes de peatones en la vía póblica respecto del último año.

Segundos, debajo pero no muy lejos, con el 37% del total de los accidentes están lo peatones.
Este grupo, al igual que los motociclistas son el segundo grupo de riesgo.

## 7. Dashboard - Resumen de Indicadores y Dashboard

El Dashboard se basa en el informe del Observatorio de Movilidad y Seguridad Vial de Buenos Aires del año 2021, que señala un total de 96 víctimas fatales en siniestros viales, predominantemente hombres entre 25 y 54 años, con motociclistas como el grupo más afectado.

#### 1. Tasa de Mortalidad

La tasa de mortalidad muestra una tendencia a la baja en los últimos cuatro años, incluso considerando el impacto de la pandemia de COVID-19.

#### 2. Años Promedio entre Muertes

Este indicador proporciona la frecuencia promedio de muertes en un período de tiempo dado, permitiendo comparaciones y análisis temporales.

#### 3. Variación Porcentual Promedio 4 Años

Muestra cómo el número de muertes en un período específico difiere de la tendencia promedio observada en un período más largo.

#### 4. Porcentaje de Muertes Motociclistas

Destaca que el 47% de las muertes en siniestros viales involucran a motociclistas, justificando un enfoque específico en este grupo.

#### 5. Porcentaje de Muertes Peatones

Con el 34% de las muertes, los peatones son el segundo grupo más vulnerable, lo que subraya la importancia de considerar medidas de seguridad para ellos.

### 8. Informe Final:

Se puede encontrar el mismo en [Informe Final y Dashboard](09.%20%20Informe.pdf)

| Conclusiones                             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ---------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ![Obelisco](02.%20imagenes/obelisco.JPG) | Según el informe estadístico del Observatorio de Movilidad y Seguridad Vial de la Ciudad de Buenos Aires, durante el año 2021 se registraron 96 víctimas fatales en 96 hechos. Más de tres cuartas partes de las víctimas fatales fueron de sexo masculino (77%) y el 49% tenían entre 25 y 54 años de edad. En relación al tipo de usuario/a de la vía fallecido, casi la mitad fueron motociclistas (48%) seguidos por los peatones (34%) y ocupantes de automóvil (11%). |

En suma, casi nueve de cada diez personas fallecidas (88%) en siniestros viales fueron usuario/as vulnerables de la vía (motociclistas, peatones, peatonas y ciclistas).

Respecto a 2020, se observa una reducción de las víctimas fatales peatonales y ocupantes de automóvil y un incremento en ocupantes de motos, permaneciendo sin cambios la cantidad de ciclistas fallecidos en siniestros viales. |

#### Propuestas: **Motociclistas**

- **Alto Riesgo para Hombres**: Los datos destacan que los hombres entre 18 y 49 años son particularmente vulnerables a los accidentes de motocicleta. Este grupo demográfico debería ser el foco de campañas de seguridad y programas de concientización.
- **Patrones de Colisión**: La prevalencia de accidentes que involucran autos y vehículos de carga sugiere la necesidad de mejorar las medidas de seguridad vial, especialmente en intersecciones y áreas con tráfico pesado.
- **Medidas de Seguridad**: Fomentar el uso de casco, licencias adecuadas y técnicas de conducción defensiva puede reducir significativamente las muertes y lesiones.

En resumen, abordar las necesidades específicas de los conductores masculinos en el grupo de edad de 18 a 49 años, promover prácticas de conducción seguras y mejorar la infraestructura vial pueden contribuir a reducir las víctimas de accidentes de motocicleta en la Ciudad de Buenos Aires.
