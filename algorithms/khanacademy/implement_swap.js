var swap = function(array, firstIndex, secondIndex) {
	var aa = array[firstIndex];
	array[firstIndex] = array[secondIndex];
	array[secondIndex] = aa;
};

var testArray = [7, 9, 4];
swap(testArray, 0, 1);

println(testArray);

Program.assertEqual(testArray, [9, 7, 4]);

swap(testArray, 0, 2);
println(testArray);
Program.assertEqual(testArray, [4, 7, 9]);

swap(testArray, 1, 2);
println(testArray);
Program.assertEqual(testArray, [4, 9, 7]);