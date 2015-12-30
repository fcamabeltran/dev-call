'use strict';
var App = angular.module("analista_webapp", ['ui.router','ngResource','controllerAnalista','controllerUtiles']); 

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
        '@': {templateUrl: "/static/analista_webapp/partials/reportes/detalleLlamadas.html" }
      }
    })
  
     $stateProvider.state('analizador', {
      url: '/reporte/analizador/',
      parent: 'root',
      views: {
        '@': {templateUrl: "/static/analista_webapp/partials/reportes/analizador.html", controller: "riskcabLists"}
      }
    })

    $stateProvider.state('reporte', {
      url: '/reporte/telefonoOrigenDestino/',
      parent: 'root',
      views: {
        '@': {templateUrl: "/static/analista_webapp/partials/reportes/telefonoOrigenDestino.html",controller: ""}
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



