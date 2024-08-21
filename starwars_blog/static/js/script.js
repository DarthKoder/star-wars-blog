document.addEventListener('DOMContentLoaded', function() {
  let sidenav = document.querySelectorAll('.sidenav');
  M.Sidenav.init(elems, options);
});

// Initialize collapsible (uncomment the lines below if you use the dropdown variation)
// var collapsibleElem = document.querySelector('.collapsible');
// var collapsibleInstance = M.Collapsible.init(collapsibleElem, options);

// Or with jQuery

$(document).ready(function(){
  $('.sidenav').sidenav();
});

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