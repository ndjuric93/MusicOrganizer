import React from 'react';
import PropTypes from 'prop-types';
import { withStyles } from '@material-ui/core/styles';
import GridList from '@material-ui/core/GridList';
import GridListTile from '@material-ui/core/GridListTile';
import GridListTileBar from '@material-ui/core/GridListTileBar';
import { fetchArtists } from '../../services/RecordProviders'
import { MainContext } from './Dashboard'
import Album from './Album'
import { withRouter } from 'react-router-dom';


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


class Artists extends React.Component {

    constructor(props) {
        super(props);
        this.state = { artists: [] }
    }

    componentDidMount() {
        fetchArtists().then(response => {
            this.setState(response.data)
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
                            {this.state.artists.map(artist => (
                                <GridListTile key={artist.id} onClick={() => value.state.update(<Album id={artist.id} />)}>
                                    <img src={"data:image/png;base64," + artist.image} alt={artist.name} />
                                    <GridListTileBar title={artist.name} />
                                </GridListTile>
                            ))}
                        </GridList>
                    </div>
                )}
            </MainContext.Consumer>
        )

    }

}

Artists.propTypes = {
    classes: PropTypes.object.isRequired,
};

export default withRouter(withStyles(styles)(Artists));
