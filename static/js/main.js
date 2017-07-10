function timer(a, b){
    var v = a;
    if (v.slice(-4,-1) == 'a.m'){
      if (v.slice(-10,-9) == '1'){
        v = v.slice(0,-12) + ' '+ v.slice(-10,-5) + ':00' ;
      }
      else{
        v = v.slice(0,-11) + ' ' + v.slice(-9,-5) + ':00' ;
      }
    }
    else{
      if (v.slice(-10,-9) == '1'){
        v = v.slice(0,-12) + ' '+ (Number(v.slice(-10,-8))+12 )+v.slice(-8,-5) + ':00' ;
      }
      else{
        v = v.slice(0,-12) + ' '+ (Number(v.slice(-9,-8))+12 )+v.slice(-8,-5) + ':00' ;
      }
    }




    // Set the date we're counting down to
    var countDownDate = new Date(v).getTime();

    // Update the count down every 1 second
    var x = setInterval(function() {

      // Get todays date and time
      var now = new Date().getTime();

      // Find the distance between now an the count down date
      var distance = countDownDate - now;

      // Time calculations for days, hours, minutes and seconds
      var days = Math.floor(distance / (1000 * 60 * 60 * 24));
      var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
      var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
      var seconds = Math.floor((distance % (1000 * 60)) / 1000);

      // Display the result in the element with id="demo"
      document.getElementById(b).innerHTML = days + "d " + hours + "h "
      + minutes + "m " + seconds + "s ";

      // If the count down is finished, write some text
      if (distance < 0) {
        clearInterval(x);
        document.getElementById(b).innerHTML = "EXPIRED";
      }
    }, 1000);
/*
    var countDownDate = new Date(v).getTime();
    var x = setInterval(function(){
      var now = new Date().getTime();
      var distance = countDownDate - now;
      var days = Math.floor(distance / (1000 * 60 * 60 * 24));
      var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
      var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
      var seconds = Math.floor((distance % (1000 * 60)) / 1000);
      document.getElementById("demo").innerHTML = days + "d " + hours + "h "
      + minutes + "m " + seconds + "s ";
      if (distance < 0) {
        clearInterval(x);
        document.getElementById("demo").innerHTML;
      }
    }, 1000);*/
}

function test(){
  alert("Good");
}

function toCelsius(fahrenheit) {

  alert(fahrenheit);
  return fahrenheit
}
