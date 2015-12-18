var gulp        = require('gulp');
var postcss     = require('gulp-postcss');
var sourcemaps  = require('gulp-sourcemaps');
var babel       = require('gulp-babel');
var concat      = require('gulp-concat');
var browserSync = require('browser-sync').create();

gulp.task('css', function () {
    return gulp.src('static/css/**/*.css')
        .pipe( sourcemaps.init() )
        .pipe( postcss([ require('autoprefixer'), require('precss') ]) )
        .pipe( sourcemaps.write('.') )
        .pipe( gulp.dest('dist/') );
});

gulp.task('js', function() {
    return gulp.src('static/js/**/*.js')
        .pipe(babel({
            presets: ['es2015']
        }))
        //.pipe(concat('all.js'))
        .pipe(sourcemaps.write('.'))
        .pipe(gulp.dest('dist'));
});

gulp.task('browser-sync', function() {
    browserSync.init({
        server: {
            baseDir: './'
        }
    });
});

gulp.task('serve', ['css', 'js'], function() {
    
    browserSync.init({
        server: {
            baseDir: './'
        }
    });

    gulp.watch('static/css/*.css', ['css']);
    gulp.watch('static/js/*.js', ['js']);
    gulp.watch('*.html').on('change', browserSync.reload);
    gulp.watch('dist/style.css').on('change', browserSync.reload);
    gulp.watch('dist/app.js').on('change', browserSync.reload);
});

gulp.task('default', ['serve'])

