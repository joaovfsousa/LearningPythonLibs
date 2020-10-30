"""Using cookies"""
from bottle import request, route, run, response


@route('/')
def hello_again():
  if request.get_cookie("visited"):
    return "Olá, bem vindo de volta"
  response.set_cookie("visited", "yes")
  return "Olá, é um prazer conhecer você."


run(port=8080, reloader=True)
