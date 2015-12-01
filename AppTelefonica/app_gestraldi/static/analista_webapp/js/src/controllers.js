var app =angular.module('controllerAnalista', []);

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

  app.controller("ctrlControlCarga", function ($scope, $http) {
      $http.get('/fraude/control/carga/').success(function (data) {
        $scope.names = data;
      });
  });

  app.controller('riskcabLists', function($scope, $http) {
      $http.get("/fraude/diario/riskcab/")
      .success(function (data) {
        $scope.names = data;
      });
    });


  app.controller('DateController', ['$scope', function($scope) {
tasacion       $scope.example = {
         value: new Date(2013, 9, 22)
       };
  }]);
