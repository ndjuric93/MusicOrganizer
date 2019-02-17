import React from 'react';
import PropTypes from 'prop-types';
import Divider from '@material-ui/core/Divider';
import List from '@material-ui/core/List';
import ListItem from '@material-ui/core/ListItem';
import ListItemText from '@material-ui/core/ListItemText';
import IconButton from '@material-ui/core/IconButton'
import PlaylistAdd from '@material-ui/icons/PlaylistAdd'
import { withStyles } from '@material-ui/core/styles';
import { fetchTracks } from '../../services/RecordProviders'
import { postToPlaylist } from '../../services/PlayerProviders'
import { MainContext } from './Dashboard';

const styles = theme => ({
    root: {
        width: '100%',
        backgroundColor: theme.palette.background.paper,
    },
});

class Tracks extends React.Component {

    constructor(props) {
        super(props);
        this.state = { tracks: [] }
    }

    componentDidMount() {
        fetchTracks(this.props.id)
            .then(response => {
                console.log(response.data)
                this.setState(response.data)
            })
    }

    render() {
        const { classes } = this.props;
        return (
            <MainContext.Consumer>
                {
                    value => (
                        <List className={classes.root}>
                            {this.state.tracks.map(track => (
                                <div key={track.id}>
                                    <ListItem>
                                        <ListItemText primary={track.track_number + '. ' + track.name + ' (selected ' + track.count + ' times)'}/>
                                        <IconButton>
                                            <PlaylistAdd onClick={() =>
                                                {
                                                    postToPlaylist(track.id).then(response => {
                                                        if(response == 200) {
                                                            value.playerState.updateSong()
                                                        }
                                                    })
                                                }
                                            } />
                                        </IconButton>
                                    </ListItem>
                                    <Divider />
                                </div>
                            ))}
                        </List>
                    )
                }
            </MainContext.Consumer>
        );
    }

}

Tracks.propTypes = {
    classes: PropTypes.object.isRequired,
};

export default withStyles(styles)(Tracks);
