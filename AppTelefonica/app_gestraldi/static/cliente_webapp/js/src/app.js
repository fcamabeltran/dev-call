'use strict';
var App = angular.module("cliente_webapp", ['ngRoute','controllerCliente','controllerUtiles']); 


App.config(['$routeProvider', '$httpProvider', function ($routeProvider, $httpProvider) {

    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.useXDomain = true;
    $httpProvider.defaults.withCredentials = true;

    $routeProvider

    //Routers 
    $routeProvider
        .when('/home/', {
            templateUrl: "/static/cliente_webapp/partials/index.html",
            controller: "controllers"
        })
        .when('/reporte/consulta/', {
            templateUrl: "/static/cliente_webapp/partials/reportes/consulta.html",
            controller: ""
        })
        .when('/reporte/consulta/detalle/', {
            templateUrl: "/static/cliente_webapp/partials/reportes/detalleReporte.html",
            controller: ""
        })
        .otherwise({
            redirectTo: '/'
        });

}]);




