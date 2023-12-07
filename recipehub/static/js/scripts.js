// scripts.js

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
});

window.addEventListener('DOMContentLoaded', event => {
    // Navbar shrink function
    var navbarShrink = function () {
        const navbarCollapsible = document.body.querySelector('#mainNav');
        if (!navbarCollapsible) {
            return;
        }
        if (window.scrollY === 0) {
            navbarCollapsible.classList.remove('navbar-shrink')
        } else {
            navbarCollapsible.classList.add('navbar-shrink')
        }
    };

    // Shrink the navbar 
    navbarShrink();
});
