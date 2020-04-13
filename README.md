# URL Scanning Service

For this exercise, we would like to see how you go about solving a rather straightforward coding challenge and architecting for the future. One of our key values in how we develop new systems is to start with very simple implementations and progressively make them more capable, scalable and reliable. And releasing them each step of the way. As you work through this exercise it would be good to "release" frequent updates by pushing updates to a shared git repo (we like to use Bitbucket's free private repos for this, but gitlab or github also work). It's up to you how frequently you do this and what you decide to include in each push. Don't forget some unit tests (at least something representative).
Here's what we would like you to build.
# URL lookup service
We have an HTTP proxy that is scanning traffic looking for malware URLs. Before allowing HTTP connections to be made, this proxy asks a service that maintains several databases of malware URLs if the resource being requested is known to contain malware.
Write a small web service, in the language/framework your choice, that responds to GET requests where the caller passes in a URL and the service responds with some information about that URL. The GET requests look like this:
       GET /urlinfo/1/{hostname_and_port}/{original_path_and_query_string}
The caller wants to know if it is safe to access that URL or not. As the implementer, you get to choose the response format and structure. These lookups are blocking users from accessing the URL until the caller receives a response from your service.
Give some thought to the following:

1. The size of the URL list could grow infinitely, how might you scale this beyond the memory capacity of this VM? Bonus if you implement this.
2. The number of requests may exceed the capacity of this VM, how might you solve that? Bonus if you implement this.
3. What are some strategies you might use to update the service with new URLs? Updates may be as much as 5 thousand URLs a day with updates arriving every 10 minutes.
4. Bonus points if you containerize the app. Email us your ideas.
 

## 1. Pulling and building image
git clone https://github.com/shiningram/url_scanning_service.git
cd url_scanning_service
docker-compose build

## 2. Cleaning up
This command cleans up every docker image and networks. If you are not sure then dont run it.
docker system prune -a

## 3. Init docker swarm

docker swarm init
## 4. Deployment
docker stack deploy --compose-file docker-compose.yml url_scanning_service

Output of above CLI looks like this.

Ram-Mac:url_scanning_service rregar$ docker stack deploy --compose-file docker-compose.yml url_scanning_service
Ignoring unsupported options: build

Creating network url_scanning_service_redis
Creating network url_scanning_service_lb
Creating network url_scanning_service_app
Creating service url_scanning_service_urldb
Creating service url_scanning_service_proxy

Creating service url_scanning_service_app
Ram-Mac:url_scanning_service rregar$ 

## 5. Check the services in stack
Ram-Mac:url_scanning_service rregar$ docker stack ls
NAME                   SERVICES            ORCHESTRATOR
url_scanning_service   3                   Swarm
Ram-Mac:url_scanning_service rregar$ 

## 6. List the containers
Ram-Mac:url_scanning_service rregar$ docker stack ps url_scanning_service
ID                  NAME                           IMAGE               NODE                DESIRED STATE       CURRENT STATE           ERROR               PORTS
hysrwwl4tm11        url_scanning_service_app.1     webapp:latest       docker-desktop      Running             Running 2 minutes ago                       
hjyyf2n65iaj        url_scanning_service_proxy.1   nginx:alpine        docker-desktop      Running             Running 2 minutes ago                       
jncq6ag1l7ui        url_scanning_service_urldb.1   redis:latest        docker-desktop      Running             Running 2 minutes ago                       
uqu413jpqmr6        url_scanning_service_app.2     webapp:latest       docker-desktop      Running             Running 2 minutes ago                       
Ram-Mac:url_scanning_service rregar$ 

## 7. Logs from each container
Ram-Mac:url_scanning_service rregar$ docker ps
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS               NAMES
b7fef5c23194        redis:latest        "docker-entrypoint.s…"   3 minutes ago       Up 3 minutes        6379/tcp            url_scanning_service_urldb.1.jncq6ag1l7uithvb4mnuuan27
7a6c29def702        nginx:alpine        "nginx -g 'daemon of…"   3 minutes ago       Up 3 minutes        80/tcp              url_scanning_service_proxy.1.hjyyf2n65iaj5zd2m5brrdif5
2a7a43c19ad1        webapp:latest       "/usr/bin/supervisord"   3 minutes ago       Up 3 minutes                            url_scanning_service_app.2.uqu413jpqmr6t7g1qusd2b0s4
868ec0a221ac        webapp:latest       "/usr/bin/supervisord"   3 minutes ago       Up 3 minutes                            url_scanning_service_app.1.hysrwwl4tm11suwxh4pk7v7bh
Ram-Mac:url_scanning_service rregar$ 
Ram-Mac:url_scanning_service rregar$ docker logs 2a7a43c19ad1
/usr/lib/python2.7/dist-packages/supervisor/options.py:461: UserWarning: Supervisord is running as root and it is searching for its configuration file in default locations (including its current working directory); you probably want to specify a "-c" argument specifying an absolute path to a configuration file for improved security.
  'Supervisord is running as root and it is searching '
2020-04-13 04:02:55,259 CRIT Supervisor is running as root.  Privileges were not dropped because no user is specified in the config file.  If you intend to run as root, you can set user=root in the config file to avoid this message.
2020-04-13 04:02:55,270 INFO supervisord started with pid 1
2020-04-13 04:02:56,274 INFO spawned: 'nginx' with pid 8

## 8. Add Bad URL to this system
curl http://0.0.0.0:9000/add_url_api?url=thisisbadurl.com

Ram-Mac:url_scanning_service rregar$ curl http://0.0.0.0:9000/add_url_api?url=thisisbadurl.com
Insert thisisbadurl.com added into redis!
Ram-Mac:url_scanning_service rregar$ 

## 9. Check if this is badurl
Ram-Mac:url_scanning_service rregar$ curl http://0.0.0.0:9000/check_url_api?url=thisisbadurl.com
Url thisisbadurl.com is bad
Ram-Mac:url_scanning_service rregar$ 

and check for good URL
Ram-Mac:url_scanning_service rregar$ curl http://0.0.0.0:9000/check_url_api?url=thisisnotbadurl.com
Url thisisnotbadurl.com is safe
Ram-Mac:url_scanning_service rregar$ 

## 10. List all bad URLs
curl http://0.0.0.0:9000/list_url_api
Some of them all. I can not put full list
Ram-Mac:url_scanning_service rregar$ curl http://0.0.0.0:9000/list_url_api
b'thisisbadurl.com'
b'75ww.com'
b'boquan.net'

## 10. Answer to design questions
Please look into ppt file
