var app = angular.module('controllersPais', []);//app.controller('PaisListCtrl', ['$scope', 'PaissFactory', 'PaisFactory', '$location',
    function ($scope, PaissFactory, PaisFactory, $location) {//        // callback for ng-click 'editPais':
        $scope.editPais = function (paisId) {
            $location.path('/pais-detail/' + paisId );
        };//        // callback for ng-click 'deletePais':
        $scope.deletePais = function (paisId) {
            PaisFactory.delete({ id: paisId });
            $scope.pais = PaissFactory.query();
        };
        // callback for ng-click 'createPais':
        $scope.createPais = function () {
            $location.path('/pais-creation');
        };//        $scope.pais = PaissFactory.query();
    }]);


  /* ... *///  /* ..Controlador Actualizar y Cancelar. */
app.controller('PaisDetailCtrl', ['$scope', '$routeParams', 'PaisFactory', '$location',
    function ($scope, $routeParams, PaisFactory, $location) {//        // callback for ng-click 'updatePais':
        $scope.updatePais = function () {
            PaisFactory.update($scope.Pais);
            $location.path('/Pais-list');
        };//        // callback for ng-click 'cancel':
        $scope.cancel = function () {
            $location.path('/Pais-list');
         };//        $scope.Pais = PaisFactory.show({id: $routeParams.id});
    }]);
        /* ..Controlador Crear Pais. *///app.controller('PaisCreationCtrl', ['$scope', 'PaissFactory', '$location',
    function ($scope, PaissFactory, $location) {//        // callback for ng-click 'createNewPais':
        $scope.createNewPais = function () {
            PaissFactory.create($scope.Pais);
            $location.path('/Pais-list');
        }
    }]);


app.factory('PaisesService', function ($http, $q) {
     var api_url = "/paises/";
     return {
         get: function (post_id) {
             var url = api_url + post_id + "/";
             var defer = $q.defer();
             $http({method: 'GET', url: url}).
                 success(function (data, status, headers, config) {
                     defer.resolve(data);
                 })
                 .error(function (data, status, headers, config) {
                    //.error(function(data, status, headers,config))
                     defer.reject(status);
                 });
             return defer.promise;
         },
         list: function () {
             var defer = $q.defer();
             $http({method: 'GET', url: api_url}).
                 success(function (data, status, headers, config) {
                     defer.resolve(data);
                 }).error(function (data, status, headers, config) {
                     defer.reject(status);
                 });
             return defer.promise;
         },
         update: function (post) {
             var url = api_url + post.id + "/";
             var defer = $q.defer();
             $http({method: 'PUT',
                 url: url,
                 data: post}).
                 success(function (data, status, headers, config) {
                     defer.resolve(data);
                 }).error(function (data, status, headers, config) {
                     defer.reject(status);
                 });
             return defer.promise;
         },


         save: function (post) {
             var url = api_url;
             var defer = $q.defer();
             $http({method: 'POST',
                 url: url,
                 data: post}).

                 data : post }).
                 success(function (data, status, headers, config) {
                     defer.resolve(data);
                 }).error(function (data, status, headers, config) {
                     defer.reject(status);
                 });
             return defer.promise;
         },
     }
 });