import setuptools

dependencies = [
    'alembic',
    'confluent_kafka',
    'flask',
    'flask-restplus',
    'flask-jwt-simple',
    'flask-marshmallow',
    'flask-sqlalchemy',
    'protobuf',
    'sqlalchemy',
    'requests',
    'marshmallow-sqlalchemy'
]

setuptools.setup(
    name="MicroPlayer",
    version="0.0.1",
    author="Nemanja Djuric",
    description="Player Module",
    author_email="nemanja.djuric@outlook.com",
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=dependencies,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
