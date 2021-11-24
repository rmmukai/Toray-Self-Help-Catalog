"use strict";

// delete_link class related
// This "link" is blank, not connecting to anywhere
const deleteLink = document.querySelectorAll("delete_link");

// overlay class related
const overlay = document.querySelector("overlay");

const overlayOn = function () {
    overlayclassList.remove("hidden");
};

const overlayOff = function () {
    overlay.classList.remove("hidden");
};

// delete_window class related
const deleteWindow = document.querySelectorAll("delete_window");

const deleteWindowOn = function () {
    deleteWindow.classList.remove("hidden");
};

const deleteWindowoff = function () {
    deleteWindow.classList.add("hidden");
};

for (let i = 0; i < deleteLink.length; i++) {
    deleteLink[i].addEventListener("click", function () {
        deleteWindow.classList.remove("hidden");
        overlay.classList.remove("hidden");
    });
}
