"use strict";

var app =angular.module('analisisxRechazoController',[]);
	//con dataResource inyectamos la factoría  

	app.controller("queryAnalisisxRechazo",['$scope','analisisxRechazoFactory','NgTableParams', function ($scope,analisisxRechazoFactory,NgTableParams) {
    	//datosResource lo tenemos disponible en la vista gracias a $scope

        $scope.controlAnalisisxRechazo = analisisxRechazoFactory.query();  

        $scope.tableParams = new NgTableParams({
            page: 1,            // show first page
            count: 4           // count per page
        }, {    
        	total: $scope.controlAnalisisxRechazo.length, // length of data
            getData: function($defer, params) {
             $defer.resolve($scope.controlAnalisisxRechazo);
         }
     });



    }]);


