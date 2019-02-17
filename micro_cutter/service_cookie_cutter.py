import os
from argparse import ArgumentParser, Action

from common import create_service
from common import render_resource, render_model, render_schema


class NameAction(Action):
    """ Creates model directory """

    def __call__(self, parser, args, values , option_string=None):
        setattr(args, self.dest, values)
        create_service(path=os.path.join(args.path, args.name), name=args.name)


class ResourceAction(Action):
    ''' Resource action renders resource template '''

    def __call__(self, parser, args, values, option_string=None):
        setattr(args, self.dest, values)
        if args.resource is not None:
            render_resource(path=os.path.join(args.path, args.name), name=args.resource)


class ModelAction(Action):
    ''' Model action renders model and schema template '''

    def __call__(self, parser, args, values, option_string=None):
        setattr(args, self.dest, values)
        if args.model is not None:
            render_model(path=os.path.join(args.path, args.name), name=args.model)
            render_schema(path=os.path.join(args.path, args.name), name=args.model)


def get_args():
    parser = ArgumentParser(prog='Micro Service Cookie Cutter', description='Creates a new service')
    parser.add_argument('name', action=NameAction, help='Name of the micro service')
    parser.add_argument('--resource', action=ResourceAction, help='Name of the resource',
                        required=False)
    parser.add_argument('--model', action=ModelAction, help='Name of the model', required=False)
    parser.add_argument('--path', default=os.getcwd(), help='Path of the project', required=False)
    return parser.parse_args()


args = get_args()
