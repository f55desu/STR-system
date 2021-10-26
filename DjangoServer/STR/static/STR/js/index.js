$(document).ready(function() {
  const panel = $('.form-panel.two');

   $('.psevdobtn').on('click', function(e) {
     e.preventDefault();
    panel.toggleClass("visible");
     
   });
 
   $('.form-toggle').on('click', function(e) {
     e.preventDefault();
     panel.toggleClass("visible");
   });
 });