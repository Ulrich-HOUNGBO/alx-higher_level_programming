$(function () {
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data, status) {
    if (status === 'success') {
      console.log(data);
      const films = data.results;
      for (const film in films) {
        $('#list_movies').append('<li>' + films[film].title + '</li>');
      }
    }
  });
});
