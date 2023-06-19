let randomElement = document.getElementById("rand-number");
let randomNumber = Math.floor(Math.random() * 100);
randomElement.innerText = randomNumber.toString();

let addToFriendsButton = document.getElementById("add-to-friends");
addToFriendsButton.addEventListener("click", (addToFriendsEvent) => {
    randomNumber += 1;
    randomElement.innerText = randomNumber.toString();
    addToFriendsEvent.target.disabled = true;
    addToFriendsButton.innerText = "Очікується підтвердження";
});