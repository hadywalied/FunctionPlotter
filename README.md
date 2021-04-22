![Function Plotter](https://github.com/hadywalied/FunctionPlotter/blob/master/logo.png)

# **Function Plotter**

The app is a demonstration of the power of sympy of parsing the string text into math functions, and plotting them by using matplotlib and pyside2.

## Requirements

`pyside2~=5.15.2`
`matplotlib~=3.4.1`
`numpy~=1.20.2`
`sympy~=1.8`
`pytest-qt`
`pytest~=6.2.3`

## Instructions 

run the app by: 

`python main.py`

run the test by using the test suite in PyCharm or by simply running 

`pytest -v`

## Screenshots

**the main interface:**

![image-20210422232128955](https://github.com/hadywalied/FunctionPlotter/blob/master/Screenshots/image-20210422232128955.png)

### Plotting

$$
f(x) = sin(x)
$$

**from x = -10 to x = 10** :

![image-20210422232513752](https://github.com/hadywalied/FunctionPlotter/blob/master/Screenshots/image-20210422232513752.png)

trying an wrong equation will result in an error, which is demonstrated below.

### Plotting f(x) = xz

![image-20210422232822455](https://github.com/hadywalied/FunctionPlotter/blob/master/Screenshots/image-20210422232822455.png)

sure we must leave a hint for the user to correct the Error

![image-20210422232852232](https://github.com/hadywalied/FunctionPlotter/blob/master/Screenshots/image-20210422232852232.png)