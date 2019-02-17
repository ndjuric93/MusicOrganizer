import React from 'react'
import { withStyles } from '@material-ui/core';
import Drawer from '@material-ui/core/Drawer';
import classNames from 'classnames';
import Divider from '@material-ui/core/Divider';
import ListItem from '@material-ui/core/ListItem';
import ListItemText from '@material-ui/core/ListItemText';
import Artist from './Artist'
import Playlist from './Playlist'
import Statistics from './Statistics'
import { MainContext } from './Dashboard'
import logout from '../users/Logout'
import { withRouter } from 'react-router-dom'

const drawerWidth = 240;

const styles = theme => ({
    drawer: {
        width: drawerWidth,
        flexShrink: 0,
    },
    drawerPaper: {
      width: drawerWidth,
    },
    toolbar: theme.mixins.toolbar,
  });



function Navigation(props) {

    const {classes} = props

    return (
        <MainContext.Consumer>
            {value => (
                <Drawer
                    variant="permanent"
                    className={classes.drawer}
                    classes={{
                        paper: classNames(classes.drawerPaper),
                    }}
                >
                <div className={classes.toolbar} />
                <ListItem button onClick={() => value.state.update(<Artist />)} >
                    <ListItemText primary="Music"/>
                </ListItem>
                <ListItem button onClick={() => value.state.update(<Playlist />)} >
                    <ListItemText primary="Playlist" />
                </ListItem>
                <ListItem button onClick={() => value.state.update(<Statistics />)}>
                    <ListItemText primary="Statistics" />
                </ListItem>
                <Divider />
                <ListItem button onClick={() => logout(props)}>
                    <ListItemText primary="Logout" />
                </ListItem>
                </Drawer>
            )}
        </MainContext.Consumer>
    )
}

export default withRouter(withStyles(styles)(Navigation))
