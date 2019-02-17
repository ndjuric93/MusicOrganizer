import axios from 'axios'

import { serverAddress } from './DataProviders'

export function fetchCountStatistics() {
    return axios.get(serverAddress + '/statistics/count')
}