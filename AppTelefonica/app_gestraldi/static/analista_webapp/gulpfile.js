var gulp = require('gulp'),
    uglify = require('gulp-uglifyjs');

var paths = {
    scripts: [
        //librerias del sistema
        'bower_components/angular/angular.js',
        'bower_components/angular-ui-router/release/angular-ui-router.js',        
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
        //librerias externas
        'bower_components/angular-resource/angular-resource.js',
        //Librerias locales
        'js/src/app.js'     ,
        'js/src/controllers.js',
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



