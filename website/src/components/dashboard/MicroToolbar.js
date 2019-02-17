import React from 'react';
import AppBar from '@material-ui/core/AppBar'
import Toolbar from '@material-ui/core/Toolbar'
import Typography from '@material-ui/core/Typography'
import classNames from 'classnames';
import { withStyles } from "@material-ui/core";

const styles = theme => ({
  root: {
    display: 'flex',
  },
  appBar: {
      zIndex: theme.zIndex.drawer + 1
  },
  content: {
    flexGrow: 1,
    paddingTop: theme.spacing.unit * 9,
  },
  title: {
    paddingLeft: '10px'
  },
  toolbar: theme.mixins.toolbar,
});
  

function MicroToolbar(props) {
  const {classes} = props

  return (
    <AppBar
      position="absolute"
      className={classNames(classes.appBar)}
    >
    <Toolbar className={classes.toolbar}>
      <Typography
        component="h1"
        variant="h6"
        color="inherit"
        noWrap
        className={classes.title}
      >
        MicroMusic
      </Typography>
    </Toolbar>
  </AppBar>
)
}

export default withStyles(styles)(MicroToolbar)
