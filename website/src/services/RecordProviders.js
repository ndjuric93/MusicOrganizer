import axios from 'axios'

import { serverAddress } from './DataProviders'

export function fetchTracks(id) {
    return axios.get(serverAddress + '/track/statistics/' + id).then(
        response => {
            console.log(response)
            if(response.status == 200) {
                return response
            } else {
                return axios.get(serverAddress + '/album/' + id)
            }
        })
}

export function fetchAlbums(id) {
    return axios.get(serverAddress + '/artist/' + id)
}

export function fetchArtists() {
    return axios.get(serverAddress + '/artist')
}
