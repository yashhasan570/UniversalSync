angular.module('universalsync.core')
    .filter('localeNumber', function () {
        return function (input) {
            return input.toLocaleString();
        };
    });
