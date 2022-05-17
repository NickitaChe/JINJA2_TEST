from jinja2 import Template

data = '''
{%raw%}

{{name}}

{%endraw%}
'''

tm = Template(data)
msg = tm.render(name = 'Aasfa')
print(msg)

link = ''' ссылки в html:
<a href="#">Ссылка</a>
'''
tm = Template(link)
msg = tm.render()
print(msg)

