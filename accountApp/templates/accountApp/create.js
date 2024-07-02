$(document).ready(function () {
  $(".main img").on("click", function () {
    $("input").toggleClass("active");
    if ($("input").hasClass("active")) {
      $(this)
        .attr("class", "./images/눈뜬아이콘.png")
        .prev("input")
        .attr("type", "text");
    } else {
      $(this)
        .attr("class", "./images/눈감은아이콘.png")
        .prev("input")
        .attr("type", "password");
    }
  });
});
