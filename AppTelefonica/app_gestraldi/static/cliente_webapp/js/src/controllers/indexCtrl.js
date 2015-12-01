var app =angular.module("analista_webapp", []);

  app.controller("indexCtrl", function ($scope, $http) {
      $http.get('/api/me/').success(function (data) {
          $scope.user = data;
      });
  });
  app.controller("tasacionList", function ($scope, $http) {
      $http.get('/fraude/diario/tasacion/').success(function (data) {
        $scope.names = data;
      });
  });





