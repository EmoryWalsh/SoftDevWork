//Emory Walsh & Sophie Nichol
//Softdev pd09
//K12 -- Connect The Dots
//2020-03-30

var svg = document.getElementById("vimage");

svg.addEventListener("click", (e) => {
  x = e.pageX-5;
  y = e.pageY-20;

  console.log(x)
  console.log(y)

  let children = svg.children
  for(let i=0; i<children.length; i++){
    if(Math.abs(x - children[i].getAttribute("cx")) < 20 && Math.abs(y - children[i].getAttribute("cy")) < 20){
      if(children[i].getAttribute("style") === "fill: blue; stroke: blue; stroke-width: 1px;"){
        children[i].setAttribute("style", "fill: #00FFFF; stroke: #00FFFF; stroke-width: 1px;");
        return
      }
      else{
        nx = Math.random() * 500 + 5
        ny = Math.random() * 500 + 20
        children[i].setAttribute("cx", nx)
        children[i].setAttribute("cy", ny)
        children[i].setAttribute('style', 'fill: blue; stroke: blue; stroke-width: 1px;' );
        return
      }
    }
  }
  var circle = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
  circle.setAttributeNS(null, 'cx', x);
  circle.setAttributeNS(null, 'cy', y);
  circle.setAttributeNS(null, 'r', 20);
  circle.setAttributeNS(null, 'style', 'fill: blue; stroke: blue; stroke-width: 1px;' );
  svg.appendChild(circle);


});

document.getElementById("clear").addEventListener("click", () => {
  while (svg.lastChild) {
    svg.removeChild(svg.lastChild);
    children = 0;
  }
});

document.getElementById("xtra").addEventListener("click", () => {
  colors = ["#1AFA72", "#F70C0C", "#DB0CF7", "#F7F70C", "#0F0CF7", "#0CF7BE"]

  for(let i=0; i < 100; i++){
    nx = Math.random() * 500 + 5
    ny = Math.random() * 500 + 20
    nr = Math.random() * 20

    var circle = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
    circle.setAttributeNS(null, 'cx', nx);
    circle.setAttributeNS(null, 'cy', ny);
    circle.setAttributeNS(null, 'r', nr);
    circle.setAttributeNS(null, 'style', 'fill:' + colors[i%6] + '; stroke:' + colors[i%6] + '; stroke-width: 1px;' );
    svg.appendChild(circle);
  }
});
