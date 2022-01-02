function addField() {
    //get recipecontainer
    let main_cont = document.getElementById("recipecontainer");


    //create inner container
    let inner_cont = document.createElement("div");
    inner_cont.id = "formdiv" + id_counter;
    inner_cont.className = "formclass-form";


    //add form, button and br to inner container
    //form
    let input_form = document.createElement("input");

    input_form.type = "text";
    input_form.id = "form" + id_counter;

    inner_cont.appendChild(input_form);

    //button
    const delete_button = document.createElement("button");

    delete_button.type = "button";
    delete_button.id = "deletebtn" + id_counter;
    delete_button.className = "delbtn-form";
    delete_button.setAttribute('onclick', "removeField(this.id)");
    delete_button.innerText = "-";

    inner_cont.appendChild(delete_button);

    //br
    inner_cont.appendChild(document.createElement("br"));


    //append the inner_cont to main_cont
    main_cont.appendChild(inner_cont);


    //increase id counter and fields counter.
    id_counter++;
    fields_counter++;
}