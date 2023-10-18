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
