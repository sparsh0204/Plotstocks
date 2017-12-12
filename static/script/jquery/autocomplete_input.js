$(document).ready(function() {$.ajax({
    url: "http://127.0.0.1:8000/static/script/jquery/symbolss.txt",
    dataType: "JSON",
    success: function(data) {
        var autoCompleteData = data;
        $("#symbol").autocomplete({
            source: function(request, response) {
                var results = $.ui.autocomplete.filter(autoCompleteData, request.term);
                response(results.slice(0, 10)); // Display the first 10 results
            }
        });
    }
});
});