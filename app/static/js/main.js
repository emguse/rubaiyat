// app/static/js/main.js

// A function to get and display a random Rubaiyat
function randomRubaiyat() {
    pywebview.api.random_rubaiyat().then(function (response) {
        alert("Random Rubaiyat: " + JSON.stringify(response));
    }).catch(function (error) {
        console.error("Error fetching random Rubaiyat:", error);
    });
}

// A function to retrieve and display Rubaiyat related to Booze-ism
function randomRubaiyatInBoozeism() {
    pywebview.api.random_rubaiyat_in_boozeism().then(function (response) {
        alert("Booze-ism Random Rubaiyat: " + JSON.stringify(response));
    }).catch(function (error) {
        console.error("Error fetching Rubaiyat in Booze-ism:", error);
    });
}

// Add an event listener after the DOM is fully loaded
document.addEventListener("DOMContentLoaded", function () {
    var randomButton = document.getElementById("Random");
    var boozeismButton = document.getElementById("Booze-ism");

    if (randomButton) {
        randomButton.addEventListener("click", randomRubaiyat);
    }

    if (boozeismButton) {
        boozeismButton.addEventListener("click", randomRubaiyatInBoozeism);
    }
});