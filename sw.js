//Service Worker installation
self.addEventListener('install', evt => {
    console.log('Service Worker installed successfully!')
});

//Service Worker activation
self.addEventListener('activate', evt => {
    console.log('Service Worker activated successfully!')
});