import React from 'react';
import { Route, Redirect, withRouter } from 'react-router-dom';


class PrivateRoute extends React.Component {

    constructor(props) {
        super(props)
    }

    render() {
        const { auth, component: Component, ...rest } = this.props
        return (
            <Route
                {...rest}
                render={props => {
                    if (localStorage.getItem('authenticated')) {
                        return <Component {...props} />
                    }
                    return <Redirect to={"/login"}/>
                }}
            />
        )
    }

}

export default withRouter(PrivateRoute)
