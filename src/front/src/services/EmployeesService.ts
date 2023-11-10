import axios from './axios'
import {integer} from "vscode-languageserver-types";

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

    async createEmployee(formData:any) {
        try {
            const urlService = this.baseUrl + `/employee`
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

    async updateEmployee(formData:any) {
        try {
            const urlService = this.baseUrl + `/employee`
            const { data } = await this.request.put(urlService, formData)
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

    async deleteEmployee(employeeId:integer) {
        try {
            const urlService = this.baseUrl + `/employee`
            const { data } = await this.request.delete(urlService, {
                data: {
                    employee_id: employeeId
                }
            })
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