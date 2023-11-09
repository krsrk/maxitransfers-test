from sqlalchemy import create_engine, text


class BeneficiaryRepository:
    def __init__(self, db_engine, model) -> None:
        self.db = db_engine
        self.model = model
        self.db_engine = create_engine('mssql+pymssql://sa:s8s!Np#m76LV#iN@db:1433/admin')

    def get_beneficiaries(self, employee_id):
        query = self.model.query.filter_by(employee_id=employee_id).all()
        beneficiaries = [beneficiary.to_dict() for beneficiary in query]

        return beneficiaries

    def get_beneficiary_by_id(self):
        pass

    def create_beneficiary(self, employee_id, data):
        conn = self.db_engine.raw_connection()
        cursor = conn.cursor()
        result = {
            "on_error": True,
            "message": "Something went wrong, try again later!",
            "error_message": "Something went wrong, try again later!"
        }

        try:
            sql = """
                EXEC sp_create_beneficiary %s, %s, %s, %s, %s, %s, %s, %s, %s
            """
            cursor.execute(sql, (
                data['name'],
                data['last_name'],
                data['birth_date'],
                data['curp'],
                data['ssn'],
                data['phone_number'],
                data['nationality'],
                data['participation_percentage'],
                employee_id,
            ))
            conn.commit()
            result['message'] = "Beneficiary created successfully"
            result['on_error'] = False
        except Exception as err:
            result['on_error'] = True
            result['error_message'] = str(err)
        finally:
            cursor.close()
            conn.close()

        return result

    def update_beneficiary(self, data):
        conn = self.db_engine.raw_connection()
        cursor = conn.cursor()
        result = {
            "on_error": True,
            "message": "Something went wrong, try again later!",
            "error_message": "Something went wrong, try again later!"
        }

        try:
            sql = """
                EXEC sp_update_beneficiary %s, %s, %s, %s, %s, %s, %s, %s, %s
            """
            cursor.execute(sql, (
                data['beneficiary_id'],
                data['name'],
                data['last_name'],
                data['birth_date'],
                data['curp'],
                data['ssn'],
                data['phone_number'],
                data['nationality'],
                data['participation_percentage'],
            ))
            conn.commit()
            result['message'] = "Beneficiary updated successfully"
            result['on_error'] = False
        except Exception as err:
            result['on_error'] = True
            result['error_message'] = str(err)
        finally:
            cursor.close()
            conn.close()

        return result

    def delete_beneficiary(self, beneficary_id):
        conn = self.db_engine.raw_connection()
        cursor = conn.cursor()
        result = {
            "on_error": True,
            "message": "Something went wrong, try again later!",
            "error_message": "Something went wrong, try again later!"
        }

        try:
            sql = """
                EXEC sp_delete_beneficiary %s
            """
            cursor.execute(sql, (beneficary_id))
            conn.commit()
            result['message'] = "Beneficiary deleted successfully"
            result['on_error'] = False
        except Exception as err:
            result['on_error'] = True
            result['error_message'] = str(err)
        finally:
            cursor.close()
            conn.close()

        return result
