import json

from pathlib import Path
from css_html_js_minify import html_minify
from jinja2 import (
    Environment,
    FileSystemLoader,
    select_autoescape,
    TemplateNotFound,
)

# Prepare Templates
env = Environment(
    loader=FileSystemLoader("src/templates"),
    autoescape=select_autoescape(["html", "xml"]),
)

# Get Data
with open("data.json", "r") as fp:
    data = json.load(fp)

# Render Templates
root = Path("dist")
if not root.exists():
    root.mkdir()

for f in Path("./src/templates").iterdir():
    try:
        temp = env.get_template(f.name)
        rendered = temp.render(data)
        root.joinpath(f.name).write_text(rendered)
    except TemplateNotFound as e:
        print(f"Template not found: {e}")
    except Exception as e:
        print(e)