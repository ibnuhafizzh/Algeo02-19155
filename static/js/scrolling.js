$(window).scroll(function(){
  var scroll = $(window).scrollTop();

  console.log(scroll);

  if(scroll >= 300){
    $("#nav").addClass("bg-dark");
    $("#search").removeClass("hidden");

  }else{
    $("#nav").removeClass("bg-dark");
    $("#search").addClass("hidden");
  }
});
