import axios from 'axios'

export const serverAddress = 'http://0.0.0.0:5000'

export function attachToken() {
    const token = localStorage.getItem('token')
    if (token) {
        axios.defaults.headers.common['Authorization'] = 'Bearer ' + token
    } else {
        axios.defaults.headers.common['Authorization'] = null;
    }
};

attachToken()
