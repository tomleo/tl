var site_url = window.location.hostname;

var getLocation = function(href) {
    var l = document.createElement("a");
    l.href = href;
    return l;
};

function add_external_link(jq_a) {
    let _l = getLocation(jq_a.attr('href'));
    if(_l.hostname !== site_url) {
        jq_a.append(' <i class="fa fa-external-link"></i>');
    }
}

$('#main a').each(function() {
    add_external_link($(this));
});

$('footer a').each(function() {
    add_external_link($(this));
});

