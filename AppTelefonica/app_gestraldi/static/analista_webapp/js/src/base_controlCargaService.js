  var app =angular.module('controlCargaService', []);

  /* Services */
/* http://docs.angularjs.org/api/ngResource.$resource
 Default ngResources are defined as
    get':    {method:'GET'},
  'save':   {method:'POST'},
  'query':  {method:'GET', isArray:true},
  'remove': {method:'DELETE'},
  'delete': {method:'DELETE'} };
 */
 
//para mostrar (Llamada)
app.factory('controlCargaFactory', function ($resource) {
    return $resource('/control/carga/',{},{
        query: { method: 'GET',isArray: true}
    })
});


