from bottle import run, route


@route('/')
def index():
  """Static route for index page."""
  return "<h1>Hello World</h1>"


@route("/tests")
def tests():
  """Static route for tests page."""
  return "<h1>Testes</h1>"


@route("/<person>")
def person(person):
  """Dinamic route for person's page"""
  if person == "Pedro":
    return "<h1>Você não é bem vindo.</h1>"
  return f"<h1>Olá {person}</h1>"


run(port=8080)
