// this function executes our search via an AJAX call
function runSearch( term ) {
    // hide and clear the previous results, if any
    $('#results').hide();
    $('tbody').empty();

    // transforms all the form parameters into a string we can send to the server
    var frmStr = $('#diseasesearch').serialize();

    $.ajax({
        url: './ffinal_project.cgi',
        dataType: 'json',
        data: frmStr,
        success: function(data, textStatus, jqXHR) {
            processJSON(data);
        },
        error: function(jqXHR, textStatus, errorThrown) {
            alert("Failed to perform Biomarker/Target search! textStatus: (" + textStatus +
                ") and errorThrown: (" + errorThrown + ")");
        }
    });
}


// this processes a passed JSON structure representing gene matches and draws it
//  to the result table
function processJSON(data) {
    // set the span that lists the match count
    $('#match_count').text(data.match_count);

    // this will be used to keep track of row identifiers
    var next_row_num = 1;

    // iterate over each match and add a row to the result table for each
    $.each(data.matches, function(i, item) {
        var this_row_id = 'result_row_' + next_row_num++;

        // create a row and append it to the body of the table
        $('<tr/>', { "id": this_row_id }).appendTo('tbody');

        // add the biomarker ID column
        $('<td/>', { "text": item.biomarkerid }).appendTo('#' + this_row_id);

        // add the name column
        $('<td/>', { "text": item.biomarkername }).appendTo('#' + this_row_id);

    });

    $.each(data.matches, function(i, item) {
        var this_row_id = 'result_row_' + next_row_num++;

        // create a row and append it to the body of the table
        $('<tr/>', { "id": this_row_id }).appendTo('tbody');
        
        // add the target ID column
        $('<td/>', { "text": item.targetid }).appendTo('#' + this_row_id);

        // add the phase column
        $('<td/>', { "text": item.phase }).appendTo('#' + this_row_id);

    });

    // now show the result section that was previously hidden
    $('#results').show();
}

// run our javascript once the page is ready
$(document).ready(function() {
    $('#submit').click(function() {
        runSearch();
        return false; // prevents 'normal' form submission
    });
})