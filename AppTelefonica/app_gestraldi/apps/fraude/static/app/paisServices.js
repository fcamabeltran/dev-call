/* Services */
/* http://docs.angularjs.org/api/ngResource.$resource
 Default ngResources are defined as
 'get':    {method:'GET'},
 'save':   {method:'POST'},
 'query':  {method:'GET', isArray:true},
 'remove': {method:'DELETE'},
 'delete': {method:'DELETE'}
 */


app.module(''TodoList.controllers),

angular.module('ToDoList.controllers', ['$http]',function($scope,$http))
    .controller('MainCtrl', ['$scope', '$http', function($scope, $http) {

        $scope.newTodo = function() {
            // Hacemos un POST a la API para dar de alta nuestro nuevo ToDo
            $http.post("/api/todo", $scope.nTodo).success(function(response) {
                if(response.status === "OK") { // Si nos devuelve un OK la API...
                    $scope.nTodo = {}; // Limpiamos el scope
                    getTodos(); // Actualizamos la lista de ToDo's
                }
            });
        }

        $scope.deleteTodo = function(id) {
            // Hacemos una petición DELETE a la API para borrar el id que nos pase el html por parametro
            $http.delete("/api/todo/" + id).success(function(response) {
                if(response.status === "OK") { // Si la API nos devuelve un OK...
                    getTodos(); // Actualizamos la lista de ToDo's
                }
            });
        }

        $scope.updateTodo = function(todo) {
            todo.id = todo._id; // Pasamos la _id a id para mayor comodidad del lado del servidor a manejar el dato.
            delete todo._id; // Lo borramos para evitar posibles intentos de modificación de un ID en la base de datos

            // Hacemos una petición PUT para hacer el update a un documento de la base de datos.
            $http.put("/api/todo", todo).success(function(response) {
                if(response.status === "OK") {
                    getTodos(); // Actualizamos la lista de ToDo's
                }
            });
        }

        // Creamos una función para obtener los datos de la base de datos y actualizarlos cada que sea necesario.
        var getTodos = function() {
            $http.get("/api/todo").success(function(response) {
                if(response.status == "OK") {
                    $scope.todos = response.data;
                }
            })
        }

        getTodos(); // Obtenemos la lista de ToDo al cargar la página


    }]);

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