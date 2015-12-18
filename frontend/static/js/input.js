// Handle accidental form submission via the enter key
(function($) {
    // Prevent Enter Key from Submitting a form
    var input_types = ['number', 'email', 'search', 'password', 'tel', 'text',
                       'url', 'date', 'datetime', 'datetime-local', 'month',
                       'time', 'week', 'radio', 'checkbox'];
    function enterKeyHandler(event) {
        if (event.which == '13') {
            console.log("Enter Key Hit");
            if (event.currentTarget.nodeName.toLowerCase() === 'textarea') {
                console.log("Stopping Propagation");
                event.stopPropagation();
            } else if (event.currentTarget.nodeName.toLowerCase() === 'input') {
                if (input_types.indexOf(event.currentTarget.type) >= 0) {
                    console.log("Stopping Propagation");
                    event.stopPropagation();
                    console.log("Stopping Default Behavior");
                    event.preventDefault();
                }
            } else if (event.currentTarget.nodeName.toLowerCase() == 'select'){
                event.stopPropagation();
            }
        }
    }
    $('form').on('keypress', 'textarea', enterKeyHandler);
    $('form').on('keypress', 'input', enterKeyHandler);
    $('form').on('keypress', 'select', enterKeyHandler);
})(jQuery);
