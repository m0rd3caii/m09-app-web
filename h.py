from flask import Flask
from flask import render_template
from flask import request
import datos
from flask import Flask, redirect, url_for, request

app = Flask(__name__)
datos.conn
datos.mydb

@app.route('/mail/<name>')
def mail(name):
   result = datos.get_data(name)
   resultado = True
   return render_template('getmailform.html', result = result, resultado = resultado)
    

@app.route('/getmail',methods = ['POST', 'GET'])
def getmail():
   if request.method == 'POST':
      user = request.form['name']
      #logica buscar el mail y render result
      return redirect(url_for('mail',name = user))
   else:
      user = request.args.get('name')
      return render_template('getmailform.html')


@app.route('/addmail',methods = ['POST', 'GET'])
def addmail():
   if request.method == 'POST':
      user = request.form['name']
      mail = request.form['mail']
      datos.add_data(user,mail)
      resultado = True
      return render_template('addmailform.html',name = user, mail = mail, resultado = resultado) 
   else:
      return render_template('addmailform.html')      

if __name__ == '__main__':
   app.run(debug = True)