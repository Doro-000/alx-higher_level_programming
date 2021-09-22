$(document).ready(function () {
  $.get('https://fourtonfish.com/hellosalut/', { lang: 'fr' }, (data, status) => {
    $('div#hello').text(data.hello);
  });
});
