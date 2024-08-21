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

// Remember me script
document.addEventListener("DOMContentLoaded", function() {
  // Check if there's a username stored in localStorage
  let savedUsername = localStorage.getItem('savedUsername');
  if (savedUsername) {
      document.getElementById('login').value = savedUsername;
      document.getElementById('remember-me').checked = true;
  }
});

document.querySelector('form').addEventListener('submit', function() {
  if (document.getElementById('remember-me').checked) {
      let username = document.getElementById('login').value;
      localStorage.setItem('savedUsername', username);
  } else {
      localStorage.removeItem('savedUsername');
  }
});