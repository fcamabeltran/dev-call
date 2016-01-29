////	var  app= angular.module('app', ['app.services.filters', 'app.services.services', 'app.directives', 'app.controllers']).
////    app.config(['$routeProvider', function ($routeProvider) {
////        $routeProvider.when('/user-list', {templateUrl: 'partials/user-list.html', controller: 'UserListCtrl'});
////        $routeProvider.when('/user-detail/:id', {templateUrl: 'partials/user-detail.html', controller: 'UserDetailCtrl'});
////        $routeProvider.when('/user-creation', {templateUrl: 'partials/user-creation.html', controller: 'UserCreationCtrl'});
////        $routeProvider.otherwise({redirectTo: '/user-list'});
////    }]);
// //creamos nuestro modulo llamado app//

//var app = angular.module("app",  ['ngResource','ngRoute']);
//        // Configuramos el Satic_url de forma constant
//        app.constant('settings',  {
//        	//minic the django Static_url variable
//        	STATIC_URL: '/static/'
//        });     //z

//        //configuramos nuestros 
//        app.config(function($interpolateProvider) {
//        $interpolateProvider.startSymbol('{[{');
//        $interpolateProvider.endSymbol('}]}');
//        });//
//

//        app.run(
//            //CSRF Token para las comunicaciones por get y post
//            function($http,$cookies){
//                $http.defaults.headers.post['X-CSRFToken'] = $cookies.csrftoken;
//            }
//        )
//    //hacemos el ruteo de nuestra aplicación
//        app.controller 'AppController', ['$scope', '$http', ($scope, $http) ->
//            $scope.posts = []
//            $http.get('/api/posts').then (result) ->
//                angular.forEach result.data, (item) ->
//                    $scope.posts.push item
//        ]       //

//        angular.module('sample', [
//            'djangular', 'sample.filters', 'sample.services', 'sample.directives',
//            'sample.controllers'
//            ]);     //

//        app.config(['$routeProvider','DjangoProperties',
//                function($routeProvider, DjangoProperties) {
//                    $routeProvider.when('/servicios', {
//                        templateUrl: DjangoProperties.STATIC_URL +
//                            'mantenimientos/servicios.html', controller: ''});
//                    $routeProvider.when('/paises', {
//                        templateUrl: DjangoProperties.STATIC_URL +
//                            'produccion/paises.html', controller: ''});
//                    $routeProvider.otherwise({redirectTo: '/'});
//                }
//            ]);
//        app.config(function($routeProvider){
//        	$routeProvider.when("/", {
//        		templateUrl : "produccion/produccion.html"
//        	})
//        	//esta es la forma de decirle a angular que vamos a pasar una variable por la url      //

//        	//mantenimientoPaises
//        	.when('/paises', {
//              templateUrl : "mantenimientos/servicios.html",
//              controller : ""
//            })
//            .when()
//        	//.when("/add", {
//        //		title: 'Añadir Pais',
//        //		templateUrl : "mantenimientos/addPais.html",
//        //		controller : "controllers/addController"
//        //	})
//        //	.when("/edit/:id", {
//        //		title: 'Editar Pais',
//        //		templateUrl : "mantenimientos/updatePais.html",
//        //		controller : "controllers/editController"//     //

//        //	})
//        // 	.when("/remove/:id", {
//        // 		title: 'Eliminar Pais',
//        // 		templateUrl : "mantenimientos/paises.html",
//        // 		controller : "controllers/removeController"
//        // 	})
//         //	.otherwise({ redirectTo : "/"})//
//        })



    
    var app = angular.module("app",[]);
  app.config(function($interpolateProvider) {
  $interpolateProvider.startSymbol('{{');
  $interpolateProvider.endSymbol('}}');
  });

    function servicios($scope, $http) {
    $http.post('/fraude/mantenimiento/fraudeServicios/').
    success(function(data) {
            $scope.servicios = data;
        });
    }
    function paises($scope, $http) {
    $http.get('/fraude/mantenimiento/fraudePais/').
    success(function(data) {
            $scope.paises = data;
        });
    }
    function central($scope, $http) {
    $http.get('/fraude/mantenimiento/fraudeCentral/').
    success(function(data) {
            $scope.central = data;
        });
    }
    function serviciosEspeciales($scope, $http) {
    $http.get('/fraude/mantenimiento/fraudeServiciosEspeciales/').
    success(function(data) {
            $scope.serviciosEspeciales = data;
        });
    }
    function ruta($scope, $http) {
    $http.get('/fraude/mantenimiento/fraudeRuta/').
    success(function(data) {
            $scope.ruta = data;
        });
    }
