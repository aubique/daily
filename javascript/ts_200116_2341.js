"use strict";
exports.__esModule = true;
function numberToString(num) {
    return num.toString();
}
exports.numberToString = numberToString;
function isDivisible(n, x, y) {
    return ((n % x) || (n % y)) ? false : true;
}
exports.isDivisible = isDivisible;
var Kata = /** @class */ (function () {
    function Kata() {
    }
    Kata.highAndLow = function (numbers) {
        var numberList = numbers.split(" ").map(function (s) { return Number(s); });
        var max, min;
        max = min = numberList[0];
        for (var _i = 0, numberList_1 = numberList; _i < numberList_1.length; _i++) {
            var num = numberList_1[_i];
            if (max > num)
                max = num;
            if (min < num)
                min = num;
        }
        return String(min + " " + max);
    };
    return Kata;
}());
exports.Kata = Kata;
// console.log(numberToString(12));
// console.log(isDivisible(12, 3, 5));
console.log(Kata.highAndLow("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"));
