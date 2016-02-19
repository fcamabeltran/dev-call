'use strict';

var App = angular.module("analista_webapp", ['ui.router',
    'ui.bootstrap',
    'ngResource',
    'ngTable',
    'googlechart',
    'highcharts-ng',
    'controllerAnalista',
    'paisController',
    'paisService',
    'detalleLlamadaController',
    'detalleLlamadaService']); 


App.config(['$stateProvider','$httpProvider',  function ($stateProvider, $httpProvider) {
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.useXDomain = true;
    $httpProvider.defaults.withCredentials = true;

    $stateProvider.state('root', {
      abstract: true,
      views: {
        '@': {   },
        'sidebar@': {templateUrl: "/static/analista_webapp/partials/sidebar_analista.html" }
      }
    }) 
    
    $stateProvider.state('home', {
      url: '',
      parent: 'root',
      views: {
        '@': {templateUrl: "/static/analista_webapp/partials/reportes/detalleLlamadas.html"}
      }
    })

    $stateProvider.state('consulta', {
      url: '/reporte/detalleLlamadas/',
      parent: 'root',
      views: {
        '@': {templateUrl: "/static/analista_webapp/partials/reportes/detalleLlamadas.html",
        controller:"queryLLamada" }
      }
    })
    $stateProvider.state('anlizQuery', {
      url: '/reporte/detalleLlamadas/',
      parent: 'root',
      views: {
        '@': {templateUrl: "/static/analista_webapp/partials/reportes/query.html" }
      }
    })

    $stateProvider.state('analizador',{
      url: '/reporte/analizador/',
      parent: 'root',
      views: {
        '@': {templateUrl: "/static/analista_webapp/partials/reportes/analizador.html", controller: "ctrlAnalizadorOnline"}
      }
    })

    $stateProvider.state('rechazos', {
      url: '/control/analisis/',
      parent: 'root',
      views: {
        '@': {templateUrl: "/static/analista_webapp/partials/base/rechazoxDetalle.html",controller: "ctrlControlRechazoDetalle"}
      }
    })

    $stateProvider.state('reporte', {
      url: '/reporte/telefonoOrigenDestino/',
      parent: 'root',
      views: {
        '@': {templateUrl: "/static/analista_webapp/partials/reportes/telefonoOrigenDestino.html",controller:"qc_pais"}
      }
    })

    $stateProvider.state('control', {
      url: '/control/controlCarga/',
      parent: 'root',
      views: {
        '@': {templateUrl: "/static/analista_webapp/partials/control/controlCarga.html", controller: "ctrlControlCarga"}
      }
    })
}]);