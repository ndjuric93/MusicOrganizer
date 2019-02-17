import React from 'react';
import PropTypes from 'prop-types';

import Button from '@material-ui/core/Button';
import FormControl from '@material-ui/core/FormControl';
import Input from '@material-ui/core/Input';
import InputLabel from '@material-ui/core/InputLabel';
import withStyles from '@material-ui/core/styles/withStyles';
import { Link, withRouter } from 'react-router-dom';
import { loginRequest } from '../../services/UserProviders'
import { attachToken } from '../../services/DataProviders'
import UserForm, { UserContext } from './UserForm'

const styles = theme => ({
    form: {
        width: '100%',
        marginTop: theme.spacing.unit,
    },
    submit: {
        marginTop: theme.spacing.unit,
    },
});


class Login extends React.Component {

    constructor(props) {
        super(props)
    }

    log(credentials) {
        loginRequest(credentials)
            .then(response => {
                if (response.status == 200) {
                    localStorage.setItem('token', response.data['token'])
                    localStorage.setItem('authenticated', true)
                    attachToken()
                    this.props.history.push('/dashboard');
                } else {
                    localStorage.setItem('authenticated', false)
                }
            })
    }

    render() {
        const { classes } = this.props
        return (<UserForm
            header='Login'
        >
            <UserContext.Consumer>
                {({ state, handleChange }) => (
                    <React.Fragment>
                        <FormControl margin="normal" fullWidth>
                            <InputLabel htmlFor="username">Username</InputLabel>
                            <Input name="username" autoFocus onChange={handleChange} />
                        </FormControl>
                        <FormControl margin="normal" fullWidth>
                            <InputLabel htmlFor="password">Password</InputLabel>
                            <Input name="password" type="password" onChange={handleChange} />
                        </FormControl>
                        <Button
                            fullWidth
                            variant="contained"
                            color="primary"
                            className={classes.submit}
                            onClick={() => this.log(state)}
                        >
                            Sign in
                        </Button>
                        <Button component={Link} to='/register' fullWidth variant="contained" className={classes.submit} >
                            Register
                        </Button>
                    </React.Fragment>
                )}
            </UserContext.Consumer>
        </UserForm>)
    }
}

Login.propTypes = {
    classes: PropTypes.object.isRequired,
};

export default withRouter(withStyles(styles)(Login));
