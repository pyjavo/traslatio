import petl as etl

datos = etl.fromjson('items.jsonl', lines=True)

# <class 'petl.io.json.JsonView'>
# print('La variable datos es de tipo: ', type(datos))
# print('El lenght de los datos: ', len(datos))  # 856,383

#print(datos[0])  # ('title', 'url', 'date', 'category')

print(
	'Revisar la cantidad de visitas de cada url para luego,'
	'crear el campo **view_count**'
)
print(datos[1][1], end='\n\n')  # url del item 1
print(datos[2][1], end='\n\n')
print(datos[3][1], end='\n\n')

'''
# Parece que los números de visitas demoran en cargar en la página
Lo carga por axios un script llamado visitas.js que consulta la URL

nota: 
	https://www.biobiochile.cl/noticias/nacional/chile/2018/05/03/diputadas-del-pc-ingresan-proyecto-que-integra-concepto-de-consentimiento-en-violaciones.shtml
idNota: 3684164 
	---> están en el header de la noticia <head data-id-nota="3684164">


https://contador.biobiochile.cl/api/visitas/get-visitas?idNota=3684164&nosumar=true

respuesta:
[{"NotaId":3684164,"Fecha":{"$date":{"$numberLong":"1525406664"}},"Categorias":["chile","region-metropolitana"],"Tags":["santiago","violacion","region-metropolitana","modificacion","consentimiento"],"Visitas":11277}]


Debido a esto, en vez de 800k peticiones, se deben hacer 1.6M de peticiones. SI cada una dura 1 seg, eso se traduce en 444 horas, es decir, 18.5 días.




'''


'''


<div class="post-visits-container ml-auto">
    <span class="post-visits">516</span> visitas
</div>

<div class="post-visits-container ml-auto">
    <span class="post-visits">12,005</span> visitas
</div>
<div class="post-visits-container ml-auto">
    <span class="post-visits">11,276</span> visitas
</div>


'''

