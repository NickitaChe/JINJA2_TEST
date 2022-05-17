from jinja2 import Template
from markupsafe import escape

#экранирование
link = ''' ссылки в html:
<a href="#">Ссылка</a>
'''
tm = Template("{{link | e}}")
msg = tm.render(link = link)

print(msg)
msg = escape(link)
print(msg)
