

let r = 0;
let g = 0;
let b = 0;    

let color_name = document.getElementById("color_name");

let color_box = document.getElementById("color_box");


let form = document.getElementById("color_pick");


form.addEventListener("submit", (e) => {
    e.preventDefault();
})


function grabGreenColor() {
    let green_input = document.getElementById("color_stats_g");

    green_input.addEventListener("input", (e) => {
        g = e.target.value;
        console.log("red amount: " + g);
        changeColorBox(r,g,b); 
    })
};


function grabRedColor() {
    let red_input = document.getElementById("color_stats_r");

    red_input.addEventListener("input", (e) => {
        r = e.target.value;
        console.log("red amount: " + r);
        changeColorBox(r,g,b); 
    })
};


function grabBlueColor() {
    let blue_input = document.getElementById("color_stats_b");

    blue_input.addEventListener("input", (e) => {
        b = e.target.value;
        console.log("blue amount: " + b); 
        changeColorBox(r,g,b);
    })
};

function changeColorBox(r,g,b) {

    if (color_box) {
        color_box.style.backgroundColor = (`rgb(${r},${g},${b})`);
    }
}




grabGreenColor();
grabRedColor();
grabBlueColor();

