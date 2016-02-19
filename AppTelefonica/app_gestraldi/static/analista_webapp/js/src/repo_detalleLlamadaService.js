  var app =angular.module('detalleLlamadaService', []);

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
app.factory('detalleLlamadaFactory', function ($resource) {
    return $resource('/today/tasacion/',{},{
        query: { method: 'GET',isArray: true}
    })
});


