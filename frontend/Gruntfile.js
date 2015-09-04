module.exports = function (grunt) {
    grunt.initConfig({
        watch: {
            sass: {
                files: '*.scss',
                tasks: ['sass']
            },
            scripts: {
                files: '*.es6.js',
                tasks: ['babel']
            },
            typeset: {
                files: '*.html',
                tasks: ['babel']
            }
        },
        sass: {
            dev: {
                files: {
                    'main.css': 'main.scss'
                }
            }
        },
        babel: {
            options: {
                sourceMap: true
            },
            dist: {
                files: {
                    'app.es5.js': 'app.es6.js'
                }
            }
        },
        typeset: {
            options: {
                ignore: '.skip',
                only: '.typeset',
                dest: 'index.html'
            },
            files: [
                'index.html',
            ]
        },
        browserSync: {
            default_options: {
                bsFiles: {
                    src: ['*.css', '*.html', '*.js']
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
    grunt.loadNpmTasks('grunt-contrib-sass');
    grunt.loadNpmTasks('grunt-contrib-watch');
    grunt.loadNpmTasks('grunt-browser-sync');
    grunt.loadNpmTasks('grunt-babel');
    grunt.loadNpmTasks('grunt-typeset');

    // define default task
    grunt.registerTask('default', ['browserSync', 'watch']);
    grunt.registerTask('test', ['typeset']);
};
