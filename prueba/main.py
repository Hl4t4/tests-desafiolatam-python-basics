import json
import requests
from string import Template
from icon import icon_svg
import random
import os



def request_get(url):
    return json.loads(requests.get(url).text)

def unpack_response(response_text):
    dictionary = [{"uid":response["uid"], "name":response["name"], "images":response["images"]} for response in response_text]
    return dictionary

def update_template(string_template, name, new_string):
    return string_template.safe_substitute({name: new_string})

def template_html_base(base):
    return update_template(Template("$base"), "base", base)

def image_pack_stringify(main_image_template, thumb_image_template, image_pack):
    new_strings = []
    i = 0
    for image in image_pack:
        if i == 0:
            new_string = str(main_image_template)
            new_string = update_template(Template(new_string), "full", image["images"]["full"])
        else:
            new_string = str(thumb_image_template)
            new_string = update_template(Template(new_string), "thumb", image["images"]["thumb"])
        if i == len(image_pack)-1:
            new_string = update_template(Template(new_string), "last", "d-none d-lg-none d-xxl-flex")
        else:
            new_string = update_template(Template(new_string), "last", "")
        i += 1
        new_string = update_template(Template(new_string), "uid", image["uid"])
        new_string = update_template(Template(new_string), "spanish", image["name"]["spanish"])
        new_string = update_template(Template(new_string), "english", image["name"]["english"])
        new_string = update_template(Template(new_string), "latin", image["name"]["latin"])
        new_strings.append(new_string)
    return "\n".join(new_strings)

def substitute_image_pack(carousel_item_template, main_image_template, thumb_image_template, image_pack):
    carousels = []
    active = True
    while (image_pack != []):
        image_pack_to_substitute = []
        if len(image_pack) < 6:
            for i in range(len(image_pack)):
                image_pack_to_substitute.append(image_pack.pop())
        else:
            for i in range(6):
                image_pack_to_substitute.append(image_pack.pop())
        images = image_pack_stringify(main_image_template, thumb_image_template, image_pack_to_substitute)
        images = update_template(Template(carousel_item_template), "images", images)
        if active:
            images = update_template(Template(images), "active", "active")
            active = False
        else:
            images = update_template(Template(images), "active", "")
            images = update_template(Template(images), "lazy", 'loading="lazy"') #Agregado para que las imagenes carguen solo de forma lazy
        carousels.append(images)
    return "\n".join(carousels)

url = "https://aves.ninjas.cl/api/birds"

base = """<!DOCTYPE html>
<html lang="es">
\t<head>
\t\t$head
\t</head>
\t<body class="bg-primary-subtle">
\t\t$body
\t</body>
</html>"""

head = """<meta charset="UTF-8">
        <meta name="description" content="Aves de Chile / Birds from Chile">
        <meta name="keywords" content="Aves, Birds, Chile">
        <meta name="author" content="Jose Latapiatt">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="icon" type="image/x-icon" href="assets/img/icon.svg">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
        <script src="https://kit.fontawesome.com/c8ed5828b7.js" crossorigin="anonymous"></script>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-C6RzsynM9kWDrMNeT87bh95OGNyZPhcTNXj1NW7RuBCsyN/o0jlpcV8Qyq46cDfL" crossorigin="anonymous"></script>
        <link rel="stylesheet" href="assets/css/style.css">
        <title>Aves de Chile / Birds from Chile</title>"""

header ="""<nav class = "navbar navbar-expand-lg px-md-5">
                \t<a class="navbar-brand ps-md-5" href="#"><i class="fa-solid fa-dove fa-xl px-md-3 text-light"> BFC</i></a>
                \t<button class="navbar-toggler" style="border-color: white;" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                \t\t<span class="navbar-toggler-icon"></span>
                \t</button>
                \t<div class="collapse navbar-collapse ps-3 pe-md-5" id="navbarNav">
                \t\t<div class="navbar-nav ms-auto">
                \t\t\t<a class="nav-link text-light" href="#inicio">Inicio</a>
                \t\t\t<a class="nav-link text-light" href="#centro">Centro</a>
                \t\t\t<a class="nav-link text-light" href="#contacto">Contacto</a>
                \t\t</div>
                \t</div>
                </nav>"""

# $active = "active" | ""

section ="""<div class="row py-5">
                    \t<div class="col">
                    \t<h1 class="text-center pb-4">Bienvenidos a Birds from Chile (BFC)!</h1>
                    \t\t<div id="headerCarousel" class="carousel slide" data-bs-ride="carousel">
                    \t\t\t<div class="carousel-inner">
                    \t\t\t\t$carousels
                    \t\t\t</div>
                    \t\t</div>
                    \t</div>
                    </div>"""

