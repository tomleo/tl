module.exports = function (grunt) {
    grunt.initConfig({
        watch: {
            css: {
                files: 'static/css/*.next.css',
                tasks: ['cssnext']
            },
            scripts: {
                files: 'static/js/*.next.js',
                tasks: ['babel']
            },
        },
        cssnext: {
          options: {
              sourcemap: true
          },
          dist: {
              files: {
                "static/css/style.current.css": "static/css/style.next.css"
              }
          }
        },
        babel: {
            options: {
                sourceMap: true
            },
            dist: {
                files: {
                    'static/js/app.current.js': 'static/js/app.next.js'
                }
            }
        },
        browserSync: {
            default_options: {
                bsFiles: {
                    src: ['static/css/*.current.css', '*.html', 'static/js/*.current.js']
                },
                options: {
                    watchTask: true,
                    server: {
                        baseDir: "./",
                        directory: true,
                        index: "index.html"
                    }
                }
            }
        }
    });

    // load npm tasks
    grunt.loadNpmTasks('grunt-contrib-watch');
    grunt.loadNpmTasks('grunt-browser-sync');
    grunt.loadNpmTasks('grunt-babel');
    grunt.loadNpmTasks("grunt-cssnext")

    // define default task
    grunt.registerTask('default', ['browserSync', 'watch']);
};
