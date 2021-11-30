"use strict";

// delete_link class related
// This "link" is blank, not connecting to anywhere
const deleteLink = document.querySelector("delete_link");
const overlay = document.querySelector("overlay");
const deleteWindow = document.querySelector("delete_window");

// Function for "turning on" the popup window
const deleteWindowOn = function () {
    overlay.classList.remove("hidden");
    deleteWindow.classList.remove("hidden");
};

// Function for "turning off" the popup window
const deleteWindowOff = function () {
    overlay.classList.add("hidden");
    deleteWindow.classList.add("hidden");
};

// When clicking the delete delete link
deleteLink.addEventListener("click", deleteWindowOn);
