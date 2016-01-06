var app =angular.module('controllerAnalista', []);
  //Controladores
  app.controller("ctrlIndex", function ($scope, $http) {
      $http.get('/api/me/').success(function (data) {
        $scope.names = data;
      });
  });

  app.controller("ctrlTasacion", function ($scope, $http) {
      $http.get('/today/tasacion/').success(function (data) {
        $scope.names = data;
      });
  });
  
  app.controller("ctrlAnalizadorOnline", function ($scope, $http) {
      $http.get('/today/analizadorOnline/').success(function (data) {
        $scope.names = data;
      });
  });

  app.controller("ctrlControlCarga", function ($scope, $http , DTOptionsBuilder) {
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

