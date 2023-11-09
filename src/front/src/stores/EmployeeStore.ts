export const useEmployeeStore = defineStore('EmployeeStore', {
    state: () => {
        return {
            employees: []
        }
    },
    actions: {
        async getEmployees() {

        },
        async createEmployee(data:Object) {

        },
        async updateEmployee(data:Object) {

        },
        async deleteEmployee(employeeId:any) {

        }
    }
})