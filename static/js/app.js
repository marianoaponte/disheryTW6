//Service Worker registration
if ('serviceWorker' in navigator) {
    navigator.serviceWorker.register('./sw.js') /* promise */
        .then(reg => console.log('Service Worker registered successfully!')) /* promise successful */
        .catch(err => console.log('Service Worker was not registered!')) /* promise rejected */

}
