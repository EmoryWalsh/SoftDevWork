//Emory Walsh
//Softdev pd09
//K07 -- They lock us in the tower whenever we get caught
//2020-02-13

var canvas = document.getElementById("playground");
var ctx = canvas.getContext("2d");

var id = null;
var radius = 2;
var direction = "out"; //out or in
var anim = "off" //on or off

document.getElementById("go").addEventListener("click", () => {
  if(anim === "off"){
    circle();
    anim = "on";
  }
});

function circle(){
  ctx.clearRect(0,0,600,600)
  if(radius === 250){
    direction = "in";
  }
  if(radius === 0){
    direction = "out";
  }
  if(direction === "out"){
    radius += 2;
  }
  else if(direction === "in"){
    radius -= 2;
  }
  //console.log(radius)
  ctx.fillStyle = "blue";
  ctx.beginPath();
  ctx.arc(300, 300, radius, 0, 2 * Math.PI);
  ctx.fill();
  if(id != 0){
  id = window.requestAnimationFrame(circle);
  }
};

document.getElementById("stop").addEventListener("click", () => {
  window.cancelAnimationFrame(id);
  anim = "off";
  id = null;
});
