from string import Template
import update_templates
import html_templates

def html_constructor (response):
    carousels = update_templates.substitute_image_pack(html_templates.carousel_item_template, html_templates.main_image_template, html_templates.thumb_image_template, response)
    html = Template(update_templates.template_html_base(html_templates.base))
    html = Template(update_templates.update_template(html, "head", html_templates.head))
    html = Template(update_templates.update_template(html, "body", html_templates.body))
    html = Template(update_templates.update_template(html, "header", html_templates.header))
    html = Template(update_templates.update_template(html, "section", html_templates.section))
    html = Template(update_templates.update_template(html, "carousels", carousels))
    html = update_templates.update_template(html, "footer", html_templates.footer)
    return html