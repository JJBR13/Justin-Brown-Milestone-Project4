/* Tab js */
function openTab(evt, tabName) {
    var i, tabcontent, tabbuttons;

    // Hide all tab contents
    tabcontent = document.getElementsByClassName("tab-content");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }

    // Remove the active class from all tab buttons
    tabbuttons = document.getElementsByClassName("tab-button");
    for (i = 0; i < tabbuttons.length; i++) {
        tabbuttons[i].className = tabbuttons[i].className.replace(" active", "");
    }

    // Show the current tab and add the active class to the clicked button
    document.getElementById(tabName).style.display = "block";
    evt.currentTarget.className += " active";
}

/* country js */
let countrySelected = $('#id_default_country').val();
if (!countrySelected || countrySelected === '') {
    $('#id_default_country').css('color', '#aab7c4');
}

$('#id_default_country').change(function() {
    countrySelected = $(this).val();
    if (!countrySelected || countrySelected === '') {
        $(this).css('color', '#aab7c4');
    } else {
        $(this).css('color', '#000');
    }
});
