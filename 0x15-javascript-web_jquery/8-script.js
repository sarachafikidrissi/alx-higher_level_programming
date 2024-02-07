const url = "https://swapi-api.alx-tools.com/api/films/?format=json";
const movieList = $('UL#list_movies');
$.get(url, function(data) {
    $.each(data.results, (i, movie) => {
        movieList.append('<li>' + movie.title + '</li>')});
});