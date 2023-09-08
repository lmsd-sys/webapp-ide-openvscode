const cacheName = 'cache-v1';
const precacheResources = ['/'];

self.addEventListener('install', (event) => {
	console.log('Service worker install event!');
	event.waitUntil(caches.open(cacheName).then((cache) => cache.addAll(precacheResources)));
});

self.addEventListener('activate', (event) => {
	console.log('Service worker activate event!');
	//https://stackoverflow.com/questions/51562781/service-worker-fetch-event-is-not-firing
	return self.clients.claim();
});

self.addEventListener('fetch', (event) => {
	console.log("seen fetch event from service worker, url=" + event.request.url);

	caches.has(event.request).then(() => { console.log("cache had request for '" + event.request.url + "'") });


	//Regular caches usage for html pages:
	event.respondWith(
		caches.match(event.request).then((cachedResponse) => {
			if (cachedResponse) {
				return cachedResponse;
			}
			return fetch(event.request).then(response => {
				if (!response || response.status !== 200 || response.type !== 'basic') {
					console.warn("failed to fetch resource from service worker.");
					return response;
				}

				const responseToCache = response.clone();
				caches.open(cacheName).then((cache) => {
					cache.put(event.request, responseToCache);
				});
				return response;
			});
		}),
	);
});
