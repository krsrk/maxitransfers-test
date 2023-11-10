import {EmployeesService} from "~/src/services/EmployeesService"

const employeesService = new EmployeesService()

export const useEmployeeStore = defineStore('EmployeeStore', {
    state: () => {
        return {
            employees: [],
            employeeForm: {
                name: '',
                last_name: '',
                birth_date: '',
                employee_number: '',
                curp: '',
                ssn: '',
                phone_number: '',
                nationality: ''
            }
        }
    },
    actions: {
        async getEmployees() {
            this.$state.employees = await employeesService.getEmployees()
        },
        async createEmployee(data:Object) {
            await employeesService.createEmployee(data)
            await this.getEmployees()
        },
        async updateEmployee(data:Object) {
            await employeesService.updateEmployee(data)
            await this.getEmployees()
        },
        async deleteEmployee(employeeId:any) {
            await employeesService.deleteEmployee(employeeId)
            await this.getEmployees()
        }
    },
    getters: {
        getEmployeesData: state => state.employees,
        getEmployeesFormData: state => state.employeeForm
    }
})