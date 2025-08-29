document.addEventListener("DOMContentLoaded", function() {
    flatpickr(".flatpickr", {
        dateFormat: "Y-m-d",
        altInput: true,
        altFormat: "F j, Y",
        allowInput: true,
        monthSelectorType: 'dropdown',
        yearSelectorType: 'dropdown'
    });
});
