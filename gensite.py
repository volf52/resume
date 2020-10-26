import json

from pathlib import Path

from css_html_js_minify import html_minify
from jinja2 import Template

SOURCE = Path("./src")

temp = Template((SOURCE / "_base.html").read_text())

with open("data.json", "r") as fp:
    data = json.load(fp)

normal = temp.render(data)
print(normal)

print("-" * 15)
mini = html_minify(normal)
print(mini)