carousel_item_template="""\t\t\t\t<div class="carousel-item $active" data-bs-interval="3000">
                    \t\t\t\t\t<div class="container-fluid">
                    \t\t\t\t\t\t<div class="row">
                    \t\t\t\t\t\t\t$images
                    \t\t\t\t\t\t\t\t</div>
                    \t\t\t\t\t\t\t</div>
                    \t\t\t\t\t\t</div>
                    \t\t\t\t\t</div>
                    \t\t\t\t</div>"""

main_image_template = """\t\t\t\t\t\t\t<div class="col-md-8 col-xs-12 col-sm-12 col-12 border border-danger px-0 text-center">
                    \t\t\t\t\t\t\t\t<img $lazy class="img-fluid pb-3" src="$full" alt="$uid">
                    \t\t\t\t\t\t\t\t<h2>Nombre Especie: <i>$spanish</i></h2>
                    \t\t\t\t\t\t\t\t<h2>Species Name: <i>$english</i></h2>
                    \t\t\t\t\t\t\t\t<h2>Nombre Cientifico: <i>$latin</i></h2>
                    \t\t\t\t\t\t\t</div>
                    \t\t\t\t\t\t\t<div class="col-md-4 col-xs-12 col-sm-12 col-12 mt-md-0 mt-sm-3 mt-3">
                    \t\t\t\t\t\t\t\t<div class="row d-flex h-100 ps-md-3 ps-sm-1 ps-1 row-gap-2" style="flex-direction: column-reverse; justify-content: space-between;">"""

# $last = "d-none d-lg-none d-xxl-flex" | ""

thumb_image_template = """\t\t\t\t\t\t\t\t\t<div class="row $last border border-danger ps-0 mx-0">
                    \t\t\t\t\t\t\t\t\t\t<div $lazy class="col-7 px-0">
                    \t\t\t\t\t\t\t\t\t\t\t<img class="img-fluid" src="$thumb" alt="$uid">
                    \t\t\t\t\t\t\t\t\t\t</div>
                    \t\t\t\t\t\t\t\t\t\t<div class="col-5 pe-0 align-self-center">
                    \t\t\t\t\t\t\t\t\t\t\t<p>Nombre Especie: $spanish</p>
                    \t\t\t\t\t\t\t\t\t\t\t<p>Species Name: $english</p>
                    \t\t\t\t\t\t\t\t\t\t\t<p>Nombre Cientifico: $latin</p>
                    \t\t\t\t\t\t\t\t\t\t</div>
                    \t\t\t\t\t\t\t\t\t</div>"""

footer = """<div class="row text-light py-md-4 py-4 pb-2 px-1 px-md-5">
                \t<div class="col-6 text-start ps-2 ps-md-5">
                \t\t<i class="fa-solid fa-dove fa-2xl text-light"> BFC</i>
                \t</div>
                \t<div class="col-6 text-end mt-2 pe-2 pe-md-5">
                \t\t<a href="https://www.github.com">
                \t\t\t<i class="fa-brands fa-square-github fa-2xl text-light align-top"></i>
                \t\t</a>
                \t\t<a href="https://www.linkedin.com">
                \t\t\t<i class="fa-brands fa-linkedin fa-2xl ps-1 text-light align-top"></i>
                \t\t</a>
                \t\t<a href="https://www.twitter.com">
                \t\t\t<i class="fa-brands fa-square-twitter fa-2xl ps-1 text-light align-top"></i>
                \t\t</a>
                \t\t<a href="https://www.facebook.com">
                \t\t\t<i class="fa-brands fa-square-facebook fa-2xl ps-1 text-light align-top"></i>
                \t\t</a>
                \t</div>
                </div>"""


body = """<header id="inicio" class="container-fluid bg-danger text-white">
        \t$header
        </header>
        <section id="centro" class="container-fluid bg-secondary-subtle text-secondary-subtle">
        \t$section
        </section>
        <footer id="contacto" class="container-fluid bg-danger text-white px-2 px-md-5">
        \t$footer
        </footer>"""

css = """p {
            font-size:14px;
}"""

response_text = request_get(url)
response = unpack_response(response_text)
random.shuffle(response)

carousels = substitute_image_pack(carousel_item_template, main_image_template, thumb_image_template, response)

html = Template(template_html_base(base))
html = Template(update_template(html, "head", head))
html = Template(update_template(html, "body", body))
html = Template(update_template(html, "header", header))
html = Template(update_template(html, "section", section))
html = Template(update_template(html, "carousels", carousels))
html = update_template(html, "footer", footer)

os.makedirs('html/assets/img', exist_ok=True)
os.makedirs('html/assets/css', exist_ok=True)

with open('html/assets/img/icon.svg', 'w') as f:
    f.write(icon_svg)

with open('html/assets/css/style.css', 'w') as f:
    f.write(css)

with open('html/index.html', 'w', encoding='utf-8') as f:
    f.write(html)