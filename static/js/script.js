function movies_f(page= -1) {
    var g = document.getElementById("genre");
    var genre = g.options[g.selectedIndex].text;
    var c = document.getElementById("country");
    var country = c.options[c.selectedIndex].text;
    if (country === "----") {
        country = "any";
    }
    if (genre === "----") {
        genre = "any";
    }
    if (page === -1) {
        page = 0;
    }
    let searchParam = document.getElementById("searchFormInput").innerHTML;
    document.location.search = `${document.location.search}?genre=${genre}&country=${country}&page=${page}&search=${searchParam}`;
    console.log('123');
}

function movies_search() {
    let searchParam = document.getElementById("searchFormInput").innerHTML;
    document.location.search = `${document.location.search}&search=${searchParam}`;
}