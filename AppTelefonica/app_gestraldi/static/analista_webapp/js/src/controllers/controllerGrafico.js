var app = angular.module('myApp', [ 'googlechart' ]);

app.controller('analizadorGrafico', function($scope) {
    var chart1 = {};
    chart1.type = "PieChart";
    chart1.data = [
       ['Component', 'cost'],
       ['Software', 50000],
       ['Hardware', 4562],
       ['Hardware', 40000],
       ['carton', 30000],
      ];
      
      chart1.options = {
        displayExactValues: true,
        width: 400,
        height: 200,
        is3D: true,
        chartArea: {left:10,top:10,bottom:0,height:"100%"}
    };

    chart1.formatters = {
      number : [{
        columnNum: 1,
        pattern: "$ #,##0.00"
      }]
    };

    $scope.chart = chart1;


});


