$(".rating__input").starRating({
    initialRating: 3.5,
    disableAfterRate: false,
    onHover: function(currentIndex, currentRating, $el){
      $('.rating__label').text(currentIndex);
    },
    onLeave: function(currentIndex, currentRating, $el){
      $('.rating__label').text(currentRating);
    }
  });

  function total(){
   var total=0;
   $("input:enabled").each(function(){
      total=total+$(this).val();
   });
   return total;
}