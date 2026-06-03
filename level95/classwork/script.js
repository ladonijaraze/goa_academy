const p = document.getElementById("par")
const p2 = document.getElementById("par2")
const p3 = document.getElementById("par3")
const p4 = document.getElementById("par4")
const but =document.getElementById("but")
const but2 =document.getElementById("but2")
const but3 =document.getElementById("but3")
const but4 =document.getElementById("but4")


but.addEventListener("click",function(){
p.textContent="gelabarkalaia"
}
)


but2.addEventListener("dblclick", function () {
    p2.style.background = "green";
})

but3.addEventListener("mouseover", function () {
    p3.style.width = "1e00px";
})

but4.addEventListener("mouseout",function(){
p4.textContent=""
}
)


