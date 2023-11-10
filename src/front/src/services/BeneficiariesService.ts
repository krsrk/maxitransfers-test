import axios from './axios'


export class BeneficiariesService {
    private baseUrl: string = 'http://localhost:8089/api'
    private request: any

    constructor() {
        this.request = axios
    }

    async getBeneficiaries(employeeId:any) {
        try {
            const urlService = this.baseUrl + `/beneficiaries/employee/${employeeId}`
            const { data } = await this.request.get(urlService)
            data.status = 'OK'

            return data
        } catch (e) {
            console.log(e)
            return {
                status: 'ERR',
                message: 'Something wrong happer, try again later!'
            }
        }
    }

    async createBeneficiary(employeeId:any, formData:any) {
        try {
            const urlService = this.baseUrl + `/beneficiaries/employee/${employeeId}`
            const { data } = await this.request.post(urlService, formData)
            data.status = 'OK'

            return data
        } catch (e) {
            console.log(e)
            return {
                status: 'ERR',
                message: 'Something wrong happer, try again later!'
            }
        }
    }
}