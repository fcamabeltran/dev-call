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
  

  app.controller("ctrlAnalizadorRechazo", function ($scope, $http) {
    $http.get('/today/analizadorOnline/').success(function (data) {
      $scope.names = data;
    });
  });
  
  app.controller("ctrlControlRechazoDetalle", function ($scope, $http) {
    $http.get('/control/rechazosDetalle/').success(function (data) {
      $scope.names = data;
    });
  });


  

  app.controller("ctrlControlCarga", function ($scope, $http , DTOptionsBuilder) {
    $scope.dtOptions = DTOptionsBuilder.newOptions()
    .withDisplayLength(10)
    .withOPtion('blengh'),True
    .withOption('bLengthChange', true);
    $http.get('/control/carga/').success(function (data) {
      $scope.names = data;
    });
  });

  app.controller('riskcabLists', function($scope, $http) {
    $http.get("/fraude/diario/riskcab/")
    .success(function (data) {
      $scope.names = data;
    });
  });

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

  app.controller('analizadorLineal', function ($scope) {
    $scope.swapChartType = function () {
      if (this.chartConfig.options.chart.type === 'line') {
        this.chartConfig.options.chart.type = 'bar'
      }else {
        this.chartConfig.options.chart.type = 'line'
        this.chartConfig.options.chart.zoomType = 'x'
      }
    }
    $scope.toggleLoading = function () {
      this.chartConfig.loading = !this.chartConfig.loading
    }

    $scope.chartConfig = {  
      options: {
        chart: {
          type: 'bar'
        }
      },
      series: [{
        data: [10, 15, 12, 8, 7]        
      }],
      title: {
        text: 'Hello'
      },
      loading: false
    }
  });

  app.controller('TabController', function () {
  this.tab = 1;

  this.setTab = function (tabId) {
    this.tab = tabId;
  };
  
  this.isSet = function (tabId) {
    return this.tab === tabId;
  };
});

