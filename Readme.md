# Análisis de Siniestralidad de la Cuidad De Buenos Aires

![Banner](02.%20imagenes/Banner_Buenos_Aires.jpg)

# 1. Descripción del Proyecto

El objetivo de este proyecto fue realizar un análisis de datos para el Observatorio de Movilidad y Seguridad Vial (OMSV) con el propósito de generar un Informe sobre la situación actual e histórica de los siniestros y victimas fatales en la Cuidad de Buenos Aires para el período 2016 a 2021, que le permita a las autoridades locales tomar medidas para disminuir la cantidad de víctimas fatales de los siniestros viales. .<br>

El producto de este análisis fue la creación de:

1. Un Dashboard para el seguimiento y gestión de los objetivos principales del **Plan de Seguridad Vial 2020-2030**
2. Recomendaciones para la implementación de medidas dentro del Plan de Seguridad Vial 2020-2030

# 2. Introducción

En _Argentina_ se registra un _promedio de 4.798 víctimas fatales_ por siniestros viales al año, lo que equivale a una _tasa de mortalidad de 10,73 cada 100.000 habitantes_. <br>
Mientras que en la **Ciudad Autónoma de Buenos Aires** se registra un **promedio de 119 víctimas fatales anuales**, lo que representa una **tasa de mortalidad de 3,87 cada 100.000 habitantes**. En conjunto, para el periodo 2016-2021 la Ciudad registró un total de 717 víctimas fatales por siniestros viales.

**El 82% de las víctimas fatales fueron usuarios vulnerables de la vía (42% motociclistas, 37% peatones y 3% ciclistas)**

# 3. Desarrollo del Proyecto

## 3.1. Datasets del Proyecto

