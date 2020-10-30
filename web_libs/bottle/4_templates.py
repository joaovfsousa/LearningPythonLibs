from bottle import jinja2_view, route, run, request, response


@route("/<area>")
@jinja2_view('pages/tests.html')
def tests(area):
  return dict(name=area)


@route("/user", method="GET")
@jinja2_view("pages/user.html")
def user():
  links = ["home", "about", "help"]

  return dict(links=links)


@route("/user", method="POST")
@jinja2_view("pages/user.html")
def user_post():
  username = request.forms.get("username")
  password = request.forms.get("password")

  if username == "eduardo" and password == "senha" or \
     request.get_cookie("user") == "eduardo":

    response.set_cookie("user", "eduardo")
    links = ["home", "about", "help", "metrics"]

    return dict(string="Você está logado", links=links)

  else:
    response.set_cookie("user", "None")
    links = ["home", "about", "help"]
    return dict(string="Erro, você não está logado.", links=links)


run(port=8080, reloader=True)
