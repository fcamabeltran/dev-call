'use strict';

var App = angular.module("analista_webapp", [
    'ui.router',
    'ui.bootstrap',
    'ngResource',
    'ngTable',
    'googlechart',
    'highcharts-ng',
    'controllerAnalista',
    'paisController',
    'paisService',
    'detalleLlamadaController',
    'detalleLlamadaService',
    'controlCargaController',
    'controlCargaService',
    'analisisxRechazoController',
    'analisisxRechazoService'
    ]); 


App.config(['$stateProvider','$httpProvider','$resourceProvider',  function ($stateProvider, $httpProvider,$resourceProvider) {
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.useXDomain = true;
    $httpProvider.defaults.withCredentials = true;
     $resourceProvider.defaults.stripTrailingSlashes = false;

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
        '@': {templateUrl: "/static/analista_webapp/partials/principal/principal.html"}
      }
    })
    
    $stateProvider.state('extra', {
      url: '/extra/datosPersonales/',
      parent: 'root',
      views: {
        '@': {templateUrl: "/static/analista_webapp/partials/extra/datosPersonales.html"}
      }
    })
    $stateProvider.state('extra.inbox', {
      url: '/extra/inbox/',
      parent: 'root',
      views: {
        '@': {templateUrl: "/static/analista_webapp/partials/extra/inbox.html"}
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
        '@': {templateUrl: "/static/analista_webapp/partials/base/rechazoxDetalle.html",controller: "queryAnalisisxRechazo"}
      }
    })

    $stateProvider.state('reporte', {
      url: '/reporte/telefonoOrigenDestino/',
      parent: 'root',
      views: {
        '@': {templateUrl: "/static/analista_webapp/partials/reportes/telefonoOrigenDestino.html",controller:"qc_pais"}
      }
    })
    $stateProvider.state('reporteComercial', {
      url: '/reporte/vistaComercial/',
      parent: 'root',
      views: {
        '@': {templateUrl: "/static/analista_webapp/partials/reportes/vistaComercial.html"}
      }
    })
    $stateProvider.state('base', {
      url: '/base/controlCarga/',
      parent: 'root',
      views: {
        '@': {templateUrl: "/static/analista_webapp/partials/base/controlCarga.html", controller: "queryControlCarga"}
      }
    })

}]);