document.addEventListener('DOMContentLoaded', function() {
    var datepicker = document.querySelectorAll('.datepicker');
    M.Datepicker.init(datepicker);
  });

  // Or with jQuery

  $(document).ready(function(){
    $('.datepicker').datepicker();
  });