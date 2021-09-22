const MyList = $('ul.my_list');
const AddItem = $('div#add_item');
const RemoveItem = $('div#remove_item');
const ClearList = $('div#clear_list');

AddItem.click(function () {
  MyList.append('<li>Item</li>');
});

RemoveItem.click(function () {
  MyList.children().last().remove();
});

ClearList.click(function () {
  MyList.empty();
});
