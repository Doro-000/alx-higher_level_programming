$(function () {
  const MyButton = $('#btn_translate');
  MyButton.click(function () {
    const InputLang = $('#language_code').val();
    $.get('https://fourtonfish.com/hellosalut/', { lang: InputLang }, (data, status) => {
      $('div#hello').text(data.hello);
    });
  });
});
