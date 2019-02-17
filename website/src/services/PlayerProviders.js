import axios from 'axios'

import { serverAddress } from './DataProviders'

export function postToPlaylist(id) {
    return axios.post(serverAddress + '/album/' + id)
}

export function setSongToPlay(id) {
    return axios.post(serverAddress + '/playlist/' + id)
}

export function reportPlayed(id) {
    return axios.post(serverAddress + '/player/' + id)
}

export function updatePlaylist() {
    return axios.post(serverAddress + '/playlist')
}

export function fetchPlaylist() {
    return axios.get(serverAddress + '/playlist')
}

export function deleteFromPlaylist(id) {
    return axios.delete(serverAddress + '/playlist/' + id)
}
