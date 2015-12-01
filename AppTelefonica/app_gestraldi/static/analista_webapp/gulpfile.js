var gulp = require('gulp'),
    uglify = require('gulp-uglifyjs');

var paths = {
    scripts: [
        'bower_components/angular/angular.js',
        'bower_components/angular-route/angular-route.js',
        'js/src/app.js',
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
