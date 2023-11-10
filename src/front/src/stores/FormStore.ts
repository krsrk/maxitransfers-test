export const useFormStore = defineStore('FormStore', {
    state: () => {
        return {
            formTitle: 'Agregar Empleado',
            formButtonTitle: 'Agregar',
            editForm: false,
            form: {
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
        async setForm(data: Object) {
            // @ts-ignore
            this.$state.form = {
                employee_id: data.id,
                name: data.name,
                last_name: data.last_name,
                birth_date: data.birth_date,
                employee_number: data.employee_number,
                curp: data.curp,
                ssn: data.ssn,
                phone_number: data.phone_number,
                nationality: data.nationality
            }
        }
    }
})