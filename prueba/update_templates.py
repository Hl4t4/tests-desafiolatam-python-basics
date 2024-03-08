from string import Template

def update_template(html_template, name, new_string):
    """Esta funcion substituye los datos de un template
    Parameters
    ----------
    string_template: [Template]
        Template de html a modificar
    name: [str]
        String con el nombre del identificador a modificar
    new_string: [str]
        String con los datos a reemplazar
    Returns
    ----------
    [str]
        Retorna un string de un html
    """
    return html_template.safe_substitute({name: new_string})

def template_html_base(base):
    """Esta funcion substituye los datos de un template
    Parameters
    ----------
    base: [str]
        String con los datos a reemplazar
    Returns
    ----------
    [str]
        Retorna un string con la base de un html modificable
    """
    return update_template(Template("$base"), "base", base)

def image_pack_stringify(main_image_template, thumb_image_template, image_pack):
    """Esta funcion transforma datos de imagenes en un string de html
    Parameters
    ----------
    main_image_template: [str]
        Template con los indicadores a reemplazar para una imagen principal
    thumb_image_template: [str]
        Template con los indicadores a reemplazar para una imagen secundaria
    image_pack: [list]
        Listado de diccionarios con datos de imagenes
    Returns
    ----------
    [str]
        Retorna un string con el html de hasta 6 imagenes contiguas
    """
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
    """Esta funcion transforma datos de imagenes en un string de html
    Parameters
    ----------
    carousel_item_template: [str]
        Template con los indicadores a reemplazar para un item de carousel
    main_image_template: [str]
        Template con los indicadores a reemplazar para una imagen principal
    thumb_image_template: [str]
        Template con los indicadores a reemplazar para una imagen secundaria
    image_pack: [list]
        Listado de diccionarios con datos de imagenes
    Returns
    ----------
    [str]
        el contenido de los multiples carousel items que pueden ser creados
    """
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
            images = update_template(Template(images), "tabs", "")
            active = False
        else:
            images = update_template(Template(images), "tabs", "\t\t\t\t\t\t\t\t")
            images = update_template(Template(images), "active", "")
            images = update_template(Template(images), "lazy", 'loading="lazy"') #Agregado para que las imagenes carguen solo de forma lazy
        carousels.append(images)
    return "\n".join(carousels)