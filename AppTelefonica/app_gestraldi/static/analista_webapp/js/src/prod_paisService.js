  var app =angular.module('paisService', []);

  /* Services */
/* http://docs.angularjs.org/api/ngResource.$resource
 Default ngResources are defined as
    get':    {method:'GET'},
  'save':   {method:'POST'},
  'query':  {method:'GET', isArray:true},
  'remove': {method:'DELETE'},
  'delete': {method:'DELETE'} };
 */
 
//para mostrar (pais)
app.factory('qc_paisFactory', function ($resource) {
    return $resource('/production/fraudePais/',{},{
        query: { method: 'GET',isArray: true},           
        create: { method: 'POST' },
        delete: { method: 'DELETE', params: {id: '@id'} }

    })
});


    
//ELIMINAR -UPDATE-SHOW (pais)
    app.factory('sud_paisFactory', function ($resource) {
    return $resource(baseUrl + '/today/analizador/:id', {}, {
        show: { method: 'GET' },
        update: { method: 'PUT', params: {id: '@id'} },
        delete: { method: 'DELETE', params: {id: '@id'} }
    })
});


