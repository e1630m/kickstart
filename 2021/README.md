# Table of Contents
| Year | Round |  #  | Problem | Solution | Runtime* |
| :--: | :---: | :-: | :-----: | :------: | :------: |
| [2021](https://codingcompetitions.withgoogle.com/kickstart/archive/2021) |      [A](https://codingcompetitions.withgoogle.com/kickstart/round/0000000000436140)      |      [1](https://codingcompetitions.withgoogle.com/kickstart/round/0000000000436140/000000000068cca3)      | [K-Goodness String (5pts, 7pts)](./2021/README.md#k-goodness-string-5pts-7pts)               | [py](./2021/ra1.py)                                                   | 2ms      \| 86ms                                                                                          |
| [2021](https://codingcompetitions.withgoogle.com/kickstart/archive/2021) |      [A](https://codingcompetitions.withgoogle.com/kickstart/round/0000000000436140)      |      [2](https://codingcompetitions.withgoogle.com/kickstart/round/0000000000436140/000000000068c509)      | [L Shaped Plots (8pts, 12pts)](./2021/README.md#l-shaped-plots-8pts-12pts)                   | [py](./2021/ra2.py)                                                   | 225ms    \| 10,053ms                                                                                      |
| [2021](https://codingcompetitions.withgoogle.com/kickstart/archive/2021) |      [A](https://codingcompetitions.withgoogle.com/kickstart/round/0000000000436140)      |      [3](https://codingcompetitions.withgoogle.com/kickstart/round/0000000000436140/000000000068cb14)      | [Rabbit House (9pts, 15pts)](./2021/README.md#rabbit-house-9pts-15pts)                       | [py](./2021/ra3.py)                                                   | 145ms    \| 6,439ms                                                                                       |
| [2021](https://codingcompetitions.withgoogle.com/kickstart/archive/2021) |      [A](https://codingcompetitions.withgoogle.com/kickstart/round/0000000000436140)      |      [4](https://codingcompetitions.withgoogle.com/kickstart/round/0000000000436140/000000000068c2c3)      | [Checksum (10pts, 17pts, 17pts)](./2021/README.md#checksum-10pts-17pts-17pts)                | [py](./2021/ra4.py)                                                   | 8ms      \| 85ms    \| 8,681ms                                                                            |
| [2021](https://codingcompetitions.withgoogle.com/kickstart/archive/2021) |      [G](https://codingcompetitions.withgoogle.com/kickstart/round/00000000004362d6)      |      [1](https://codingcompetitions.withgoogle.com/kickstart/round/00000000004362d6/00000000008b3771)      | [Dogs and Cats (5pts, 6pts)](./2021/README.md#dogs-and-cats-5pts-6pts)                       | [py](./2021/rg1.py)                                                   | 62ms     \| 47ms                                                                                          |


Every runtime data is based on the python3 solution, and it is measured by the testing modules available in this repo (starts with `test_`) on the following environment (average of 3 runs).
* Python 3.10.0, Apple M1, macOS 12.0 Beta 8 (21A5534d)

# Round A
## K-Goodness String (5pts, 7pts)
### Problem
Charles defines the goodness score of a string as the number of indices i such that Si≠SN−i+1 where 1≤i≤N/2 (1-indexed). For example, the string CABABC has a goodness score of 2 since S2≠S5 and S3≠S4.

Charles gave Ada a string S of length N, consisting of uppercase letters and asked her to convert it into a string with a goodness score of K. In one operation, Ada can change any character in the string to any uppercase letter. Could you help Ada find the minimum number of operations required to transform the given string into a string with goodness score equal to K?

### Input
* The first line of the input gives the number of test cases, T. T test cases follow.
* The first line of each test case contains two integers N and K. The second line of each test case contains a string S of length N, consisting of uppercase letters.

### Output
* For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is the minimum number of operations required to transform the given string S into a string with goodness score equal to K.

### Limits
* Memory limit: 1 GB.
* 1≤T≤100.
* 0≤K≤N/2.
#### Test Set 1
* Time limit: 20 seconds.
* 1≤N≤100.
#### Test Set 2
* Time limit: 40 seconds.
* 1≤N≤2×105 for at most 10 test cases.
* For the remaining cases, 1≤N≤100.

### Sample
#### Sample Input
```
2
5 1
ABCAA
4 2
ABAA
```
#### Sample Output
```
Case #1: 0
Case #2: 1
```

* In Sample Case #1, the given string already has a goodness score of 1. Therefore the minimum number of operations required is 0.
* In Sample Case #2, one option is to change the character at index 1 to B in order to have a goodness score of 2. Therefore, the minimum number of operations required is 1.

## L Shaped Plots (8pts, 12pts)
### Problem
Given a grid of `R` rows and `C` columns each cell in the grid is either 0 or 1.

A segment is a nonempty sequence of consecutive cells such that all cells are in the same row or the same column. We define the length of a segment as number of cells in the sequence.

A segment is called "good" if all the cells in the segment contain only 1s.

An "L-shape" is defined as an unordered pair of segments, which has all the following properties:

* Each of the segments must be a "good" segment.
* The two segments must be perpendicular to each other.
* The segments must share one cell that is an endpoint of both segments.
* Segments must have length at least 2.
* The length of the longer segment is twice the length of the shorter segment.

We need to count the number of L-shapes in the grid.

Below you can find two examples of correct L-shapes,

<p align="center"><img src="https://codejam.googleapis.com/dashboard/get_file/AQj_6U1WsahNThgYYtiGIsNwzSCjHVJWsHC6X_ingMAqSrQGYgfbVuL0LVBATISPEtJMRcB--32orWnGB_o38g/examples_correct.png"></p>

and three examples of **invalid** L-shapes.

<p align="center"><img src="https://codejam.googleapis.com/dashboard/get_file/AQj_6U2uIrTynEAgxTEUyFr7fXYtrQsMVCBgF3JvvNjteUmCzkLv9kKcp0jGtvdyJxUXG8N3_NZ6pDlWXetE4C6K/examples_incorrect.png"></p>

Note that in the shape on the left, two segments do not share a common endpoint. The next two shapes do not meet the last requirement, as in the middle shape both segments have the same length, and in the last shape the longer segment is longer than twice the length of the shorter one.

### Input
* The first line of the input contains the number of test cases, T. T test cases follow.
* The first line of each testcase contains two integers R and C.
* Then, R lines follow, each line with C integers representing the cells of the grid.

### Output
* For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is the number of L-shapes.

### Limits
* Time limit: 60 seconds.
* Memory limit: 1 GB.
* 1≤T≤100.
* Grid consists of 0s and 1s only.
#### Test Set 1
* 1≤R≤40.
* 1≤C≤40.
#### Test Set 2
* 1≤R≤1000 and 1≤C≤1000 for at most 5 test cases.
* For the remaining cases, 1≤R≤40 and 1≤C≤40.

### Sample
#### Sample Input
```
2
4 3
1 0 0
1 0 1
1 0 0
1 1 0
6 4
1 0 0 0
1 0 0 1
1 1 1 1
1 0 1 0
1 0 1 0
1 1 1 0
```
#### Sampe Output
```
Case #1: 1
Case #2: 9
```

* In Sample Case #1, there is one L-shape.
  * The first one is formed by using cells: (1,1), (2,1), (3,1), (4,1), (4,2)
<p align="center"><img src="https://codejam.googleapis.com/dashboard/get_file/AQj_6U02RuuoHmgmAvG0ZBiqjEBwJYXaz0T0xEagTAd5cOoedtB-pfxZ399i3flXxnk04O0w1g/sample1.png"></p>

* In Sample Case #2, there are nine L-shapes.
  * The first one is formed by using cells: (1,1), (2,1), (3,1), (4,1), (5,1), (6,1), (6,2), (6,3)
  * The second one is formed by using cells: (3,1), (4,1), (5,1), (6,1), (6,2)
  * The third one is formed by using cells: (6,1), (5,1), (4,1), (3,1), (3,2)
  * The fourth one is formed by using cells: (3,3), (4,3), (5,3), (6,3), (6,2)
  * The fifth one is formed by using cells: (6,3), (5,3), (4,3), (3,3), (3,2)
  * The sixth one is formed by using cells: (3,1), (3,2), (3,3), (3,4), (2,4)
  * The seventh one is formed by using cells: (3,4), (3,3), (3,2), (3,1), (2,1)
  * The eighth one is formed by using cells: (3,4), (3,3), (3,2), (3,1), (4,1)
  * The ninth one is formed by using cells: (6,3), (5,3), (4,3), (3,3), (3,4)
  * The first three L-shapes are shown on the picture below.

<p align="center"><img src="https://codejam.googleapis.com/dashboard/get_file/AQj_6U1W7GSavANlJvX8yZ6WD8w0vImYNHTW3ggnwzh7DOx3MSc7yexHsNidAtCt9CFyqWt3zQ/sample2.png"></p>

## Rabbit House (9pts, 15pts)
### Problem
Barbara got really good grades in school last year, so her parents decided to gift her with a pet rabbit. She was so excited that she built a house for the rabbit, which can be seen as a 2D grid with R rows and C columns.

Rabbits love to jump, so Barbara stacked several boxes on several cells of the grid. Each box is a cube with equal dimensions, which match exactly the dimensions of a cell of the grid.

However, Barbara soon realizes that it may be dangerous for the rabbit to make jumps of height greater than 1 box, so she decides to avoid that by making some adjustments to the house. For every pair of adjacent cells, Barbara would like that their absolute difference in height be at most 1 box. Two cells are considered adjacent if they share a common side.

As all the boxes are superglued, Barbara cannot remove any boxes that are there initially, however she can add boxes on top of them. She can add as many boxes as she wants, to as many cells as she wants (which may be zero). Help hew determine what is the minimum total number of boxes to be added so that the rabbit's house is safe.

### Input
* The first line of the input gives the number of test cases, T. T test cases follow.
* Each test case begins with a line containing two integers R and C.
* Then, R lines follow, each with C integers. The j-th integer on i-th line, Gi,j, represents how many boxes are there initially on the cell located at the i-th row and j-th column of the grid.

### Output
* For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is the minimum number of boxes to be added so that the rabbit's house is safe.

### Limits
* Memory limit: 1 GB.
* 1≤T≤100.
* 0≤Gi,j≤2⋅106, for all i, j.
#### Test Set 1
* Time limit: 20 seconds.
* 1≤R,C≤50.
#### Test Set 2
* Time limit: 40 seconds.
* 1≤R,C≤300.

### Sample
#### Sample Input
```
3
1 3
3 4 3
1 3
3 0 0
3 3
0 0 0
0 2 0
0 0 0
```
#### Sample Output
```
Case #1: 0
Case #2: 3
Case #3: 4
```

* In Sample Case #1, the absolute difference in height for every pair of adjacent cells is already at most 1 box, so there is no need to add any extra boxes.
* In Sample Case #2, the absolute difference in height of the left-most cell and the middle cell is 3 boxes. To fix that, we can add 2 boxes to the middle cell. But then, the absolute difference of the middle cell and the right-most cell will be 2 boxes, so Barbara can fix that by adding 1 box to the right-most cell. After adding these 3 boxes, the safety condition is satisfied.
* In Sample Case #3, the cell in the middle of the grid has an absolute difference in height of 2 boxes with all of its four adjacent cells. One solution is to add exactly 1 box to all of the middle's adjacent cells, so that the absolute difference between any pair of adjacent cells will be at most 1 box. That requires 4 boxes in total.

## Checksum (10pts, 17pts, 17pts)
### Problem
Grace and Edsger are constructing a N×N boolean matrix A. The element in i-th row and j-th column is represented by Ai,j. They decide to note down the checksum (defined as bitwise XOR of given list of elements) along each row and column. Checksum of i-th row is represented as Ri. Checksum of j-th column is represented as Cj.

For example, if <img src="https://render.githubusercontent.com/render/math?math=\color{white}N = {2},\ A = \begin{bmatrix}1 %26 1\\0 %26 1\end{bmatrix}">, then <img src="https://render.githubusercontent.com/render/math?math=\color{white}R = \begin{bmatrix}1 %26 0\end{bmatrix}"> and <img src="https://render.githubusercontent.com/render/math?math=\color{white}C = \begin{bmatrix}0 %26 1\end{bmatrix}">


Once they finished the matrix, Edsger stores the matrix in his computer. However, due to a virus, some of the elements in matrix A are replaced with −1 in Edsger's computer. Luckily, Edsger still remembers the checksum values. He would like to restore the matrix, and reaches out to Grace for help. After some investigation, it will take Bi,j hours for Grace to recover the original value of Ai,j from the disk. Given the final matrix A, cost matrix B, and checksums along each row (R) and column (C), can you help Grace decide on the minimum total number of hours needed in order to restore the original matrix A?

### Input
* The first line of the input gives the number of test cases, T. T test cases follow.
* The first line of each test case contains a single integer N.
* The next N lines each contain N integers representing the matrix A. j-th element on the i-th line represents Ai,j.
* The next N lines each contain N integers representing the matrix B. j-th element on the i-th line represents Bi,j.
* The next line contains N integers representing the checksum of the rows. i-th element represents Ri.
* The next line contains N integers representing the checksum of the columns. j-th element represents Cj.

### Output
* For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is the minimum number of hours to restore matrix A.

### Limits
* Memory limit: 1 GB.
* 1≤T≤100.
* −1≤Ai,j≤1, for all i,j.
* 1≤Bi,j≤1000, for i,j where Ai,j=−1, otherwise Bi,j=0.
* 0≤Ri≤1, for all i.
* 0≤Cj≤1, for all j.
* It is guaranteed that there exist at least one way to replace −1 in A with 0 or 1 such that R and C as satisfied.
#### Test Set 1
* Time limit: 20 seconds.
* 1≤N≤4.
#### Test Set 2
* Time limit: 35 seconds.
* 1≤N≤40.
#### Test Set 3
* Time limit: 35 seconds.
* 1≤N≤500.

### Sample
#### Sample Input
```
3
3
1 -1 0
0 1 0
1 1 1
0 1 0
0 0 0
0 0 0
1 1 1
0 0 1
2
-1 -1
-1 -1
1 10
100 1000
1 0
0 1
3
-1 -1 -1
-1 -1 -1
0 0 0
1 1 3
5 1 4
0 0 0
0 0 0
0 0 0
```
#### Sample Output
```
Case #1: 0
Case #2: 1
Case #3: 2
```

* In Sample Case #1, A1,2 can be restored using the checksum of either 1-st row or 2-nd column. Hence, Grace can restore the matrix without spending any time to recover the data.
* In Sample Case #2, Grace spends one hour to recover A1,1. After that, she can use checksums of 1-st row and 1-st column to restore A1,2 and A2,1 respectively. And then she can use checksum of 2-nd row to restore A2,2. Hence, Grace can restore the matrix by spending one hour.
* In Sample Case #3, Grace can spend one hour to recover A1,1 and another hour to recover A2,2. After that, she can use checksum to restore the rest of the matrix. Hence, Grace can restore the matrix by spending two hours in total.


# Round G
## Dogs and Cats (5pts, 6pts)

### Problem
You work for an animal shelter and you are responsible for feeding the animals. You already prepared D portions of dog food and C portions of cat food.

There are a total of N animals waiting in a line, some of which are dogs and others are cats. It might be possible that all the animals in the line are dogs or all the animals are cats. A string S of N characters C and D represents the order of cats and dogs in the line. The i-th character is equal to C if the i-th animal in the line is a cat. Similarly, the i-th character is equal to D if the i-th animal in the line is a dog.

The animals are fed in the order they stay in the line. Each dog eats exactly 1 portion of dog food and similarly each cat eats exactly 1 portion of cat food. Moreover, you have extra portions of cat food. Every time a dog eats food, you bring M extra portions of cat food for cats.

Animals have to be fed in the order they wait in line and an animal can only eat if the animal before it has already eaten. That means that if you run out of dog (or cat) food portions and a dog (or a cat) is about to get fed, the line will not move, as all the animals will wait patiently.

You need to determine if in this scenario all the dogs in the line will be fed. Note that this means that some cats might remain in the line, but worry not, you will eventually feed them later!

### Input
* The first line of the input gives the number of test cases, T. T test cases follow.
* The first line of each test case contains four integers N, D, C, and M: the number of animals, the initial number of dog food portions, the initial number of cat food portions, and the additional portions of cat food that we add after a dog eats a portion of dog food, respectively.
* The next line contains a string S of length N representing the arrangement of animals.

### Output
* For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is YES if all the dogs will be fed and NO otherwise.

### Limits
* Memory limit: 1 GB.
* 1≤T≤100.
* 1≤N≤104.
* 0≤D,C≤106.
* S consists of only characters C and D.
#### Test Set 1
* Time limit: 20 seconds.
* M=0
#### Test Set 2
* Time limit: 40 seconds.
* 0≤M≤106.

### Sample
Note: there are additional samples that are not run on submissions down below.
#### Sample Input
```
3
6 10 4 0
CCDCDD
4 1 2 0
CCCC
4 2 1 0
DCCD
```
#### Sample Output
```
Case #1: YES
Case #2: YES
Case #3: NO
```
* In Sample Case #1, there are 10 portions of dog food and 4 portions of cat food.
  1. The first two animals are cats, so after they eat, 2 portions of cat food remain.
  2. Then a dog eats one portion of dog food. Now, there are 9 portions of dog food left.
  3. Next, a cat eats a portion of cat food, reducing the number of portions of cat food to 1.
  4. The last two animals are dogs and they each eat one portion of dog food.
  * So in this case, all the dogs are able to eat.
* In Sample Case #2, there are no dogs. Hence, all (zero) dogs will be able to eat trivially.
* In Sample Case #3, the cat before the second dog will not be able to eat because there will not be enough portions of cat food. Hence, the second dog will also not eat.

### Additional Sample - Test Set 2
*The following additional sample fits the limits of Test Set 2. It will not be run against your submitted solutions.*
### Sample Input
```
2
12 4 2 2
CDCCCDCCDCDC
8 2 1 3
DCCCCCDC
```
#### Sample Output
```
Case #1: YES
Case #2: NO
```
* In Sample Case #1, 2 portions of cat food appear whenever a dog eats a portion of dog food.
  1. After the first cat eats, there is 1 portion of cat food left.
  2. Then a dog eats, leaving 3 portions of dog food and 3 portions of cat food.
  3. After the next 3 cats eat, there are 3 portions of dog food and 0 portions of cat food remaining.
  4. Then a dog eats, leaving 2 portions of dog food and 2 portions of cat food.
  5. After the next 2 cats eat food, there are 2 portions of dog food and 0 portions of cat food left.
  6. Now a dog eats, leaving 1 portion of dog food and 2 portions of cat food.
  7. Next a cat eats, leaving 1 portion of dog food and 1 portion of cat food.
  8. The last dog eats the remaining portion of dog food.
  * So in this case, all the dogs are able to eat.
* In Sample Case #2, the cat before the second dog will not be able to eat because there will not be enough portions of cat food.
