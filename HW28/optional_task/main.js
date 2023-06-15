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

let sendMessageButton = document.getElementById("send-message");
sendMessageButton.addEventListener("click", (sendMessageEvent) => {
    if(sendMessageButton.classList.contains("new-button-color")) {
        sendMessageButton.classList.remove("new-button-color");
    } else {
        sendMessageButton.classList.add("new-button-color");
    }
});

let offerJobButton = document.getElementById("offer-job");
offerJobButton.addEventListener("click", (offerJobEvent) => {
    if(addToFriendsButton.style.display === "none") {
        addToFriendsButton.style.display = "block";
    } else {
        addToFriendsButton.style.display = "none";
    }
});

let passHwButton = document.getElementById("pass-hw");
passHwButton.addEventListener("click", (passHwEvent) => {
    let marksTable = document.getElementById("marks-table");

    let row = marksTable.insertRow();
    let cell1 = row.insertCell(0);
    let cell2 = row.insertCell(1);

    cell1.innerText = "Нове ДЗ";
    cell2.innerText = "10/10";


})