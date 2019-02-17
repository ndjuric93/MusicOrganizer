import React from 'react';
import PropTypes from 'prop-types';
import { withStyles } from '@material-ui/core/styles';
import CssBaseline from '@material-ui/core/CssBaseline';
import Navigation from './Navigation';
import MicroToolbar from './MicroToolbar';
import Artists from './Artist'
import Player from './Player'


const styles = theme => ({
    root: {
        display: 'flex',
    },
    content: {
        flexGrow: 1,
        paddingTop: theme.spacing.unit * 9,
    },

});


class Dashboard extends React.Component {

    constructor(props) {
        super(props)
        this.state = {
            current: <Artists />,
            update: component => { this.setState({ current: component }) }
        }
        this.playerState = {
            test: 'test'
        }
    }

    render() {
        const { classes } = this.props;
        return (
            <MainContext.Provider value={{
                state: this.state,
                playerState: this.playerState
            }}>
                <React.Fragment>
                    <CssBaseline />
                    <div className={classes.root}>
                        <MicroToolbar />
                        <Navigation />
                        <main className={classes.content}>
                            {this.state.current}
                        </main>
                        <Player playerState={this.playerState}/>
                    </div>
                </React.Fragment>
            </MainContext.Provider>
        );
    }
}

Dashboard.propTypes = {
    classes: PropTypes.object.isRequired,
};

export const MainContext = React.createContext()
export default withStyles(styles)(Dashboard);
