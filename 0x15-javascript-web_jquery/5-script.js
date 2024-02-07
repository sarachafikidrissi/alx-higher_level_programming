const newElement = $('<li>Item</li>');
$('DIV#add_item').click(function(){
    $('UL.my_list').append(newElement);
});
