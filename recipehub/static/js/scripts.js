// scripts.js

// Define navbarShrink globally
var navbarShrink = function () {
    const navbarCollapsible = document.body.querySelector('#mainNav');
    if (!navbarCollapsible) {
        return;
    }
    if (window.scrollY === 0) {
        navbarCollapsible.classList.remove('navbar-shrink');
    } else {
        navbarCollapsible.classList.add('navbar-shrink');
    }
};

$(document).ready(function () {
    // Initialize Bootstrap Select
    $('.selectpicker').selectpicker();

    // Handle change event on the select element
    $('#required_tools').on('changed.bs.select', function (e, clickedIndex, isSelected, previousValue) {
        // Get the selected options
        var selectedOptions = $(this).val();

        // Update the list of selected tools
        var selectedToolsList = $('#selectedToolsList');
        selectedToolsList.empty(); // Clear the list

        // Populate the list with selected tools
        if (selectedOptions) {
            selectedOptions.forEach(function (option, index) {
                var toolName = $('#required_tools option[value="' + option + '"]').text();
                selectedToolsList.append('<span>' + toolName + (index < selectedOptions.length - 1 ? ', ' : '') + '</span>');
            });
        }
    });

    // Automatically show the modal on page load if there are flash messages
    var messagesModal = $('#flashMessagesModal');
    if (messagesModal.find('ul li').length > 0) {
        messagesModal.modal('show');
    }
    // Hide the modal after 1 second
    setTimeout(function () {
        messagesModal.modal('hide');
    }, 1000);

    // Update the navbar on scroll
    $(window).on('scroll', function () {
        navbarShrink();
    });
});

window.addEventListener('DOMContentLoaded', event => {
    // Shrink the navbar on page load
    navbarShrink();
});
