require.config({
    baseUrl: "/static/", // it's needed first slash for this is working
    paths: {
    	'jquery': 'https://ajax.googleapis.com/ajax/libs/jquery/1.11.0/jquery.min',
        'prism': 'https://cdnjs.cloudflare.com/ajax/libs/prism/0.0.1/prism.min',
        'underscore-min': 'https://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.7.0/underscore-min',
        'backbone-min': 'https://cdnjs.cloudflare.com/ajax/libs/backbone.js/1.1.2/backbone-min',
        'socket.io': 'https://cdn.socket.io/socket.io-1.2.1',
        'bootstrap': 'javascripts/bootstrap.min',
        'global': 'javascripts/global'
    },
    shim: {
        'jquery': {
            exports: '$'
        },
        'underscore-min': {
            exports: '_'
        },
        'backbone-min': {
            deps: ['jquery','underscore-min'],
            exports: 'Backbone'
        },
        'bootstrap': {
            deps: ['jquery']
        },
        'global': {
            deps: ['bootstrap','backbone-min','socket.io'],
        },
    }
});

require(['global']);
require(['prism']);