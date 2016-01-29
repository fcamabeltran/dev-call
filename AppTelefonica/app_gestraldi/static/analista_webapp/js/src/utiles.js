	   var app =angular.module('controllerUtiles', []);

   app.controller('DateController', ['$scope', function($scope) {
       $scope.example = {
         value: new Date(2013, 9, 22)
       };
   }]);
