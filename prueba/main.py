import random

import api
import files
import html_constructor

import css_template
import icon

url = "https://aves.ninjas.cl/api/birds"

response_text = api.request_get(url)
response = api.unpack_response(response_text)
random.shuffle(response)

html = html_constructor.html_constructor(response)

files.make_files('html/assets/img/icon.svg', icon.icon_svg)
files.make_files('html/assets/css/style.css', css_template.css)
files.make_files('html/index.html', html)