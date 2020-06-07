####This repository is the template for anyone who want to use FLASK as an api server

To start using, just run command
```
docker-compose -f docker-compose.yml up -d
```
(Your computer need to have docker and docker-compose installed first)

This command will build docker image from command in Dockerfile. 
If you want other packages to install in this docker image, just edit Dockerfile or requirements for PIP packages.

To enable authentication for API, you have to config constant.py first.
Change REQUIRED_AUTH to True and then specify your SECRET key and AUTH_BODY.
We use JWT standard as an encoder.

All starting flask command is written in server.py. Enjoy your coding!