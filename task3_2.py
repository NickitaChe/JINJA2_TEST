from jinja2 import Template

persons = [
    {"name": "Alex", "old":18, "weight":80.5 },
    {"name": "Nicola", "old":25, "weight": 78.4},
    {"name": "Ivan", "old":33, "weight": 99.3}
]

html = '''
{%macro list_users(list_of_user) -%}
<ul>
{%for u in list_of_user -%}
    <li>{{u.name}}{{caller(u)}}
{%-endfor%}
</ul>
{%- endmacro%}

{%-call(user) list_users(users)-%}
 <ul>
 <li>age:{{user.age}}
 <Li>weight: {{user.weight}}
 </ul>
{%-endcall-%}
'''

tm = Template(html)
msg = tm.render(users = persons)

print(msg)