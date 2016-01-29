/* Services */
/* http://docs.angularjs.org/api/ngResource.$resource
 Default ngResources are defined as
 'get':    {method:'GET'},
 'save':   {method:'POST'},
 'query':  {method:'GET', isArray:true},
 'remove': {method:'DELETE'},
 'delete': {method:'DELETE'}
 */

var services = angular.module('controllerPais', ['ngResource']);//    //SHOW
services.factory('PaisFactory', function ($resource) {
    return $resource('/fraude/mantenimiento/fraudePais/', {}, {
        query: { method: 'GET', params: {}, isArray: false }
        
    })
});

//ADD

services.factory('PaissFactory', function ($resource) {
    return $resource('/fraude/mantenimiento/fraudePais/', {}, {
        query: { method: 'GET', isArray: true },
        create: { method: 'POST' }
    })
});

//UPDATE - DELETE - 
services.factory('PaisFactory', function ($resource) {
    return $resource('/fraude/mantenimiento/fraudePais/:id', {}, {
        show: { method: 'GET' },
        update: { method: 'PUT', params: {id: '@id'} },
        delete: { method: 'DELETE', params: {id: '@id'} }
    })
var = services.factory('PaisFactory',function($resource))

});//