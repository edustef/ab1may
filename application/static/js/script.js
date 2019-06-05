
/*
document.querySelector("#showless").addEventListener("click", showLess);

function showLess() {
  if (document.querySelector("#showless").innerHTML == "Mai mult"){
    document.getElementById("showless").innerHTML = "Mai putin";
  }
  else {
    document.querySelector("#showless").innerHTML = "Mai mult";
  }
}
*/
$(document).ready(function(){
  // Add smooth scrolling to all links
  $("a").on('click', function(event) {
    // Make sure this.hash has a value before overriding default behavior
    let this_address = this.href.replace(this.hash,'');
    let link_address = window.location.href.replace(window.location.hash,'');
    if (this.hash !== "" && this_address == link_address) {
      // Prevent default anchor click behavior
      event.preventDefault();

      // Store hash
      var hash = this.hash;

      // Using jQuery's animate() method to add smooth page scroll
      // The optional number (800) specifies the number of milliseconds it takes to scroll to the specified area
      $('html, body').animate({
        scrollTop: $(hash).offset().top
      }, 800, function(){
        // Add hash (#) to URL when done scrolling (default click behavior)
        window.location.hash = hash;
      });
    } // End if
  });
});
