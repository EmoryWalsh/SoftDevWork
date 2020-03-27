//Emory Walsh
//Softdev pd09
//K06 -- Dot Dot Dot
//2020-02-12

var canvas = document.getElementById("playground");

//mode either "rect" or "dot"
var curmode = "dot";

lx = null
ly = null



document.getElementById("clear").addEventListener("click", () => {
  //Emory Walsh
  //Softdev pd09
  //K06 -- Dot Dot Dot
  //2020-02-12

  var svg = document.getElementById("vimage");

  //mode either "rect" or "dot"
  var curmode = "dot";

  lx = null
  ly = null

  svg.addEventListener("click", (e) => {
      console.log("here");
  });

  document.getElementById("clear").addEventListener("click", () => {
    while (svg.lastChild) {
      svg.removeChild(svg.lastChild);
    }
  });
});
