import sqlalchemy
from flask import Flask, jsonify, request, abort
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from repositories.EmployeeRepository import EmployeeRepository
from repositories.BeneficiaryRepository import BeneficiaryRepository

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pymssql://sa:s8s!Np#m76LV#iN@db:1433/admin'
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Beneficiary(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(250), nullable=False)
    last_name = db.Column(db.String(550), nullable=False)
    birth_date = db.Column(db.Date, nullable=False)
    curp = db.Column(db.String, nullable=False)
    ssn = db.Column(db.String, nullable=False)
    phone_number = db.Column(db.String(10), nullable=False)
    nationality = db.Column(db.String)
    participation_percentage = db.Column(db.Integer)
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "last_name": self.last_name,
            "birth_date": self.birth_date,
            "curp": self.curp,
            "ssn": self.ssn,
            "phone_number": self.phone_number,
            "nationality": self.nationality,
            "participation_percentage": self.participation_percentage
        }


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
    beneficiaries = db.relationship(Beneficiary, backref='employee', lazy=True, cascade='all, delete-orphan')

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "last_name": self.last_name,
            "birth_date": self.birth_date,
            "curp": self.curp,
            "ssn": self.ssn,
            "phone_number": self.phone_number,
            "nationality": self.nationality,
            "beneficiaries": [{
                "id": beneficiary.id,
                "name": beneficiary.name,
                "last_name": beneficiary.last_name,
                "birth_date": beneficiary.birth_date,
                "curp": beneficiary.curp,
                "ssn": beneficiary.ssn,
                "phone_number": beneficiary.phone_number,
                "nationality": beneficiary.nationality,
                "participation_percentage": beneficiary.participation_percentage
            } for beneficiary in self.beneficiaries]
        }


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/api/employees')
def get_employees():
    result_set = EmployeeRepository(db, Employee).get_employees()
    return jsonify(result_set)


@app.route('/api/employee', methods=['POST'])
def create_employees():
    result_set = EmployeeRepository(db, Employee).create_employee(request.get_json())

    if result_set['on_error']:
        return jsonify({'message': result_set['error_message']}), 500

    return jsonify({'message': result_set['message']}), 201


@app.route('/api/employee', methods=['PUT'])
def update_employees():
    result_set = EmployeeRepository(db, Employee).update_employee(request.get_json())

    if result_set['on_error']:
        return jsonify({'message': result_set['error_message']}), 500

    return jsonify({'message': result_set['message']}), 201


@app.route('/api/employee', methods=['DELETE'])
def delete_employees():
    data = request.get_json()
    result_set = EmployeeRepository(db, Employee).delete_employee(data['employee_id'])

    if result_set['on_error']:
        return jsonify({'message': result_set['error_message']}), 500

    return jsonify({'message': result_set['message']}), 201


@app.route('/api/beneficiaries/employee/<int:employee_id>')
def get_beneficiaries(employee_id):
    result_set = BeneficiaryRepository(db, Beneficiary).get_beneficiaries(employee_id)
    return jsonify(result_set)


@app.route('/api/beneficiaries/employee/<int:employee_id>', methods=['POST'])
def create_employee_beneficiaries(employee_id):
    result_set = BeneficiaryRepository(db, Beneficiary).create_beneficiary(employee_id, request.get_json())

    if result_set['on_error']:
        return jsonify({'message': result_set['error_message']}), 500

    return jsonify({'message': result_set['message']}), 201


@app.route('/api/beneficiaries', methods=['PUT'])
def update_employee_beneficiaries():
    result_set = BeneficiaryRepository(db, Beneficiary).update_beneficiary(request.get_json())

    if result_set['on_error']:
        return jsonify({'message': result_set['error_message']}), 500

    return jsonify({'message': result_set['message']}), 201


@app.route('/api/beneficiaries', methods=['DELETE'])
def delete_employee_beneficiaries():
    data = request.get_json()
    result_set = BeneficiaryRepository(db, Beneficiary).delete_beneficiary(data['beneficiary_id'])

    if result_set['on_error']:
        return jsonify({'message': result_set['error_message']}), 500

    return jsonify({'message': result_set['message']}), 201


if __name__ == '__main__':
    app.run(debug=True)
