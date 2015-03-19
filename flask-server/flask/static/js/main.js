require.config({
    baseUrl: "/static/", // it's needed first slash for this is working
    paths: {
    	'jquery': 'https://ajax.googleapis.com/ajax/libs/jquery/1.11.0/jquery.min',
        'underscore': 'js/bb/underscore-min',
        'backbone': 'js/bb/backbone-min',
        'global': 'js/global',
    },
    shim: {
        'jquery': {
            exports: '$'
        },
        'underscore': {
            exports: '_'
        },
        'backbone': {
            deps: ['jquery','underscore'],
            exports: 'Backbone'
        },
        'global': {
            deps: ['backbone'],
        },
    }
});

require(['global']);