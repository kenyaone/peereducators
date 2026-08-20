const CACHE_VERSION = 'peer-datapost-v1';

// Install service worker - cache on first load
self.addEventListener('install', (e) => {
  e.waitUntil(
    caches.open(CACHE_VERSION).then((cache) => {
      // Try to cache main pages
      Promise.all([
        cache.add('/peereducator/?p=datapost').catch(() => {}),
        cache.add('/peereducator/pwa_datapost').catch(() => {}),
        cache.add('/peereducator/css/style.css').catch(() => {}),
        cache.add('/peereducator/js/app.js').catch(() => {}),
      ]);
      return cache;
    })
  );
  self.skipWaiting();
});

// Activate - clean old caches
self.addEventListener('activate', (e) => {
  e.waitUntil(
    caches.keys().then((cacheNames) => {
      return Promise.all(
        cacheNames.map((cacheName) => {
          if (cacheName !== CACHE_VERSION) {
            return caches.delete(cacheName);
          }
        })
      );
    })
  );
  self.clients.claim();
});

// Fetch - CACHE FIRST for DataPost, network-first for others
self.addEventListener('fetch', (e) => {
  const url = new URL(e.request.url);
  
  // For DataPost pages - use CACHE FIRST strategy
  if (url.pathname === '/peereducator/' && url.searchParams.get('p') === 'datapost') {
    e.respondWith(
      caches.match(e.request).then((cached) => {
        if (cached) return cached;
        
        return fetch(e.request).then((response) => {
          if (response.ok) {
            caches.open(CACHE_VERSION).then((cache) => {
              cache.put(e.request, response.clone());
            });
          }
          return response;
        }).catch((err) => {
          return caches.match('/peereducator/?p=datapost') || 
                 new Response('Offline - page not cached', { status: 503 });
        });
      })
    );
    return;
  }
  
  // For other GET requests - network first
  if (e.request.method === 'GET') {
    e.respondWith(
      fetch(e.request).then((response) => {
        if (response.ok) {
          caches.open(CACHE_VERSION).then((cache) => {
            cache.put(e.request, response.clone());
          });
        }
        return response;
      }).catch(() => {
        return caches.match(e.request).catch(() => {
          return new Response('Offline', { status: 503 });
        });
      })
    );
  }
});
