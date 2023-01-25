$(function () {
  $.ajax({
    type: 'GET',
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    success: function (movies) {
      $.each(movies.results, function (i, result) {
        $('UL#list_movies').append('<li>' + result.title + '</li>');
      });
    }
  });
});
