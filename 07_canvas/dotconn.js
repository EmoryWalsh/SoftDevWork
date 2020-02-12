//Emory Walsh
//Softdev pd09
//K07 -- expansion & contraction
//2020-02-13

var canvas = document.getElementById("playground");
var ctx = canvas.getContext("2d");

var id = null
var radius = 10
var action = null

document.getElementById("go").addEventListener("click", () => {
  id = window.requestAnimationFrame(circle());
  radius++;
  console.log(radius)
});

function circle(){
  ctx.fillStyle = "blue";
  ctx.beginPath();
  ctx.arc(300, 300, radius, 0, 2 * Math.PI);
  ctx.fill();
};

document.getElementById("stop").addEventListener("click", () => {
  window.cancelAnimationFrame(id);
});
