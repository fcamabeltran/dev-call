"use strict";

var app =angular.module('controlCargaController',[]);
	//con dataResource inyectamos la factoría  

	app.controller("queryControlCarga",['$scope','controlCargaFactory','NgTableParams', function ($scope,controlCargaFactory,NgTableParams) {
    	//datosResource lo tenemos disponible en la vista gracias a $scope

        $scope.controlCarga = controlCargaFactory.query();  

        $scope.tableParams = new NgTableParams({
            page: 1,            // show first page
            count: 4           // count per page
        }, {    
        	total: $scope.controlCarga.length, // length of data
            getData: function($defer, params) {
             $defer.resolve($scope.controlCarga);
         }
     });



    }]);