El Dataset del proyecto se extrajo de la página de [Secretaría de Transporte y Obras Públicas](https://data.buenosaires.gob.ar/organization/transporte-y-obras-publicas) de la Cuidad de Buenos Aires.
Consiste en un archivo .xls con varias hojas.

Para el desarrollo del proyecto nos centramos en la hoja homicidios y complementamos la información con la hoja de víctimas.

### 3.1 ETL Homicidios

Durante el ETL procuramos explorar cada una de las variables del Dataset para eliminar valores duplicados, erroneos, o vacíos y preparar la data para el proceso de EDA.

Para ver el paso a paso de este proceso en detalle se puede consultar:

[ETL y EDA de homicidios](01.%20ETL_EDA_homicidios.ipynb)
En este notebook encontrarán el proceso completo con sus paso, transformaciones y al tiempo que se desarrollan descripciones y conclusiones de lo analizado y hallado para cada variable.

### 3.2 ETL Victimas

En el notebook [ETL Victimas](02.%20ETL_victimas.ipynb) pueden encontrar el paso a paso detallado de las transformaciones realizadas al dataset homicidios en la hoja victimas.<br>
Este dataframe es luego guardado en **victimas_etl.csv** para ser utilizado en el EDA de Homicidios.hechos como complementario a hechos_df.<br>

En este dataset encontramos de manera complementaria toda la información demográfica referente a las victimas:

- Edad
- Género

**Con esta información complementamos el Dataframe de homicidios, pudiendo realizar análisis mas completos sobre la demografía de las victimas, para caracterizar su perfil.**

## 3.2 EDA - Resumen del Análisis Exploratorio de Datos (EDA) sobre Siniestros Viales en la Ciudad de Buenos Aires

Durante el Análisis Exploratorio de Datos (EDA) del proyecto se realizó un análisis detallado de las variables disponibles, sus relaciones y sus tendencias.
En el notebook [ETL_EDA_homicidios](01.%20ETL_EDA_homicidios.ipynb) se encuentra el paso a paso, detalle, desarrollo, hallazgos y conclusiones de todo lo trabajado durante el desarrollo del EDA.

A continuación, resumo los hallazgos más importantes del EDA:

1. **Análisis Univariable de Homicidios**
   Se realizó un análisis univariable para cada variable del dataset, destacando los siguientes puntos:

- Analisis de la distribución de siniestros por año, mes y día.
- Observaciones de una tendencia a la baja en la cantidad de siniestros, con fluctuaciones debido a eventos como la pandemia de COVID-19.
- No se encontraron patrones claros en la distribución de siniestros por mes o día de la semana.

2. **Análisis Multivariable de Homicidios**
   Se exploró la relación entre variables y cómo afectan a la cantidad de siniestros:

- Se observó que el 75% de los siniestros ocurrieron en intersecciones de calles.
- Las Avenidas fueron el tipo de calle con más siniestros, 70% de las muertes.
- Los motociclistas (42% de las fatalidades) y peatones (37% de las fatalidades) fueron las víctimas más comunes en los siniestros, seguidos por los conductores de autos.
- Hubo una ligera tendencia a un mayor número de muertes durante los fines de semana en comparación con los días laborables.

3. **Evolución de la Cantidad de Siniestros**

- Se analizó la evolución de la cantidad de siniestros por año y por tipo de calle.
- Observando una tendencia a la baja en la cantidad de siniestros en general, aunque con fluctuaciones debido a eventos externos como la pandemia.
- Nuevamente se volvió a evidenciar que Las muertes de motociclistas representaron la mayoría de las muertes a lo largo de los años, siendo este el grupo mas vulnerable de manera constante.
- Los peatones se ubican en segundo lugar y finalmente los conductores de autos.

4. **Distribución de Muertes por Edad y Género**

- Se observa que el **rango etario de 30-49 años representan el 30% de las muertes**, siendo el Rango Etario mas vulnerable.
- Las personas entre los **18-29 años** representan el segundo grupo mas vulnerable, con el **23% de las muertes**
- Las fatalidad en los hombres es significativamente mayor que en las mujeres para todos los años y combinaciones analizados.
  - El **75% de las victimas fatales son hombres.**
- Se realizó un análisis detallado de la distribución de muertes por edad y género, destacando diferencias significativas entre grupos de edad y género.
  - El **32% de las victimas son hombres de entre de 30-49 años representan**
  - El **27% de las victimas fueron hombres en 18-29 años**.

5. **Ocurrencia de Muertes por Franja Horaria**

<div style="text-align:center;">
    <img src="02.%20imagenes/Franja_horaria.JPG" alt="Franja_Horaria" width="40%">
</div>

- Se realizó un análisis detallado de la incidencia del horario en la ocurrencia del siniestro, pero **no se encontraron patrones concluyentes**.

Igualmente, se identificaron momentos del día con mayor frecuencia de muertes, tanto para motociclistas como para peatones:

- Las _tardes de miércoles y viernes_ son periodos críticos con una alta incidencia de muertes.

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

En resumen, primero se guardaron los Dataframe resultantes del proceso de ETL y EDA en formato .csv.

Estos son:

1. **homicidios_etl.csv** : son los registros de los homicidios por número de siniestro y toda la información relevante, luego de la limpieza y transformacion de los datos.
2. **victimas_completo.csv**: es el dataframe donde se vinculan las victimas cada una identificada y asociada a su id de siniestro con la informacion adicional del género, edad y rango etario definido como información más relevante y complementaria a homicidios.

Segundo, se creó en MySQL Workbench la Database, que llamamos proyecto_individual_02.

Tercero, se conectó Python con MySQL, para que desde Python, con la base de datos ya creada, pudieramos crear y migrar con tan sólo unas pocas líneas de código las Tablas que serían nuestra base de Datos y posterior recursos en Power Bi.

Ultimo, tocó conectar la Base de Datos de MySQL con Power BI, en el notebook [Connection_mysql](06.%20Connection_msql.ipynb) se encuentra el instructivo para replicar lo que es la creación y la conexión en caso de que quisieran utilizarla o explorarla.

Con esto quedamos listos para comenzar a crear el Dashboard y todas las visualizaciones.

## 5. Dashboard

[Dashboard_Siniestros_Viales_2021](07.%20Dashboard.pbix)

<div style="text-align:center;">
    <img src="02.%20imagenes/Dashboard.JPG" alt="Dashboard" width="50%">
</div>

### Selección y Presentación de Indicadores

En el marco del Plan de Seguridad Vial 2020-2023, La Ciudad de Buenos Aires propone en una reducción del 50% en las víctimas fatales para el año 2030.
Como se presenta en el [Informe](09.%20%20Informe.pdf), el principal desafío que se presenta para alcanzar este objetivo es reducir la tasa de mortalidad, o la cantidad de muertes de los dos principales grupos más vulnerables detectados durante el desarrollo del proyecto:

- Hombres de entre de 30-49 años que representan el **32% de las victimas**
- Los Hombre entre 18-29 años, **27%**.

Esta es el eje principal en la selección de los indicadores para el Dashboard.

Presentamos cada uno de ellos y el propósito para su implementación:

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

## 6. KPIS

En el año 2020, se lanzó un _Segundo Plan de Seguridad Vial en la Cuidad de Buenos Aires_, manteniendo el anterior objetivo de **reducir un 20% las víctimas fatales por siniestros viales en la Ciudad para 2023**

Alineado con este objetivo, se dispusieron los siguientes 3 objetivos de plazo intermedio, para el seguimiento del Plan:

## 1. Reducir un 10% la tasa de muertes en siniestros viales de los últimos seis meses contra el semestre anterior

| KPI # 1                              | Tasa de Mortalidad accidentes viales                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ![KPI 1](02.%20imagenes/KPI%201.JPG) | La tasa de muertes en la Cuidad de Buenos Aires es un tercio de la Tasa de Mortalidad en siniestros viales de Argentina (10.87 para el 2021) y la mitad que la de la Provincia de Buenos Aires (3.5 en 2021). Asimismo, incluso si se la compara contra la tasa de mortalidad de siniestros viales de Ciudades como Madrid, que es de 2.2.en el 2021, los resultados impresionan positivos. Es por ello que el seguimiento de la tasa de muertes, o tasa de mortalidad es un indicador clave. |
|                                      |

## 2. Reducir un 7% la cantidad de accidentes mortales de motocilistas en el último año versus el año anterior

| KPI # 2                           | Cantidad de Muertes motociclistas                                                                                                                                                                                                                                                                                                                                                                                                   |
| --------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ![KPI 2](02.%20imagenes/KPI2.JPG) | Siendo que el 47% de los accidentes que ocurren involucran a motociclistas como víctimas o participes, se vuelve inminente enfocarse en reducir la cantidad de accidentes de este grupo. Es por ello que el foco del proyecto fue idenficarlo y caracterizarlo . Este grupo representa el 42% del total, con lo cual una reducción porcentual del 10% en este grupo impactaría en un 5% sobre el resultado en la tasa de mortalidad |
|                                   |

## 3. Alcanzar una reducción del 10% en la cantidad de muertes de peatones en la vía póblica respecto del último año.

| KPI #3                            | Peatones                                                                                                                                                                                                                                                                                                                                                                                                           |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| ![KPI 2](02.%20imagenes/KPI3.JPG) | Segundos, debajo pero no muy lejos, con el 37% del total de los accidentes están lo peatones. Este grupo, es el segundo grupo de riesgo. A difenrecia de las motos, que tienen un ragno etario mas prominente, este grupo tiene una distribución mas uniforme por edad. Nuevemente, podemos establecer que una reducción porcentual del 10% en este grupo representa el 80% del cumpliento del objetivo principal. |

Acompaña a este Dashboard el [Informe](09.%20%20Informe.pdf) donde se presenta el Proyecto.

### 8. Conclusiones:

| Conclusiones                             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ---------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ![Obelisco](02.%20imagenes/obelisco.JPG) | Según el informe estadístico del Observatorio de Movilidad y Seguridad Vial de la Ciudad de Buenos Aires, durante el año 2021 se registraron 96 víctimas fatales en 96 hechos. Más de tres cuartas partes de las víctimas fatales fueron de sexo masculino (76%) y el 59% tenían entre 18 y 49 años de edad. En relación al tipo de usuario/a de la vía fallecido, casi la mitad fueron motociclistas (42%) seguidos por los peatones (37%) y ocupantes de automóvil (11%). |

En suma, ocho de cada diez personas fallecidas (80%) en siniestros viales fueron usuario/as vulnerables de la vía, motociclistas o peatones.

Respecto a 2019, para excluir el 2020 que tiene la particularidad del cierre por la pandemia, se observa una reducción de las víctimas fatales peatonales, ocupantes de automóvil y motociclistas, permaneciendo sin cambios la cantidad de ciclistas fallecidos en siniestros viales. |

Resumiendo los hallazgos, pudimos identificar al grupo mas vulnerable:

#### Perfil del Motociclista:

- **Alto Riesgo para Hombres**: Los datos destacan que los hombres entre 18 y 49 años son particularmente vulnerables a los accidentes de motocicleta. Este grupo demográfico debería ser el foco de campañas de seguridad y programas de concientización.
- **Patrones de Colisión**: La prevalencia de accidentes que involucran autos y vehículos de carga sugiere la necesidad de mejorar las medidas de seguridad vial, especialmente en intersecciones y áreas con tráfico pesado.
- **Medidas de Seguridad**: Fomentar el uso de casco, licencias adecuadas y técnicas de conducción defensiva puede reducir significativamente las muertes y lesiones.

En resumen, abordar las necesidades específicas de los conductores masculinos en el grupo de edad de 18 a 49 años, promover prácticas de conducción seguras y mejorar la infraestructura vial pueden contribuir a reducir las víctimas de accidentes de motocicleta en la Ciudad de Buenos Aires.

# 9. Recursos:

[Funciones para el ETL](funciones.py)
En este link se encuentran las funciones que escribí para realizar varias de las operaciones de limpieza, análisis y transformación del dataset homicidios y victimas utilizados en el proyecto.

[Estadística y Censos | Buenos Aires Ciudad](https://www.estadisticaciudad.gob.ar/eyc/?cat=132)<br>

[Proyección de población por sexo y edad simple](https://www.estadisticaciudad.gob.ar/eyc/?p=135617)

[Informe del proyecto Salud Urbana en América Latina (Salurbal)](https://www.youtube.com/watch?v=aUM9cxbz_-s)

[red de bicicletas de la ciudad de Buenos Aires](https://www.lanacion.com.ar/autos/tendencias/los-datos-mas-curiosos-de-la-red-de-bicicletas-de-la-ciudad-de-buenos-aires-nid20032023/)

[Secretaría de Transporte y Obras Públicas](https://data.buenosaires.gob.ar/organization/transporte-y-obras-publicas)

[Bastrap 7.1](https://gcba.github.io/BAstrap/#introduccion)

[Beyond Defaults: Using Custom Fonts in Power BI](https://medium.com/microsoft-power-bi/beyond-defaults-using-custom-fonts-in-power-bi-b2b341fd323e)
