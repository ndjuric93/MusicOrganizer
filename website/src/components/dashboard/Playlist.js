import React from 'react';
import PropTypes from 'prop-types';
import Divider from '@material-ui/core/Divider';
import List from '@material-ui/core/List';
import ListItem from '@material-ui/core/ListItem';
import ListItemText from '@material-ui/core/ListItemText';
import { withStyles } from '@material-ui/core/styles';
import { deleteFromPlaylist, fetchPlaylist, setSongToPlay } from '../../services/PlayerProviders'
import IconButton from '@material-ui/core/IconButton'
import Clear from '@material-ui/icons/Clear'
import PlayArrow from '@material-ui/icons/PlayArrow'
import { MainContext } from './Dashboard';


const styles = theme => ({
    root: {
        width: '100%',
        backgroundColor: theme.palette.background.paper,
    },
});

class Playlist extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            index: 0,
            tracks: []
        }
    }

    getPlaylist() {
        fetchPlaylist(this.props.id)
            .then(response => {
                this.setState({
                    tracks: response.data['playlist'],
                    index: response.data['index']
            })
        })
    }

    componentDidMount() {
        this.getPlaylist()
    }

    render() {
        const { classes } = this.props;
        return (
            <List className={classes.root}>
                {this.state.tracks.map((track, index )=> (
                    <div key={index}>
                        <ListItem>
                            <ListItemText primary={index + '. ' + track}/>
                            <MainContext.Consumer>
                                {
                                    value => (
                                        <IconButton>
                                            <PlayArrow onClick={() => {
                                                setSongToPlay(index).then(() => {
                                                    value.playerState.updateSong()    
                                                })
                                            }} />
                                        </IconButton>   
                                    )
                                }
                            </MainContext.Consumer>
                            <IconButton>
                                <Clear onClick={() =>
                                    deleteFromPlaylist(index).then(this.getPlaylist())
                                } />
                            </IconButton>
                        </ListItem>
                        <Divider />
                    </div>
                ))}
            </List>
        );
    }
}

Playlist.propTypes = {
    classes: PropTypes.object.isRequired,
};

export default withStyles(styles)(Playlist);
