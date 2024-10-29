// app/static/js/main.js

// A function to get and display a random Rubaiyat
function randomRubaiyat() {
    pywebview.api.random_rubaiyat().then(function (response) {
        // Display poem_body
        displayPoem(response.poem_body);
    }).catch(function (error) {
        console.error("Error fetching random Rubaiyat:", error);
    });
}

// A function to retrieve and display Rubaiyat related to Booze-ism
function randomRubaiyatInBoozeism() {
    pywebview.api.random_rubaiyat_in_boozeism().then(function (response) {
        // Display poem_body
        displayPoem(response.poem_body);
    }).catch(function (error) {
        console.error("Error fetching Rubaiyat in Booze-ism:", error);
    });
}

// Display poem_body
function displayPoem(poem) {
    var poemDisplay = document.getElementById("poemDisplay");
    if (poemDisplay) {
        poemDisplay.textContent = poem;
    } else {
        console.error("poemDisplay not found");
    }
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