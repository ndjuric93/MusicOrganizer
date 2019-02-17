import React from 'react';
import PropTypes from 'prop-types';
import Button from '@material-ui/core/Button';
import FormControl from '@material-ui/core/FormControl';
import Input from '@material-ui/core/Input';
import InputLabel from '@material-ui/core/InputLabel';
import { Link } from 'react-router-dom';
import withStyles from '@material-ui/core/styles/withStyles';
import { withRouter } from 'react-router-dom'
import { registerRequest } from '../../services/UserProviders'

import UserForm, { UserContext } from './UserForm'


const styles = theme => ({
    layout: {
        width: 'auto',
        display: 'block', // Fix IE 11 issue.
        marginLeft: theme.spacing.unit * 3,
        marginRight: theme.spacing.unit * 3,
        [theme.breakpoints.up(400 + theme.spacing.unit * 3 * 2)]: {
            width: 400,
            marginLeft: 'auto',
            marginRight: 'auto',
        },
    },
    paper: {
        marginTop: theme.spacing.unit * 8,
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        padding: `${theme.spacing.unit * 2}px ${theme.spacing.unit * 3}px ${theme.spacing.unit * 3}px`,
    },
    avatar: {
        margin: theme.spacing.unit,
        backgroundColor: theme.palette.secondary.main,
    },
    form: {
        width: '100%', // Fix IE 11 issue.
        marginTop: theme.spacing.unit,
    },
    submit: {
        marginTop: theme.spacing.unit,
    },
});


class Register extends React.Component {

    constructor(props) {
        super(props)
    }

    register(credentials) {
        registerRequest(credentials).then(response => {
            if (response.status == 200) {
                this.props.history.push('/login')
            }
        })
    }

    render() {
        const { classes } = this.props

        return (
            <UserForm
                header='Register'
            >
                <UserContext.Consumer>
                    {({ state, handleChange }) => (
                        <React.Fragment>
                            <FormControl margin="normal" fullWidth>
                                <InputLabel htmlFor="username">Username</InputLabel>
                                <Input name="username" onChange={handleChange} />
                            </FormControl>
                            <FormControl margin="normal" fullWidth>
                                <InputLabel htmlFor="email">Email Address</InputLabel>
                                <Input name="email" onChange={handleChange} />
                            </FormControl>
                            <FormControl margin="normal" fullWidth>
                                <InputLabel htmlFor="password">Password</InputLabel>
                                <Input name="password" type="password" onChange={handleChange} />
                            </FormControl>
                            <Button
                                component={Link} to='/'
                                fullWidth
                                onClick={() => this.register(state)}
                                variant="contained"
                                color="primary"
                                className={classes.submit}
                            >
                                Register
                            </Button>
                            <Button
                                component={Link}
                                to='/login'
                                fullWidth
                                variant="contained"
                                className={classes.submit}
                            >
                                    Go back to Login
                            </Button>
                        </React.Fragment>
                    )}
                </UserContext.Consumer>
            </UserForm>)
    }
}

Register.propTypes = {
    classes: PropTypes.object.isRequired,
};

export default withRouter(withStyles(styles)(Register))
