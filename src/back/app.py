from flask import Flask, jsonify
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pymssql://sa:s8s!Np#m76LV#iN@db:1433/admin'
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Beneficiary(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(250), nullable=False)
    last_name = db.Column(db.String(550), nullable=False)
    birth_date = db.Column(db.Date, nullable=False)
    employee_number = db.Column(db.String, nullable=False)
    curp = db.Column(db.String, nullable=False)
    ssn = db.Column(db.String, nullable=False)
    phone_number = db.Column(db.String(10), nullable=False)
    nationality = db.Column(db.String)
    participation_percentage = db.Column(db.Integer)
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'), nullable=False)


class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(250), nullable=False)
    last_name = db.Column(db.String(550), nullable=False)
    birth_date = db.Column(db.Date, nullable=False)
    employee_number = db.Column(db.String, nullable=False)
    curp = db.Column(db.String, nullable=False)
    ssn = db.Column(db.String, nullable=False)
    phone_number = db.Column(db.String(10), nullable=False)
    nationality = db.Column(db.String)
    beneficiaries = db.relationship(Beneficiary, backref='employee', lazy=True)





@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
