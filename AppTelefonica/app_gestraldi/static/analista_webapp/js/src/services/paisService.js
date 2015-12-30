/* Services */
/* http://docs.angularjs.org/api/ngResource.$resource
 Default ngResources are defined as
 'get':    {method:'GET'},
 'save':   {method:'POST'},
 'query':  {method:'GET', isArray:true},
 'remove': {method:'DELETE'},
 'delete': {method:'DELETE'}
 */

var paisService = angular.module('paisService', []);//    //SHOW

paisService.factory('paisesService', function ($resource) {
    return $resource('/fraude/mantenimiento/fraudePais/', {}, {
         	query: { method: "GET", isArray: true },
            create: { method: "POST"},
            get: { method: "GET"},
            remove: { method: "DELETE"},
            update: { method: "PUT"}
    });
});
