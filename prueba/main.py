import random

import api
import files
import html_constructor

import css_template
import icon

#Url de la api a usar
url = "https://aves.ninjas.cl/api/birds"

#Se solicitan los datos de la api
response_text = api.request_get(url)
#Se reorganizan y eliminan algunos datos no usados
response = api.unpack_response(response_text)
#Se desordenan los datos para que cada vez que se crea la pagina las imagenes carguen distintas
random.shuffle(response)

#Se invoca al constructor del html
html = html_constructor.html_constructor(response)

#Finalmente se crean los archivos necesarios el icono, css y html
files.make_files('html/assets/img/icon.svg', icon.icon_svg)
files.make_files('html/assets/css/style.css', css_template.css)
files.make_files('html/index.html', html)