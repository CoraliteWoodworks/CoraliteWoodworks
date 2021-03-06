/*global module:false*/
module.exports = function (grunt) {

    // Project configuration.
    grunt.initConfig({
        // Metadata.
        pkg: grunt.file.readJSON('package.json'),
        uglify: {
            target: {
                options: {
                    mangle: false
                },
                files: {
                    'Coralite/static/js/main.min.js': 'Coralite/static/js/main.js',
                    'Coralite/static/js/util.min.js': 'Coralite/static/js/util.js',
                    'Coralite/static/js/skel.min.js': 'Coralite/static/js/skel.js',
                    'Coralite/static/js/skel-layers.min.js': 'Coralite/static/js/skel-layers.js',
                    'Coralite/static/js/jquery.scrollzer.min.js': 'Coralite/static/js/jquery.scrollzer.js',
                    'Coralite/static/js/jquery.scrolly.min.js': 'Coralite/static/js/jquery.scrolly.js',
                    'Coralite/static/js/ie/html5shiv.min.js': 'Coralite/static/js/ie/html5shiv.js'

                }
            }
        },
        cssmin: {
            style: {
                src: ['Coralite/static/css/prologue.css', 'Coralite/static/css/main.css'],
                dest: 'Coralite/static/css/coralite.min.css'
            }
        }
    });

    // These plugins provide necessary tasks.
    grunt.loadNpmTasks('grunt-contrib-concat');
    grunt.loadNpmTasks('grunt-contrib-uglify');
    grunt.loadNpmTasks('grunt-contrib-watch');
    grunt.loadNpmTasks('grunt-contrib-cssmin');

    // Default task.
    grunt.registerTask('default', ['cssmin', 'uglify']);

};