function minInput(input, min) {
    if (input.value < min) {
        input.value = min;
    }
}

function maxInput(input, max) {
    if (input.value > max) {
        input.value = max;
    }
}

function minMaxInput(input, min, max) {
    if (input.value > max) {
        input.value = max;
    }
    if (input.value < min) {
        input.value = min;
    }
}