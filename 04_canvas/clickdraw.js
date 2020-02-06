//Emory Walsh
//Softdev pd09
//K04 -- I See a Red Door...
//2020-02-05

var canvas = document.getElementById("slate");
var ctx = canvas.getContext("2d");

//mode either "rect" or "dot"
var curmode = "dot";

canvas.addEventListener("click", (e) => {
    //console.log("mode: " + curmode);
    pgx = e.pageX;
    pgy = e.pageY;
    cx = pgx - canvas.offsetLeft;
    cy = pgy - canvas.offsetTop;
    if(curmode === "dot"){
      ctx.fillStyle = "blue";
      ctx.beginPath();
      ctx.arc(cx, cy, 10, 0, 2 * Math.PI);
      ctx.stroke();
      ctx.fill();
    }
    else{
      ctx.fillStyle = "pink";
      ctx.fillRect(cx, cy, 10, 40);
    }
});

document.getElementById("clear").addEventListener("click", () => {
  //console.log("clear");
  ctx.fillStyle = "white";
  ctx.fillRect(0,0,canvas.width,canvas.height);
});

document.getElementById("mode").addEventListener("click", () => {
  if(curmode === "rect"){
    curmode = "dot";
    //console.log("dot");
  }
  else{

    curmode = "rect";
    //console.log("rect2");
  }
});
