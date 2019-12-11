//Joseph Lee & Emory Walsh
//SoftDev1 pd1
//K28 -- Sequential Progression II: Electric Boogaloo
//2019-12-12


var fact = function(n){
    if (n < 2) return 1;
    return (n * (fact(n - 1)));
};

var fib = function(n){
    if (n == 0){
        return 0;
    }
    else if (n == 1){
        return 1;
    }
    else{
        return fib(n-1) + fib(n-2);
    }
}

var gcd = function (a,b){
    if (b > a) return gcd(b, a);
    if (a % b == 0) return b;
    return gcd(b, a % b);
}

var randStudent = function (list){
	return list[Math.floor(Math.random()*list.length)];
}

//////////////////////////////////////////////////////////////////

  var factorialDOM = document.getElementById("fact");
  //console.log("here");
  if(factorialDOM){
    console.log("Hi");
    factorialDOM.addEventListener('click', function(){
    var num = fact(5);
    console.log(num);
  });
};



var fibDOM = document.getElementById("fib");
if(fibDOM){
  console.log("hola");
  fibDOM.addEventListener('click', function(){
    var result = fib(5);
    console.log(result);
  });
};



var gcdDOM = document.getElementById("gcd");
if(gcdDOM){
  console.log("hola");
  gdcDOM.addEventListener('click', function(){
    var result = gdc(12, 9);
    console.log(result);
  });
};



var randStudentDOM = document.getElementById("randStudent");
if(randStudentDOM){
  console.log("hola");
  randStudentDOM.addEventListener('click', function(){
    var result = randStudent();
    console.log(result);
  });
};
