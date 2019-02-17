import requests


def fetch_services(location):
    services = requests.get(
        'http://' + location.address + ':' + location.port + '/registry'
    ).json()
    print(services)
    return services
