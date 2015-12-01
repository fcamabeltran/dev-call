var App = angular.module("analista_webapp", ['ngRoute','controllerAnalista','controllerUtiles']); 

App.config(['$routeProvider', '$httpProvider', function ($routeProvider, $httpProvider) {

    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';

    $httpProvider.defaults.useXDomain = true;
    $httpProvider.defaults.withCredentials = true;

    //Routers
    $routeProvider
        .when('/home/', {
            templateUrl: "/static/analista_webapp/partials/index.html",
            controller: "ctrlIndex"
        })
        .when('/reporte/detalleLlamadas/', {
            templateUrl: "/static/analista_webapp/partials/tiws_reportes/detalleLlamadas.html",
            controller: "ctrlTasacion"
        })
        .when('/reporte/analizador/', {
            templateUrl: "/static/analista_webapp/partials/tiws_reportes/analizador.html",
            controller: "riskcabLists"
        })
        .when('/reporte/telefonoOrigenDestino/', {
            templateUrl: "/static/analista_webapp/partials/tiws_reportes/telefonoOrigenDestino.html",
            controller: ""
        })
        .when('/reporte/traficoAnomalo/', {
            templateUrl: "/static/analista_webapp/partials/tiws_reportes/traficoAnomalo.html",
            controller: ""
        })
        .when('/reporte/vistaComercial/', {
            templateUrl: "/static/analista_webapp/partials/tiws_reportes/vistaComercial.html",
            controller: ""
        })
        .when('/control/controlCarga/', {
            templateUrl: "/static/analista_webapp/partials/tiws_control/controlCarga.html",
            controller: "ctrlControlCarga"
        })
        .otherwise({
            redirectTo: '/'
        });
}]);

