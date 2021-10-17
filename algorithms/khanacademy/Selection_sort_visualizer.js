var displayArray = function(array, iter) {
    textFont(createFont("monospace"), 12);
    fill(0, 0, 0);
    for (var j=0; j<array.length; j++) {
        text(array[j].toString(), j * 30 + 50, iter * 30 + 50);
    }
};

var createLine = function(array, iter, i , minIndex) {
    textFont(createFont("monospace"), 12);
    fill(0, 0, 0);
    line(i * 30 + 52,iter * 30 + 40, minIndex * 30 + 52, (iter-1) * 30 + 52);
};


var swap = function(array, firstIndex, secondIndex) {
    var temp = array[firstIndex];
    array[firstIndex] = array[secondIndex];
    array[secondIndex] = temp;
};

var indexOfMinimum = function(array, startIndex) {

    var minValue = array[startIndex];
    var minIndex = startIndex;

    for(var i = minIndex + 1; i < array.length; i++) {
        if(array[i] < minValue) {
            minIndex = i;
            minValue = array[i];
        }
    } 
    return minIndex;
}; 

var selectionSort = function(array) {
    
    var minIndex;
    
    displayArray(array, 0);
    for(var i = 0; i < array.length - 1; i++) {
        minIndex = indexOfMinimum(array, i);
        swap(array,i,minIndex);
        displayArray(array, i+1);
        createLine(array, i+1, i, minIndex);
    }
};

//var array = [22, 11,99,88,9];
//selectionSort(array);

//var array2 = [5,4,3,2,1];
//selectionSort(array2);

//var array3 = [1, 5,5,88,4];
//selectionSort(array3);

var array3 = [1, 5,5,88,4 ,32, 21,32,41];
selectionSort(array3);