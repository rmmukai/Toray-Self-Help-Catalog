"use strict";

// delete_link class related
// This "link" is blank, not connecting to anywhere
const deleteBtn = document.querySelector(".delete_btn");
const overlay = document.querySelector(".overlay");
const deleteWindow = document.querySelector(".delete_window");

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

// When clicking the delete button
deleteBtn.addEventListener("click", deleteWindowOn);

// Closing the popup window
const noBtn = document.querySelector(".no_btn");
const closeBtn = document.querySelector(".close_btn");

overlay.addEventListener("click", deleteWindowOff);
noBtn.addEventListener("click", deleteWindowOff);
closeBtn.addEventListener("click", deleteWindowOff);
