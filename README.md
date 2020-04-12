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
 
## Technical Details
In design I choose Python/Flask/RESTful framework that connects to MongoDB for database store
There will be multiple App Servers container processing request. MongoDB databases has its own slave.
