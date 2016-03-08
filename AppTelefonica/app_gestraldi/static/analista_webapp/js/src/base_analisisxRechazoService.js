  var app =angular.module('analisisxRechazoService', []);

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
app.factory('analisisxRechazoFactory', function ($resource) {
    return $resource('/control/rechazosDetalle/',{},{
        query: { method: 'GET',isArray: true}
    })
});


