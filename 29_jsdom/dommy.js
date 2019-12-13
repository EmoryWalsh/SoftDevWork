//Emory Walsh & Emily Zhang
//SoftDev1 pd1
//K29 -- Sequential Progression III: Season of the Witch
//2019-12-12

//Changes heading
var changeHeading = function(e, str){
  //console.log(e);
  var h = document.getElementById("h");
  h.innerHTML = e.target.innerHTML;
}

var changeHeadingBack = function(e){
  var h = document.getElementById("h");
  h.innerHTML = "Hello World!";
}

//Removes item from list when clicked
var removeItem = function(e, node){
  var el = e.target.remove();
  lis = document.getElementsByTagName("li");
  console.log(lis);
};

//List element and their events
var lis = document.getElementsByTagName("li");

for(var i=0; i<lis.length; i++){
  console.log(i);
  lis[i].addEventListener('mouseover', changeHeading);
  lis[i].addEventListener('mouseout', changeHeadingBack);
  lis[i].addEventListener('click', removeItem);
};

//Adds item "WORD" to the list
var addItem = function(e){
  var list = document.getElementById("thelist");
  var item = document.createElement("li");
  var value = "WORD"
  item.innerHTML = value;
  list.appendChild(item);
  item.addEventListener('mouseover', changeHeading);
  item.addEventListener('mouseout', changeHeadingBack);
  item.addEventListener('click', removeItem);
  lis = document.getElementsByTagName("li");
  console.log(lis);
};

var button = document.getElementById("b");
button.addEventListener('click', addItem)

//Fib function
var fib = function(n){
  if(n < 2){
    return 1;
  }
  else{
    return fib(n-1) + fib(n-2);
  }
};

var addFib = function(e){
  console.log(e);
  //???
}

var addFib2 = function(e){
  console.log(e);
  //???
}

var fb = document.getElementById("fb");
fb.addEventListener('click', addFib);


//Shows event fields in console
button.addEventListener('click', function(e){
  //console.log(e);
});
