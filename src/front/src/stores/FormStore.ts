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
            },
            beneficiaryForm: {
                name: '',
                last_name: '',
                birth_date: '',
                participation_percentage: '',
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
        },

        async setBeneficiaryForm(data: Object) {
            // @ts-ignore
            this.$state.form = {
                beneficiary_id: data.id,
                name: data.name,
                last_name: data.last_name,
                birth_date: data.birth_date,
                participation_percentage: data.participation_percentage,
                curp: data.curp,
                ssn: data.ssn,
                phone_number: data.phone_number,
                nationality: data.nationality
            }
        }
    }
})