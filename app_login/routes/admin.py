from flask import (
    Blueprint,
    render_template,
    request,
    redirect
)
from models import Usuarios
from flask_login import login_required

admin = Blueprint("admin", __name__, url_prefix="/dash", template_folder="../templates/admin")

@admin.route("/usuarios")
@admin.route("/usuarios/editar/<int:id_usuario>")
@login_required
def usuarios():
    lista_usuarios = Usuarios.query.all()

    for i in lista_usuarios:
        print(i.__dict__)
        break

    return render_template("home.html", usuarios=lista_usuarios)

@admin.route("/usuarios/editar/<int:id_usuario>")
def usuarios_edtar(id_usuario):
    usuario = Usuarios.query.filter_by(id=id_usuario).first()

    if usuario:
        return render_template("usuario.html", usuario=usuario)
    
    return redirect(request.path)


