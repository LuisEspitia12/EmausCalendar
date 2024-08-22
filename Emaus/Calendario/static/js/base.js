

document.addEventListener('DOMContentLoaded', function() {
    const navToggle = document.querySelector('.nav-toggle');
    const nav = document.querySelector('.nav');
  
    navToggle.addEventListener('click', function() {
      nav.classList.toggle('nav-visible');
    });
  });
  
  $(document).ready(function() {
    // Inicializar el datepicker con el idioma español
    $('.datepicker').datepicker({
        language: 'es',
        format: 'yyyy-mm-dd',  // Asegúrate de que el formato de fecha sea el correcto
    });
});