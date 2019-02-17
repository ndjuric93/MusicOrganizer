
export default function logout(props) {
    localStorage.removeItem('authenticated')
    localStorage.removeItem('id_token')
    props.history.push('/login')
}
