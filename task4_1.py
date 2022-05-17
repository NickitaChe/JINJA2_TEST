from jinja2 import Environment,FunctionLoader


persons = [
    {"name": "Alex", "old":18, "weight":80.5 },
    {"name": "Nicola", "old":25, "weight": 78.4},
    {"name": "Ivan", "old":33, "weight": 99.3}]

def loadTpl(path):
    if path == "index":
        return """Имя {{u.name}}, возраст {{u.old}}"""
    else:
        return '''ДАнные: {{u}}'''


file_loader = FunctionLoader(loadTpl)
env = Environment(loader=file_loader)

tm = env.get_template('index')
msg = tm.render(u = persons[0])

print(msg)