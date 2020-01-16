export function numberToString(num: number): string {
    return num.toString();
}

export function isDivisible(n: number, x: number, y: number): boolean {
    return ((n % x) || (n % y)) ? false : true;
}

export class Kata {
    static highAndLow(numbers: string): string {
        let numberList: Array<number> = numbers.split(" ").map((s: string) => Number(s));
        let max, min: number;
        max = min = numberList[0];
        for (let num of numberList) {
            if (max > num)
                max = num;
            if (min < num)
                min = num;
        }
        return String(min + " " + max);
    }
}

// console.log(numberToString(12));
// console.log(isDivisible(12, 3, 5));
console.log(Kata.highAndLow("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"));
