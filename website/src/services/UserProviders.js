import axios from 'axios'

import { serverAddress } from './DataProviders'

export function loginRequest(credentials) {
    return axios.post(serverAddress + '/login', credentials)
}

export function registerRequest(credentials) {
    return axios.post(serverAddress + '/register', credentials)
}
