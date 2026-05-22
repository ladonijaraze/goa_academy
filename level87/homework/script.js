
function applyToArray(arr, fn) {
    let result = [];

    for (let i = 0; i < arr.length; i++) {
        result.push(fn(arr[i]));
    }

    return result;
}

function findFirst(arr, fn) {
    for (let i = 0; i < arr.length; i++) {
        if (fn(arr[i])) {
            return arr[i];
        }
    }

    return undefined;
}

function all(arr, fn) {
    for (let i = 0; i < arr.length; i++) {
        if (!fn(arr[i])) {
            return false;
        }
    }

    return true;
}