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
        async deleteBeneficiary(employeeId:any, beneficiaryId:any) {
            await beneficiaryService.deleteBeneficiary(beneficiaryId)
            await this.getBeneficiaries(employeeId)
        },
        isParticipationPercentageOutOfLimit(editForm: any, itFrm: any) {
            let countParticipation = 0

            this.$state.beneficiaries.map((it: any) => {
                if (editForm && itFrm.beneficiary_id == it.id) {
                    it.participation_percentage = itFrm.participation_percentage
                }

                countParticipation += parseInt(it.participation_percentage)
            })

            if (!editForm) {
                countParticipation += parseInt(itFrm.participation_percentage)
            }

            return (countParticipation > 100)
        },
    },
    getters: {
        getBeneficiariesData: state => state.beneficiaries,
    }
})