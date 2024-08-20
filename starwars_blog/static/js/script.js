// datepicker script
document.addEventListener('DOMContentLoaded', function() {
    let datepicker = document.querySelectorAll('.datepicker');
    M.Datepicker.init(datepicker);
  });

  // Or with jQuery

  $(document).ready(function(){
    $('.datepicker').datepicker();
  });

// Modal script
document.addEventListener('DOMContentLoaded', function() {
  let modals = document.querySelectorAll('.modal');
  M.Modal.init(modals);
});

// Or with jQuery
$(document).ready(function(){
  $('.modal').modal();
});

// Function to open a specific modal by its ID
function openModal(modalId) {
  let instance = M.Modal.getInstance(document.getElementById(modalId));
  instance.open();
}