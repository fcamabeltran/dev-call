var gulp = require('gulp'),
    uglify = require('gulp-uglifyjs');

var paths = {
    scripts: [        
        'bower_components/angular/angular.js',
        'bower_components/jquery/dist/jquery.min.js',
        'bower_components/angular-animate/angular-animate.min.js',
        'bower_components/bootstrap-sass/assets/javascripts/bootstrap/transition.js',
        'bower_components/bootstrap-sass/assets/javascripts/bootstrap/collapse.js',
        'bower_components/bootstrap-sass/assets/javascripts/bootstrap/dropdown.js',
        'bower_components/bootstrap-sass/assets/javascripts/bootstrap/button.js',
        'bower_components/bootstrap-sass/assets/javascripts/bootstrap/tooltip.js',
        'bower_components/bootstrap-sass/assets/javascripts/bootstrap/alert.js',
        'bower_components/slimScroll/jquery.slimscroll.min.js',
        'bower_components/widgster/widgster.js',
        'bower_components/pace.js/pace.js',
        'bower_components/angular-touch/angular-touch.min.js',

        'bower_components/angular-ui-bootstrap-bower/ui-bootstrap.js',
        'bower_components/angular-resource/angular-resource.js',
        'bower_components/angular-ui-router/release/angular-ui-router.js',

        'bower_components/ng-table/dist/ng-table.js',
        'bower_components/angular-google-chart/ng-google-chart.js',
        'bower_components/highcharts-ng/src/highcharts-ng.js',
        
        'js/src/app.js',
        'js/src/controllers.js',
        'js/src/prod_paisController.js',
        'js/src/repo_detalleLlamadaController.js',

        'js/src/prod_paisService.js',
        'js/src/repo_detalleLlamadaService.js',

        'js/src/table.js',
        'js/src/utiles.js',
                
    ]
};

gulp.task('scripts', function () {
    return gulp.src(paths.scripts)
        .pipe(uglify('main.min.js', {
            outSourceMap: true,
            enclose: true,
            mangle: false
        }))
        .pipe(gulp.dest('js/dist/'));
});

gulp.task('watch', function () {
    gulp.watch(paths.scripts, ['scripts']);
});

gulp.task('default', ['scripts']);



