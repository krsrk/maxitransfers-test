from sqlalchemy import create_engine, text


class EmployeeRepository:
    def __init__(self, db_engine, model) -> None:
        self.db = db_engine
        self.model = model
        self.db_engine = create_engine('mssql+pymssql://sa:s8s!Np#m76LV#iN@db:1433/admin')

    def get_employees(self):
        query = self.model.query.all()
        employees = [employee.to_dict() for employee in query]

        return employees

    def get_employee_by_id(self):
        pass

    def create_employee(self, data):
        conn = self.db_engine.raw_connection()
        cursor = conn.cursor()
        result = {
            "on_error": True,
            "message": "Something went wrong, try again later!",
            "error_message": "Something went wrong, try again later!"
        }

        try:
            sql = """
                EXEC sp_create_employee %s, %s, %s, %s, %s, %s, %s, %s
            """
            cursor.execute(sql, (
                data['name'],
                data['last_name'],
                data['birth_date'],
                data['employee_number'],
                data['curp'],
                data['ssn'],
                data['phone_number'],
                data['nationality']
            ))
            conn.commit()
            result['message'] = "Employee created successfully"
            result['on_error'] = False
        except Exception as err:
            result['on_error'] = True
            result['error_message'] = str(err)
        finally:
            cursor.close()
            conn.close()

        return result

    def update_employee(self, data):
        conn = self.db_engine.raw_connection()
        cursor = conn.cursor()
        result = {
            "on_error": True,
            "message": "Something went wrong, try again later!",
            "error_message": "Something went wrong, try again later!"
        }

        try:
            sql = """
                EXEC sp_update_employee %s, %s, %s, %s, %s, %s, %s, %s, %s
            """
            cursor.execute(sql, (
                data['employee_id'],
                data['name'],
                data['last_name'],
                data['birth_date'],
                data['employee_number'],
                data['curp'],
                data['ssn'],
                data['phone_number'],
                data['nationality']
            ))
            conn.commit()
            result['message'] = "Employee updated successfully"
            result['on_error'] = False
        except Exception as err:
            result['on_error'] = True
            result['error_message'] = str(err)
        finally:
            cursor.close()
            conn.close()

        return result

    def delete_employee(self, employee_id):
        conn = self.db_engine.raw_connection()
        cursor = conn.cursor()
        result = {
            "on_error": True,
            "message": "Something went wrong, try again later!",
            "error_message": "Something went wrong, try again later!"
        }

        try:
            sql = """
                EXEC sp_delete_employee %s
            """
            cursor.execute(sql, (employee_id))
            conn.commit()
            result['message'] = "Employee deleted successfully"
            result['on_error'] = False
        except Exception as err:
            result['on_error'] = True
            result['error_message'] = str(err)
        finally:
            cursor.close()
            conn.close()

        return result
