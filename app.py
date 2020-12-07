from flask import Flask, render_template, request, redirect
import yagmail as yagmail
import utils
#Para indacarle desde donde se está ejecutando la aplicación
app = Flask(__name__)
tareas = []
#Decorador
@app.route("/")
def hola_mundo():
    return render_template('index.html', tareas=tareas)
@app.route("/registro", methods=('POST','GET'))
def registro():
    if request.method == 'POST':
        username =request.form.get('usuario')
        password = request.form.get('password')
        email = request.form.get('correo')

        if not utils.isUsernameValid(username):
            return render_template('registro.html')
        if not utils.isPasswordValid(password):
            return render_template('registro.html')
        if not utils.isEmailValid(email):
            return render_template('registro.html')

        yag = yagmail.SMTP('mintic2022@gmail.com', 'HolamundoMintic2020')  #SMTP protocolo de envío de correos      
        yag.send(to=email, subject='Activa tu cuenta', contents='Bienvenido, usa el link para activar tu cuenta')
        return render_template('login.html')
    return render_template('registro.html')    
@app.route("/agregar", methods=("GET","POST"))
def agregar():
    if request.method == "GET":
        return render_template("agregar.html")
    else:    
        tarea = request.form.get("tarea")
        tareas.append(tarea)
        return redirect("/")

