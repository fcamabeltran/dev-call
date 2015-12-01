
'use strict';

////    var  app= angular.mdule('app', ['app.services.filters', 'app.services.services', 'app.directives', 'app.controllers']).
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
//          //minic the django Static_url variable
//          STATIC_URL: '/static/'
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
//          $routeProvider.when("/", {
//              templateUrl : "produccion/produccion.html"
//          })
//          //esta es la forma de decirle a angular que vamos a pasar una variable por la url      //

//          //mantenimientoPaises
//          .when('/paises', {
//              templateUrl : "mantenimientos/servicios.html",
//              controller : ""
//            })
//            .when()
//          //.when("/add", {
//        //        title: 'Añadir Pais',
//        //        templateUrl : "mantenimientos/addPais.html",
//        //        controller : "controllers/addController"
//        //    })
//        //    .when("/edit/:id", {
//        //        title: 'Editar Pais',
//        //        templateUrl : "mantenimientos/updatePais.html",
//        //        controller : "controllers/editController"//     //

//        //    })
//        //    .when("/remove/:id", {
//        //        title: 'Eliminar Pais',
//        //        templateUrl : "mantenimientos/paises.html",
//        //        controller : "controllers/removeController"
//        //    })
//         //   .otherwise({ redirectTo : "/"})//
//        })
  var app = angular.module('app',[]);
//  app.config(function($interpolateProvider) {
//  $interpolateProvider.startSymbol('{{');
//  $interpolateProvider.endSymbol('}}');
//  });

    app.controller('servicioList', function($scope, $http) {
      $http.get("/fraude/mantenimiento/fraudeServicios/")
      .success(function (data) {
        $scope.names = data;
      });
    });
//    app.controller('paisesListDEtalle', function($scope, $http) {
//      $http.get("/fraude/mantenimiento/fraudePais/")
//      .success(function (data) {
//        $scope.names = data;
//      });
//    });
//asfa
    app.controller('paisesList', function($scope, $http) {
      $http.get("/fraude/mantenimiento/fraudePaisPrueba/")
      .success(function (data) {
        $scope.names = data;
      });
    });

    app.controller('centralList', function($scope, $http) {
      $http.get("/fraude/mantenimiento/fraudeCentral/")
      .success(function (data) {
        $scope.names = data;
        
      });
    });
    app.controller('rutaList', function($scope, $http) {
      $http.get("/fraude/mantenimiento/fraudeRuta/")
      .success(function (data) {
        $scope.names = data;
      });
    });
    app.controller('serviciosEspecialesList', function($scope, $http) {
      $http.get("/fraude/mantenimiento/fraudeServiciosEspeciales/")
      .success(function (data) {
        $scope.names = data;
      });
    });

    app.controller('riskcabLists', function($scope, $http) {
      $http.get("/fraude/diario/riskcab/")
      .success(function (data) {
        $scope.names = data;
      });
    });


   app.controller('pais', ['$scope', '$http', function($scope, $http) {

        $scope.new = function() {
              console.log( $scope);
        // Hacemos un POST a la API para dar de alta nuestro nuevo ToDo
            $http.post("/fraude/mantenimiento/fraudePais/", $scope.paises).success(function(data) {
                 // Si nos devuelve un OK la API...
                 console.log( $scope.paises);
                    $scope.paises = {}; // Limpiamos el scope
                  //   getTodos(); Actualizamos la lista de ToDo'
               
            });
        }
        
        $scope.delete = function(id) {
      // Hacemos una petición DELETE a la API para borrar el id que nos pase el html por parametro
            $http.delete("/fraude/mantenimiento/fraudePais/" + id +"/").success(function(response) {
                if(response.status === "OK") { // Si la API nos devuelve un OK...
                  getTodos(); // Actualizamos la lista de ToDo's
                }
            });
        }

        $scope.update = function(todo) {
            todo.id = todo._id; // Pasamos la _id a id para mayor comodidad del lado del servidor a manejar el dato.
            delete todo._id; // Lo borramos para evitar posibles intentos de modificación de un ID en la base de datos
            // Hacemos una petición PUT para hacer el update a un documento de la base de datos.
            $http.put("/fraude/mantenimiento/fraudePais/", todo).success(function(response) {
                if(response.status === "OK") {
                    getTodos(); // Actualizamos la lista de ToDo's
                }
            });
        }
        $scope.list = function(todo) {
                getTodos(); //Listar
        }  
        // Creamos una función para obtener los datos de la base de datos y actualizarlos cada que sea necesario.
        var get= function() {
            $http.get("/fraude/mantenimiento/fraudePais/").success(function(response) {
                if(response.status == "OK") {
                    $scope.todos = response.data;
                }
            })
        }
       // getTodos();  Obtenemos la lista de ToDo al cargar la página


    }]);
   app.controller('servicio', ['$scope', '$http', function($scope, $http) {
        $scope.new = function() {
         
        // Hacemos un POST a la API para dar de alta nuestro nuevo ToDo
            $http.post("/fraude/mantenimiento/fraudeServicios/", $scope.servicio).success(function(data) {
                 // Si nos devuelve un OK la API...
        
                    $scope.servicio = {}; // Limpiamos el scope
                  //  getTodos(); Actualizamos la lista de ToDo'            
            });
        }
         $scope.delete = function(id) {
      // Hacemos una petición DELETE a la API para borrar el id que nos pase el html por parametro
            $http.delete("/fraude/mantenimiento/fraudePais/" + id +"/").success(function(response) {
                if(response.status === "OK") { // Si la API nos devuelve un OK...
                 // getTodos(); // Actualizamos la lista de ToDo's
                }
            });
        }

        $scope.update = function(todo) {
            todo.id = todo._id; // Pasamos la _id a id para mayor comodidad del lado del servidor a manejar el dato.
            delete todo._id; // Lo borramos para evitar posibles intentos de modificación de un ID en la base de datos
            // Hacemos una petición PUT para hacer el update a un documento de la base de datos.
            $http.put("/fraude/mantenimiento/fraudePais/", todo).success(function(response) {
                if(response.status === "OK") {
                   // getTodos(); // Actualizamos la lista de ToDo's
                }
            });
        }
        $scope.list = function(todo) {
                getTodos(); //Listar
        }  
        // Creamos una función para obtener los datos de la base de datos y actualizarlos cada que sea necesario.
        var get= function() {
            $http.get("/fraude/mantenimiento/fraudePais/").success(function(response) {
                if(response.status == "OK") {
                    $scope.todos = response.data;
                }
            })
        }
       // getTodos();  Obtenemos la lista de ToDo al cargar la página


    }]);

