import React from 'react';
import PropTypes from 'prop-types';
import List from '@material-ui/core/List';
import Typography from '@material-ui/core/Typography';
import { withStyles } from '@material-ui/core/styles';
import { fetchCountStatistics } from '../../services/StatisticProviders'
import CanvasJSReact from '../../lib/canvasjs.react'

var CanvasJSChart = CanvasJSReact.CanvasJSChart;

const styles = theme => ({
    container: {
      display: 'flex',
      flexWrap: 'wrap',
    },
    textField: {
      marginLeft: theme.spacing.unit,
      marginRight: theme.spacing.unit,
      width: 200,
    },
    dense: {
      marginTop: 19,
    },
    menu: {
      width: 200,
    },
  });


class Statistics extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            'mostPlayedSong': ''
        }
    }

    getStatistics() {
        fetchCountStatistics().then(response => {
            console.log(response)
            this.setState({
                'mostPlayedSong': response.data['most_played']
            });
        })
    }

    componentWillMount() {
        this.getStatistics()
    }

    render() {
        console.log(this.state['mostPlayedSong'])
        const { classes } = this.props;
        const { name, author, count } = this.state['mostPlayedSong']
        const options = {
            title: {
              text: "Basic Column Chart in React"
            },
            data: [{
                      type: "column",
                      dataPoints: [
                          { label: "Apple",  y: 10  },
                          { label: "Orange", y: 15  },
                          { label: "Banana", y: 25  },
                          { label: "Mango",  y: 30  },
                          { label: "Grape",  y: 28  }
                      ]
             }]
         }


        return (
            <div>
                <CanvasJSChart options={options} />
                <CanvasJSChart options={options} />
            </div>
        );
    }
}

Statistics.propTypes = {
    classes: PropTypes.object.isRequired,
};

export default withStyles(styles)(Statistics);
