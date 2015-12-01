'use strict';
var App = angular.module("cliente_webapp", ['ngRoute']);

App.config(['$routeProvider', '$httpProvider', function ($routeProvider, $httpProvider) {

    
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';

    $httpProvider.defaults.useXDomain = true;
    $httpProvider.defaults.withCredentials = true;

    $routeProvider
        .when('/', {
            templateUrl: "/static/cliente_webapp/partials/index.html",
            controller: "indexCtrl"
        })
        .when('/reporte/detalleLlamadas/', {
            templateUrl: "/static/analista_webapp/partials/reportes/detalleLlamadas.html",
            controller: "indexCtrl"
        })
        .otherwise({
            redirectTo: '/'
        });
}]);