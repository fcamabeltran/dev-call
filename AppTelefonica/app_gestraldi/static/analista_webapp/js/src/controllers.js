var app =angular.module('controllerAnalista', ['datatables']);
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

  app.controller("ctrlControlCarga", function ($scope, $http , DTOptionsBuilder) {
       // DataTables configurable options
      $scope.dtOptions = DTOptionsBuilder.newOptions()
        .withDisplayLength(10)
        .withOption('bLengthChange', true);
        
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

