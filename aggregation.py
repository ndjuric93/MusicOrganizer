from itertools import chain

first = [
    {
        'id': 1,
        'count': 2
    },
    {
        'id': 2,
        'count': 8
    }
]

second = [
    {
        'id': 1,
        'track': 'tracko'
    },
    {
        'id': 2,
        'track': 'macko'
    }
]

def aggregate(resp, aggregate_by):
    # Split by tuples with same id
    # Combine tuples
    # Return list
    response_list = list(chain.from_iterable(resp.values()))
    val = split_by_id(response_list, aggregate_by)
    return val

def split_by_id(data, id):
    temp = {}
    for d in data:
        temp[d[id]] = list(chain(d))
    return temp

resp = {
    'first': first,
    'second': second
}

print(aggregate(resp, 'id'))
