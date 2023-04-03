import os

from flask import Flask, render_template, request, session, redirect, url_for, flash
from flask_mysqldb import MySQL
import MySQLdb.cursors
from werkzeug.utils import secure_filename

app = Flask(__name__)

app.config['AADHAR_FOLDER'] = "static/register/"
app.config['UPLOAD_FOLDER'] = "static/upload/"
app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = ""
app.config['MYSQL_DB'] = "evote"
app.secret_key = 'the random string'
app.config['secret_key'] = "dhfebfhuiu34h3u7rh387fh8723h7hr83h27h8"

mysql = MySQL(app)


@app.route("/", methods=['post', 'get'])
def homepage():
    return render_template("homepage.html")


@app.route('/userlogin')
def log():
    return render_template('userlogin.html')


@app.route('/userlogin', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        aadharno = request.form['aadharno']
        pwd = request.form['pwd']
        # status = "APPROVED"
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * from register where aadharno= %s AND password = %s  ',
                       (aadharno, pwd))
        register = cursor.fetchone()
        if register is None:
            msg = 'INVALID LOGIN'
            return render_template('userlogin.html', msg=msg)
        elif register['status'] == "APPROVED":
            session['loggedin'] = True
            session['username'] = register['username']
            session['city'] = register['city']
            return redirect(url_for('welcome'))
        elif register['status'] == "APPLIED":
            msg = 'APPLICATION ON PROCESS'
            return render_template('userlogin.html', msg=msg)
        else:
            return redirect('alreadyvote')

        # return render_template('userlogin.html')


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        aadharno = request.form['aadharno']
        username = request.form['username']
        age = request.form['age']
        city = request.form['city']
        phoneno = request.form['phoneno']
        password = request.form['password']
        file = request.files['file']
        status = "APPLIED"
        file.save(os.path.join(app.config['AADHAR_FOLDER'], secure_filename(file.filename)))
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM register WHERE aadharno = % s AND password = % s', (aadharno, password))
        registers = cursor.fetchone()
        if registers:
            msg = 'Account already exists !'
            return render_template('useregister.html', msg=msg)
        elif allowed_file(file.filename):
            cur = mysql.connection.cursor()
            cur.execute(
                "INSERT INTO register(aadharno,username,age,city,phoneno,password,file,status) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",
                (aadharno, username, age, city, phoneno, password, file.filename, status))
            print(status)
            mysql.connection.commit()
            cur.close()
            return redirect('/registersuccess')
        else:
            return redirect('/register')
    elif request.method == 'POST':
        msg = 'Please fill out the form !'
    return render_template('useregister.html')


@app.route('/registersuccess', methods=['POST', 'GET'])
def thanks():
    return render_template('afteregister.html')


@app.route('/welcome', methods=['POST', 'GET'])
def welcome():
    return render_template('welcomepage.html', msg=session['username'], msg1=session['city'])


ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'png', 'mp3', 'doc'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/addcandidate', methods=['GET', 'POST'])
def addcandidate():
    if request.method == "POST" and session['username']:
        candidatename = request.form['candidatename']
        partyname = request.form['partyname']
        cityname = request.form['cityname']
        electiontype = request.form['electiontype']
        partylogo = request.files['partylogo']
        candidatephoto = request.files["candidatephoto"]
        aadharphoto = request.files["aadharphoto"]
        partylogo.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(partylogo.filename)))
        candidatephoto.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(candidatephoto.filename)))
        aadharphoto.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(aadharphoto.filename)))
        if partylogo and candidatephoto and aadharphoto and allowed_file(partylogo.filename):
            cur = mysql.connection.cursor()
            cur.execute(
                "INSERT INTO addcandidate (candidatename,partyname,cityname,electiontype,partylogo, candidatephoto, aadharphoto) VALUES (%s,%s,%s,%s,%s,%s,%s)",
                (candidatename, partyname, cityname, electiontype, partylogo.filename, candidatephoto.filename,
                 aadharphoto.filename))
            mysql.connection.commit()
            cur.close()
            return redirect('/addcandidate')
        else:
            msg = 'Invalid Uplaod only txt, pdf, png, jpg, jpeg, gif'
    return render_template("addcandidate.html")


@app.route('/viewpublic', methods=['POST', 'GET'])
def viewpublic():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("SELECT * from register WHERE status='APPLIED'")
    upload = cursor.fetchall()
    print(upload)
    return render_template("viewpublic.html", msg=upload)
    # return render_template("viewpublic.html")


