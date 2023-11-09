import axios from './axios'

export class EmployeesService {
    private baseUrl: string = 'http://localhost:8089/api'
    private request: any

    constructor() {
        this.request = axios
    }

    async getEmployees() {
        try {
            const urlService = this.baseUrl + `/employees`
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
}