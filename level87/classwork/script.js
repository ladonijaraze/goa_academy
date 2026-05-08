function Num(num) {
    if (num % 2 === 0) {
        console.log("luwia brat");
    } else {
        console.log("araa brat");
    }
}

lado=(Num) 




function listMap(list, func) {
    let result = [];

    for (let i = 0; i < list.length; i++) {
        func(list[i]);
    }

}

listMap([13,14,67,8,99],lado)