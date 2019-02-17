# Server

This part of the repo represent service with a set of microservices.

Here is a set of available services and main parts of the app

#### Service Registry

Service Registry is an element of the server that is used to keep track of all available services.
Apache Zookeeper will serve as a service registry

##### How it works

When service registry is deployed, it publishes it's name and address to the Apache Zookeeper.
Every microservice, has a location of zookeeper, and registers with a list of routes the service has, and it's location.

#### Gateway

Gateway is an element of the server that is exposed to the world.

##### How it works

The client sends requests to it, and it should respond with 
It is used to group routes.
Grouping routes is necessary so the client sends one requests and get all the expected resources.
For example, if someone requests the records, it will fetch the artists of the records as well so they can be shown in appropriate matter.
It will also be capable to do API joins from different tables.
It is configured from an .ini file.

#### Services

TO DO.
