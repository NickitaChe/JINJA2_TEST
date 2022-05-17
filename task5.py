from jinja2 import Environment,FileSystemLoader


persons = [
    {"name": "Alex", "old":18, "weight":80.5 },
    {"name": "Nicola", "old":25, "weight": 78.4},
    {"name": "Ivan", "old":33, "weight": 99.3}]

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

tm = env.get_template('page.html')
msg = tm.render(users = persons,domain = 'localhost', title="Main")

print(msg)