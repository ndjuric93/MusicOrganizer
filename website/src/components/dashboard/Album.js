import React from 'react';
import PropTypes from 'prop-types';
import { withStyles } from '@material-ui/core/styles';
import GridList from '@material-ui/core/GridList';
import GridListTile from '@material-ui/core/GridListTile';
import GridListTileBar from '@material-ui/core/GridListTileBar';
import { fetchAlbums } from '../../services/RecordProviders'
import { MainContext } from './Dashboard'
import Track from './Track'

const styles = theme => ({
    root: {
        flexWrap: 'wrap',
        overflow: 'hidden',
        backgroundColor: theme.palette.background.paper,
    },
    gridList: {
        width: '100%',
        height: '100%',
        paddingTop: '10px'
    },
});


class Album extends React.Component {

    constructor(props) {
        super(props);
        this.state = { albums: [] }
    }

    componentDidMount() {
        fetchAlbums(this.props.id).then(response => {
            if(response.status == 200) {
                this.setState(response.data)
            }
        }).catch(error => {
            localStorage.setItem('authenticated', false)
            this.props.history.push('/login')
        })
    }

    render() {
        const { classes } = this.props;
        return (
            <MainContext.Consumer>
                {value => (
                    <div className={classes.root}>
                        <GridList className={classes.gridList} cols={4}>
                            {this.state.albums.map(album => (
                                <GridListTile key={album.id} onClick={() => {value.state.update(<Track id={album.id} />)}}>
                                    <img src={"data:image/png;base64," + album.image} alt={album.name} />
                                    <GridListTileBar title={album.name} />
                                </GridListTile>
                            ))}
                        </GridList>
                    </div>
                )}
            </MainContext.Consumer>
        )

    }

}

Album.propTypes = {
    classes: PropTypes.object.isRequired,
};

export default withStyles(styles)(Album);
