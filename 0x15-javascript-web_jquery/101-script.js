$(document).ready(function() {
    const element = $('UL.my_list');
    const newElement = $('<li>Item</li>');
    $('DIV#add_item').click(function(){
        $(element).append(newElement);
    });
    $('DIV#remove_item').click(function(){
        $(newElement).remove();
    });
    $('DIV#clear_list').click(function(){
        $("ul").empty();
    });
});