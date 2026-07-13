const CACHE = "arranchamento-v1";

const arquivos = [
    "/",
    "/static/style.css"
];


self.addEventListener("install", evento => {

    evento.waitUntil(

        caches.open(CACHE)
        .then(cache => cache.addAll(arquivos))

    );

});


self.addEventListener("fetch", evento => {

    evento.respondWith(

        caches.match(evento.request)
        .then(resposta => {

            return resposta || fetch(evento.request);

        })

    );

});