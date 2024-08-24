// Sidenav script
document.addEventListener('DOMContentLoaded', function() {
  let sidenav = document.querySelectorAll('.sidenav');
  M.Sidenav.init(elems, options);
});

// Or with jQuery

$(document).ready(function(){
  $('.sidenav').sidenav();
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