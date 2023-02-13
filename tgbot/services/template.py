import re

from django.template.loader import render_to_string


def render_template(template_name: str, context: dict | None = None) -> str:
    if context is None:
        context = {}
    rendered: str = render_to_string(template_name, context).replace('\n', ' ')
    rendered = rendered.replace('<br>', '\n')
    rendered = re.sub(' +', ' ', rendered).replace(' .', '.').replace(' ,', ',')
    rendered = '\n'.join(line.strip() for line in rendered.split('\n'))
    rendered = rendered.replace('{FOURPACES}', '    ')
    return rendered
