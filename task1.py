from jinja2 import Template

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

per = Person("Фёдор", 33)

tm = Template("Мне {{p.age}} Лет и зовут {{p.name}}")
msg = tm.render(p = per)

print(msg)



per = {'name': 'Фёдор','age':34}

tm = Template("Мне {{p['age']}} Лет и зовут {{p.name}}")
msg = tm.render(p = per)

print(msg)