app.controller('pagination', function($scope, sedeFactory) {
    init();
    $scope.curPage = 0;

    function init() {
        getAll(0);
    }

    function createPagination() {
        console.info("totalCount", $scope.totalCount);
        pagination = new Pagination($scope.totalCount,$scope.curPage);
        $scope.pages = this.pagination.getPages();
        console.info("print ", $scope.pages);
    }

    $scope.goPage = function(page) {
        $scope.curPage =page;
        getAll(page);
    }

    function getAll(page) {
        start = page;
        limit = 10;
        console.info("quuee ", page);

        if (!page) {
            start = 0;
            limit = 10;
        }

        (new sedeFactory({
            "start" : start * limit,
            "limit" : limit
        })).$getAll().then(function(data) {
            $scope.sedes = data.data;
            $scope.totalCount = data.totalCount;
            createPagination();
        });
    }

});

function Pagination(totalCount, curPage) {
    this.curPage = curPage;
    this.pagesInPagination = 5;
    this.rowsPerPage = 10;
    this.totalCount = totalCount;
    this.pages = [];

    this.getPages = function() {
        this.pages = [];
        if (!this.totalCount || this.totalCount == 0)
            return this.pages;
        
        console.info("curPage",this.curPage);
        

        var pages = (this.totalCount + this.rowsPerPage) / this.rowsPerPage;

        var canRight = (pages - this.curPage + 1);
        var canLeft = this.curPage;

        var taken = 0;
        for (i = this.curPage; i < pages && taken < this.pagesInPagination; i++) {
            this.pages.push(i);
            taken++;
        }
        for (i = this.curPage - 1; i >= 0 && taken < this.pagesInPagination; i++) {
            this.pages.push(i);
            taken++;
        }
        this.pages.sort();
        return this.pages;
    }

}