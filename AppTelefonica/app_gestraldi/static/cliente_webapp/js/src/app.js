'use strict';
var App = angular.module("cliente_webapp", ['ui.router','controllerCliente','controllerUtiles','controllertable']); 

App.config(['$stateProvider','$httpProvider',  function ($stateProvider, $httpProvider) {
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.useXDomain = true;
    $httpProvider.defaults.withCredentials = true;

$stateProvider.state('root', {
  abstract: true,
  views: {
    '@': {   },
    'sidebar@': { templateUrl: "/static/cliente_webapp/partials/sidebar_cliente.html" }
  }
})

$stateProvider.state('home', {
  url: '',
  parent: 'root',
  views: {
    '@': { templateUrl: '/static/cliente_webapp/partials/reportes/consulta.html', controller: 'controllers' }
  }
})


$stateProvider.state('reporte', {
      url: '/reporte/telefonoOrigenDestino/',
      parent: 'root',
      views: {
        '@': {templateUrl: "/static/analista_webapp/partials/reportes/detalleLlamadas.html",controller: ""}
      }
    })


}]);



