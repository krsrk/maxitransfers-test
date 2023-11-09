import { useAxiosRequest } from "#build/composables/useAxios"


export class EmployeesService {
    private baseUrl: string = 'htpp://localhost:8089/api'
    private request: any

    constructor() {
        this.request = useAxiosRequest()
    }
}