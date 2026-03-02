let price = [250,645,300,900,50];
arr = []
for(let i of price){
    arr.push(i-(i/10));
}
console.log(arr);