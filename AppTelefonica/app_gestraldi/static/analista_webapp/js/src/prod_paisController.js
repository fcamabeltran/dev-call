"use strict";
    
var app =angular.module('paisController',[]);
	//con dataResource inyectamos la factoría  

	app.controller("qc_pais",['$scope','$uibModal','qc_paisFactory','NgTableParams','$filter', function ($scope,$uibModal,qc_paisFactory,NgTableParams,$filter) {
    	//datosResource lo tenemos disponible en la vista gracias a $scope

        $scope.udpatePais=function(){
            qc_paisFactory.update($scope.Pais)
        };   

        $scope.cancel=function(){
        };

        $scope.createNewPais=function(){ 
            qc_paisFactory.create($scope.Pais)
        };

        $scope.createNewPais=function(id){ 
            qc_paisFactory.delete(id);
        };

        
        $scope.dataPais = qc_paisFactory.query();  

        $scope.tableParams = new NgTableParams({
            page: 1,            // show first page
            count: 4 ,          // count per page
            total: $scope.dataPais.length // length of data
        }, { 
            getData: function($defer, params) {
                $defer.resolve($scope.dataPais);
         }
    });

     //this.defaultConfigTableParams = new NgTableParams({}, { dataset: qc_paisFactory.query() });


       $scope.open = function (size) {
            var modalInstance = $uibModal.open({
              templateUrl: '/static/analista_webapp/partials/reportes/modalTelefonoOrigen.html',
              controller: 'ModalInstanceCtrl',
              size: size,
          });

        };   

    }]);

    app.controller("ModalInstanceCtrl",['$scope','$uibModalInstance','qc_paisFactory', function ($scope,$uibModalInstance,qc_paisFactory) {

      $scope.ok = function () {
        $uibModalInstance.close(qc_paisFactory.create($scope.Pais));
    };

    $scope.cancel = function () {
        $uibModalInstance.dismiss('cancel');
    };
}]);