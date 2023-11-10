import {BeneficiariesService} from "~/src/services/BeneficiariesService"

const beneficiaryService = new BeneficiariesService()

export const useBeneficiaryStore = defineStore('BeneficiaryStore', {
    state: () => {
        return {
            employeeId: '',
            beneficiaries: []
        }
    },
    actions: {
        async getBeneficiaries(employeeId:any) {
            this.$state.beneficiaries = await beneficiaryService.getBeneficiaries(employeeId)
        },
        async createBeneficiary(employeeId:any, data:Object) {
            await beneficiaryService.createBeneficiary(employeeId, data)
            await this.getBeneficiaries(employeeId)
        },
        async updateBeneficiary(employeeId:any, data:Object) {
            await beneficiaryService.updateBeneficiary(data)
            await this.getBeneficiaries(employeeId)
        },
        async deleteBeneficiary(beneficiaryId:any) {

        }
    },
    getters: {
        getBeneficiariesData: state => state.beneficiaries,
    }
})