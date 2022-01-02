function removeField(clicked_id) {
    //getting num from string
    let id_no = clicked_id.replace( /^\D+/g, '');

    //converting num to container id:
    let div_id = "formdiv" + id_no;

    //actually deleting the div
    document.getElementById(div_id).remove();

    //decreasing fields counter. Id counter is not decreased.
    fields_counter--;
}