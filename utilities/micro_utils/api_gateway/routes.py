from collections import defaultdict


def list_routes(app):
    return {str(rule)[1:]: list(rule.methods) for rule in
            filter(lambda r: r.endpoint[0] == '_', app.url_map.iter_rules())}


def service_to_routes(services):
    options = defaultdict(dict)
    for address, routes in services.items():
        for resource, methods in routes.items():
            if 'GET' in methods:
                options['GET'][resource] = address
            if 'POST' in methods:
                options['POST'][resource] = address
            if 'PUT' in methods:
                options['PUT'][resource] = address
            if 'DELETE' in methods:
                options['DELETE'][resource] = address
    return options
