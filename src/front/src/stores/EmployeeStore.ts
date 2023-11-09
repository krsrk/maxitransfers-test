import {EmployeesService} from "~/src/services/EmployeesService"

const employeesService = new EmployeesService()

export const useEmployeeStore = defineStore('EmployeeStore', {
    state: () => {
        return {
            employees: []
        }
    },
    actions: {
        async getEmployees() {
            this.$state.employees = await employeesService.getEmployees()
        },
        async createEmployee(data:Object) {

        },
        async updateEmployee(data:Object) {

        },
        async deleteEmployee(employeeId:any) {

        }
    },
    getters: {
        getEmployeesData: state => state.employees
    }
})