"use strict";

var app =angular.module('detalleLlamadaController',[]);
	//con dataResource inyectamos la factoría  

	app.controller("queryLLamada",['$scope','detalleLlamadaFactory','NgTableParams', function ($scope,detalleLlamadaFactory,NgTableParams) {
    	//datosResource lo tenemos disponible en la vista gracias a $scope

        $scope.dataDetLlamada = detalleLlamadaFactory.query();  

        $scope.tableParams = new NgTableParams({
            page: 1,            // show first page
            count: 4           // count per page
        }, {    total: $scope.dataDetLlamada.length, // length of data
            getData: function($defer, params) {
             $defer.resolve($scope.dataDetLlamada);
         }
     });



    }]);


