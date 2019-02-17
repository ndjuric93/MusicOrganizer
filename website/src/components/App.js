import React, { Component } from 'react';
import { BrowserRouter as Router, Route, Switch, withRouter } from 'react-router-dom';
import Login from './users/Login'
import Register from './users/Register'
import Dashboard from './dashboard/Dashboard'
import PrivateRoute from '../services/AuthService'

function App(props) {
    return (
        <Router>
            <Switch>
                <Route path='/login' component={() => <Login />}  />
                <Route path='/register' component={Register} />
                <PrivateRoute path='/dashboard' component={Dashboard} />
            </Switch>
        </Router>
    );
}

export default App;
