
let word = document.querySelector(".text");
const stuffBtn = document.querySelector(".btn-change");

const url = `http://127.0.0.1:6060/`;
fetch(url)
    .then((response) => {
        return response.json();
    })
    .then((data) => {
        console.log(word)
        console.log(data["name"])
        word.textContent = data["name"];
    });

// word.addEventListener("click", function () {
//     //Create an Li out of thin air
//     word = data[0].WeatherText;
// });