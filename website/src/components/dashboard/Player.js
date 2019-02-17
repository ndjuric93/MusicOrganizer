import React from 'react'
import { withStyles } from '@material-ui/core/styles';
import AudioPlayer from "react-h5-audio-player";
import Footer from '../utility/Footer'
import { serverAddress } from '../../services/DataProviders'
import { fetchPlaylist, updatePlaylist, reportPlayed } from '../../services/PlayerProviders'
import { MainContext } from './Dashboard'

const styles = () => ({
    player: {
        height: '100%',
        display: 'flex',
        flexDirection: 'column',
        margin: '0px'
    }
})

class Player extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            song_id: 0,
            source: this.createSrcAddress(0)
        }
        props.playerState.updateSong = this.updateSong.bind(this)
    }

    createSrcAddress(id) {
        return serverAddress + '/player/' + id
    }

    updateSong() {
        fetchPlaylist().then(response => {
            if(response.status == 200) {
                this.setState({
                    song_id: response.data['index'],
                    source: this.createSrcAddress(response.data['index'])
                })
            }
        })
    }

    render() {
        const { classes } = this.props;
        console.log('player is refreshing')
        return (
            <Footer>
                <MainContext.Provider value={{updateSong: this.updateSong.bind(this)}}>
                    <AudioPlayer
                        className={classes.player}
                        src={this.state.source}
                        preload='none'
                        onPlay={e => {
                            this.updateSong()
                        }}
                        onEnded={() => {
                            reportPlayed(this.state.song_id).then(
                                () => updatePlaylist().then(() => this.updateSong())
                            )
                        }}
                    />
                </MainContext.Provider>
            </Footer>
        )
    }
}

export default withStyles(styles)(Player);
export const PlayerContext = React.createContext()
