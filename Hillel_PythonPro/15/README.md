# [Homework 15 • PokeAPI integrationt](https://lms.ithillel.ua/groups/63c0179f2482232c29371552/homeworks/64667a2de3071359d9792066)

## Acceptance criteria:

- [ ] You must repeat the lesson code and integrate it into yours as a mandatory step.
- [ ] Next API endpoints are integrated into the application:
	- [ ] HTTP GET /api/pokemons/<str:name> -> Fetches the pokemon from the API and saves to the cache like on the lesson
	- [ ] HTTP GET /api/pokemons/ -> Returns all pokemons that are available in the cache variable
	- [ ] HTTP DELETE /api/pokemons/<str:name> -> Removes the pokemon from the cache

As you can see now we use different HTTP methods for the same API endpoint.  
You might find [this document](https://docs.djangoproject.com/en/4.0/ref/request-response/#django.http.HttpRequest.method) pretty useful
