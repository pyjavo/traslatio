# Notas traslatio

#### Sobre scrapping

El scraping lo haré en otra versión del proyecto


- Hay 856,382 registros
- Se pueden cargar en bigquery
```SQL
SELECT COUNT(*) AS row_count FROM `traslatio.items_raw.items`
```

- Parece que los números de visitas demoran en cargar en la página. Lo carga por axios en un script llamado `visitas.js` que consulta otra URL.
- Guardaré el id de cada nota
    - están en el header de la noticia. Por ejemplo:
        - https://www.biobiochile.cl/noticias/nacional/chile/2018/05/03/diputadas-del-pc-ingresan-proyecto-que-integra-concepto-de-consentimiento-en-violaciones.shtml
        - `<head data-id-nota="3684164">`
        - https://contador.biobiochile.cl/api/visitas/get-visitas?idNota=3684164&nosumar=true
        - Devuelve:
        ```js
        [{"NotaId":3684164,"Fecha":{"$date":{"$numberLong":"1525406664"}},"Categorias":["chile","region-metropolitana"],"Tags":["santiago","violacion","region-metropolitana","modificacion","consentimiento"],"Visitas":11300}]
        ````

        - https://www.biobiochile.cl/noticias/futbol-internacional/notas-futbol-internacional/2021/05/03/la-dura-ninez-de-shevchenko-entre-chernobyl-y-mudanzas-todos-mis-amigos-de-infancia-estan-muertos.shtml
        - idNota=4912524
        - https://contador.biobiochile.cl/api/visitas/get-visitas?idNota=4912524&nosumar=true
        - Devuelve
        ```js
        [{"NotaId":4912524,"Fecha":{"$date":{"$numberLong":"1620057501"}},"Categorias":["futbol-internacional","notas-futbol-internacional"],"Tags":["amigos","andriy-shevchenko","chernobyl","futbol","ucrania","union-sovietica"],"Visitas":7094}]
        ```
- A partir del JSON, guardaré el valor de las visitas (si no existe, podría entrar a scrapear el sitio web). La estructura para obtener ese dato luce de esta forma:
```html
<div class="post-visits-container ml-auto">
    <span class="post-visits">516</span> visitas
</div>

<div class="post-visits-container ml-auto">
    <span class="post-visits">12,005</span> visitas
</div>
<div class="post-visits-container ml-auto">
    <span class="post-visits">11,276</span> visitas
</div>
```

- Debido a que son 856k de registros aproximados, en vez de hacer 856k peticiones, se debe hacer el doble de peticiones, es decir, 1.7M. Si cada una dura 1 seg, eso se traduce en 444 horas, es decir, 18.5 días.


#### Análisis
```
# obtener URL a consultar
# hacer petición para obtener idNota de la noticia
# nueva peticion a endpoint para obtener visitas
# si no existe el campo 'Visitas' en el JSON, scrapear HTML de la noticia
# Si no existe dato de visitas en HTML, dejar como None
# actualizar BD con registro

# La pregunta ahora es si hacerlo local o hacerlo en 5 días en google cloud

######## Local ########

# Convertir datos de json en sqlite
# No tengo tantos core
# tendría que dejar mi laptop encendida bastante tiempo
# BD sería SQLite

######## Google Cloud ########

# Usaría bigquery
# recursos de la nube
# Usaría otra IP que no sea la mía
# tendría que lidiar con permisos en la nube
# Lidiar en como descargar los datos a SQLite
```


## Análisis para btener datos en csv

Ejecute el siguiente comando para obtener la BD en formato .CSV:

```bash
sqlite3 -header -csv biobio.db "select * from news;" > data.csv

sqlite3 -header -csv data/raw/biobio.db < src/data/make_csv.sql > data/raw/data.csv
```

Ya con esto podría usar pandas y analizarla en un notebook, pero debo primero limpiar un poco los datos. Puedo empezar haciendolo con SQL


```sql
SELECT COUNT(view_count) FROM news; # Hay en total 910,085 registros


###################################################################
############ Validar que 'view_count' solo sea números ############
###################################################################



SELECT COUNT(view_count) FROM news where printf("%d", view_count) = view_count;
## 910,077

SELECT view_count FROM news where printf("%d", view_count) = view_count; # selecciona solo los que son números


select view_count from news where abs(view_count) = 0.0 or view_count = '0' # esto me da los que tienen letras
# son 8 registros





##############################################################################
############ Obtener la columna current_date ############
##############################################################################


# SELECT date FROM news WHERE date IS strftime('%Y/%m/%d', date) LIMIT 200; # 0 records

# SELECT date FROM news WHERE CHECK(date IS strftime('%Y/%m/%d', date)) LIMIT 200; # error Result: near "CHECK": syntax error

# SELECT strftime('%Y/%m/%d', date) as myDate LIMIT 3; # 0 records


# generar fecha actual y fecha de creacion en el mismo query
SELECT DATE(); # 2023-10-19
SELECT DATE('now'); # 2023-10-19

SELECT url, title, category, date as created_date, DATE('now') as current_date, view_count from news;





##############################################################################
##################### Validar que category no sea vacío ######################
##############################################################################


SELECT COUNT(category) as cat_count FROM news WHERE category = ''; # 189 records son vacíos


#### ¿Cuántas noticias tienen solo la categoría de 'noticias'?
SELECT COUNT(category) as cat_count FROM news WHERE category='noticias'; # 475484 records
# es el 52.2% de las 910085 noticias




##############################################################################
####################### Validar que title no sea vacío #######################
##############################################################################


SELECT COUNT(title) as title_count FROM news WHERE title = '' # 0 records
SELECT COUNT(title) as title_count FROM news WHERE title = NULL # 0 records





#########################################################
############# Como crear una nueva tabla ################
#########################################################


CREATE TABLE news_v1 AS
SELECT Url, title, category, date as created_date, DATE('now') as current_date, view_count 
FROM news 
WHERE printf("%d", view_count) = view_count AND category != '';

```
