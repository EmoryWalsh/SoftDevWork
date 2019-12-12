
//Removes item from list when clicked
var removeItem = function(e){

};

//List element and their events
var lis = document.getElementsByTagName("li");

for(var i=0; i<lis.length; i++){
  lis[i].addEventListener('click', removeItem);
};

//Adds item "WORD" to the list
var addItem = function(e){
  var list = document.getElementById("thelist");
  var item = document.createElement("li");
  var value = "WORD"
  item.innerHTML = value;
  list.appendChild(item);
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

//Shows event fields in console
button.addEventListener('click', function(e){
  console.log(e);
});
