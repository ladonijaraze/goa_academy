const changeToBlue = () => document.body.style.backgroundColor = "lightblue";
document.getElementById("btn1").addEventListener("click", changeToBlue);

document.getElementById("btn2").addEventListener("click", () => {
  document.body.style.backgroundColor = "lightgreen";
});

const changeColor = (color) => () => document.body.style.backgroundColor = color;
document.getElementById("btn3").addEventListener("click", changeColor("lightcoral"));