@app.route('/approved/<idn>', methods=['POST', 'GET'])
def approved(idn):
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    print(idn)
    status = "APPROVED"
    cursor.execute("UPDATE register SET status=%s WHERE id=%s ", (status, idn))
    mysql.connection.commit()
    cursor.close()
    return redirect('/viewpublic')


@app.route('/rejected/<idn>', methods=['POST', 'GET'])
def rejected(idn):
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    print(idn)
    cursor.execute("DELETE FROM register WHERE id=%s ", idn)
    mysql.connection.commit()
    cursor.close()
    return redirect('/viewpublic')


@app.route('/canrejected/<idn>', methods=['POST', 'GET'])
def canrejected(idn):
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    print(idn)
    cursor.execute("DELETE FROM addcandidate WHERE id=%s ", idn)
    mysql.connection.commit()
    cursor.close()
    return redirect('/viewcandidate')


@app.route('/viewcandidate', methods=['post', 'get'])
def viewcandidate():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("SELECT * FROM addcandidate")
    upload = cursor.fetchall()
    print(upload)
    return render_template("viewcandidate.html", msg=upload)


# @app.route('/vote', methods=['post', 'get'])
# def vote():
#
#

@app.route("/display/<filename>")
def display_image(filename):
    h = 'upload/' + filename
    flash(h)
    return redirect(url_for('static', filename=h), code=301)


@app.route("/imgdisplay/<filename>")
def imgdisplay_image(filename):
    h = 'register/' + filename
    flash(h)
    return redirect(url_for('static', filename=h), code=301)


@app.route("/voting", methods=['post', 'get'])
def voting():
    electiontype = request.form.get('electiontype')
    cityname = request.form.get('cityname')
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("SELECT * FROM addcandidate WHERE cityname =%s AND  electiontype =%s ORDER BY vote DESC",
                   (cityname, electiontype))
    upload = cursor.fetchall()
    print(upload)
    return render_template("voting.html", msg=upload)


# @app.route("/voting/<idn>/<idn2>", methods=['post', 'get'])
# def votings(idn, idn2):
#     cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
#     cursor.execute("SELECT * FROM addcandidate WHERE cityname =%s AND  electiontype =%s", idn, idn2)
#     upload = cursor.fetchall()
#     print(upload)
#     return render_template("voting.html", msg=upload)


@app.route("/logreg", methods=['post', 'get'])
def logreg():
    return render_template("logreg.html")


@app.route("/adminlogin", methods=['post', 'get'])
def adminlogin():
    return render_template("adminlogin.html")


@app.route("/adminmodules", methods=['post', 'get'])
def adminmodules():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == "admin" and password == "admin":
            session['loggedin'] = True
            session['username'] = username
            return render_template("/adminmodules.html")
        else:
            msg = "Invalid Login"
            return render_template("adminlogin.html", msg=msg)


@app.route("/userlogin", methods=['post', 'get'])
def userlogin():
    return redirect("/")


@app.route("/useregister", methods=['post', 'get'])
def useregister():
    return render_template("useregister.html")


@app.route("/usermodules/<idn>", methods=['post', 'get'])
def usermodules(idn):
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("SELECT * FROM addcandidate WHERE cityname LIKE %s", [idn])
    upload = cursor.fetchall()
    print(upload)
    return render_template("usermodules.html", msg=upload, uname=session['username'])


@app.route("/usermodules/<idn>/<user>", methods=['post', 'get'])
def usermodule(idn, user):
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    print(idn)
    status = 'VOTED'
    cursor.execute("UPDATE addcandidate SET vote=vote+1 WHERE id=%s ", idn)
    cursor.execute("UPDATE register SET status=%s WHERE username=%s ", (status, user))
    mysql.connection.commit()
    cursor.close()
    return redirect('/thanksvote')


@app.route("/thanksvote", methods=['post', 'get'])
def thanksvote():
    session.pop('loggedin', None)
    session.pop('username', None)
    if request.method == "POST":
        return render_template("login.html")
    return render_template("thanks.html")


@app.route("/logout", methods=['post', 'get'])
def logout():
    session.pop('loggedin', None)
    session.pop('username', None)
    if request.method == "POST":
        return render_template("adminlogin.html")
    return redirect("/adminmodules")

@app.route("/alreadyvote", methods=['post', 'get'])
def alreadyvote():
    return render_template("alreadyvote.html")


if __name__ == '__main__':
    app.run(debug=True)
