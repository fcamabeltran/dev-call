var app =angular.module('controllerCliente', []);


  app.controller("ctrlIndex", function ($scope, $http) {
      $http.get('/api/me/').success(function (data) {
        $scope.names = data;
      });
  });

  app.controller("ctrlTasacion", function ($scope, $http) {
      $http.get('/fraude/diario/tasacion/').success(function (data) {
        $scope.names = data;
      });
  });


  app.controller('riskcabLists', function($scope, $http) {
      $http.get("/fraude/diario/riskcab/")
      .success(function (data) {
        $scope.names = data;
      });
    });




