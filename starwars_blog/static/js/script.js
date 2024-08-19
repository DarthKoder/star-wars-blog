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
  let modal = document.querySelectorAll('.modal');
  M.Modal.init(elems, options);
});

// Or with jQuery

$(document).ready(function(){
  $('.modal').modal();
})
