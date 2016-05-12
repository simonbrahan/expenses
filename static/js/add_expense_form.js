$(
    function() {
        $('input[type=date]').val(new Date().toJSON().slice(0,10));
    }
)
