document.ready(function ($) {
  const btn = $('#add_item');
  const listItems = $('UL.my_list');
  btn.click(function () {
    list.items.append('<li>Item</li>');
  });
});
