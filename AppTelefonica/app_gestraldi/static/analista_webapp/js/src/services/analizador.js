  var app =angular.module('controllerAnalista', ["highcharts-ng"]);

  app.controller("ctrlAnalizador", function ($scope, $http) {
      $http.get('/today/analizador/').success(function (data) {
        $scope.names = data;
      });

  /* Services */
/* http://docs.angularjs.org/api/ngResource.$resource
 Default ngResources are defined as
 'get':    {method:'GET'},
 'save':   {method:'POST'},
 'query':  {method:'GET', isArray:true},
 'remove': {method:'DELETE'},
 'delete': {method:'DELETE'}
 */

var appAnalizador = angular.module('analizadorService', []);//    //SHOW

paisService.factory('viewAnalizadorService', function ($resource) {
    return $resource('/today/analizador/', {}, {
         	query: { method: "GET", isArray: true },
            create: { method: "POST"},
            get: { method: "GET"},
            remove: { method: "DELETE"},
            update: { method: "PUT"}
    });
});
