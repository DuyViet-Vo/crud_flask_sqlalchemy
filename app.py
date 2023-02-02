from flask import Flask, render_template, request,redirect,url_for
from model import db, students
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///student.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.before_first_request
def create_student():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.form:
        name = request.form.get('name1')
        date_birth = datetime.strptime(request.form.get('date_birth1'), '%Y-%m-%d')
        address = request.form.get('address1')
        phone = request.form.get('phone_1')
        Student = students(name = name,date_birth= date_birth ,address = address, phone = phone)
        db.session.add(Student)
        db.session.commit()
    data= students.query.all()
    
    
    return render_template('home.html',data= data)

@app.route('/update',methods=['POST','GET'])
def update():
    if request.method == 'POST':
        my_data = students.query.get(request.form.get('id'))
        my_data.name = request.form['name']
        my_data.date_birth =datetime.strptime( request.form['date_birth'], '%Y-%m-%d')
        my_data.address = request.form['address']
        my_data.phone = request.form['phone']
        
        db.session.commit()
        
        return redirect(url_for('home'))

@app.route('/delete/<id>/', methods= ['GET','POST'])
def delete(id):
    my_student= students.query.get(id)
    db.session.delete(my_student)
    db.session.commit()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)