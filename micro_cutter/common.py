import os

from jinja2 import Template

INIT_FILE_NAME = '__init__'
RESOURCES = 'resources'
MODELS = 'models'
SCHEMAS = 'schemas'

def get_script_folder():
    return os.path.dirname(os.path.realpath(__file__))

def create_python_module_dir(path):
    if os.path.exists(path) is False:
        os.mkdir(path)
        create_init_file(path)


def create_service(path, name):
    create_python_module_dir(path)
    render_app(path, name)

def read_file(path):
    with open(os.path.join(path), 'r') as file:
        return file.read()

def create_file(path, content=''):
    with open(path + '.py', 'w+') as file:
        file.write(content)

def create_init_file(path):
    create_file(path=os.path.join(path, INIT_FILE_NAME), content='')

def render(template, path, module, name):
    create_python_module_dir(os.path.join(path, module))
    template = Template(read_file(os.path.join(get_script_folder(), template)))
    create_file(path=os.path.join(path, module, name),
                content=template.render(name=name))

def render_app(path, name):
    render(template='app.jinja2', path=path, module='', name='app')
    render(template='config.jinja2', path=path, module='', name='config')
    render(template='__init__.jinja2', path=path, module='', name='__init__')


def render_resource(path, name):
    render(template='resource.jinja2', path=path, module=RESOURCES, name=name)


def render_model(path, name):
    render(template='model.jinja2', path=path, module=MODELS, name=name)


def render_schema(path, name):
    render(template='schema.jinja2', path=path, module=SCHEMAS, name=name)

