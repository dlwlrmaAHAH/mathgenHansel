# mathgenerator

A math problem generator, created for the purpose of giving self-studying students and teaching organizations the means to easily get access to random math problems to suit their needs.

To try out generators, go to <https://todarith.ml/generate/>

If you have an idea for a generator, please add it as an issue and tag it with the "New Generator" label.

## Usage

The project can be install via pip

```bash
pip install mathgenerator
```

Here is an example of how you would generate an addition problem:

```python
from mathgenerator import mathgen

#generate an addition problem
problem, solution = mathgen.addition()

#another way to generate an addition problem using genById()
problem, solution = mathgen.genById(0)
```

## List of Generators

| Id   | Skill                             | Example problem    | Example Solution      | Function Name            |
|------|-----------------------------------|--------------------|-----------------------|--------------------------|
[//]: # list start
| 0 | Addition | 39+50= | 89 | addition |
| 1 | Subtraction | 91-37= | 54 | subtraction |
| 2 | Multiplication | 39*1= | 39 | multiplication |
| 3 | Division | 67/85= | 0.788235294117647 | division |
| 4 | Binary Complement 1s | 1101100101= | 0010011010 | binary_complement_1s |
| 5 | Modulo Division | 72%26= | 20 | modulo_division |
| 6 | Square Root | sqrt(16)= | 4 | square_root |
| 7 | Power Rule Differentiation | 4x^1 | 4x^0 | power_rule_differentiation |
| 8 | Square | 20^2= | 400 | square |
| 9 | LCM (Least Common Multiple) | LCM of 5 and 2 = | 10 | lcm |
| 10 | GCD (Greatest Common Denominator) | GCD of 17 and 20 =  | 1 | gcd |
| 11 | Basic Algebra | 10x + 8 = 8 | 0 | basic_algebra |
| 12 | Logarithm | log2(64) | 6 | log |
| 13 | Easy Division | 147/7 =  | 21 | int_division |
| 14 | Decimal to Binary | Binary of 4= | 100 | decimal_to_binary |
| 15 | Binary to Decimal | 010111110 | 190 | binary_to_decimal |
| 16 | Fraction Division | (2/10)/(8/4) | 1/10 | divide_fractions |
| 17 | Integer Multiplication with 2x2 Matrix | 9 * [[6, 1], [1, 3]] =  | [[54,9],[9,27]] | multiply_int_to_22_matrix |
| 18 | Area of Triangle | Area of triangle with side lengths: 19 17 10 =  | 84.71127433818948 | area_of_triangle |
| 19 | Triangle exists check | Does triangle with sides 29, 13 and 3 exist? | No | valid_triangle |
| 20 | Midpoint of the two point | (10,-14),(-4,-1)= | (3.0,-7.5) | midpoint_of_two_points |
| 21 | Factoring Quadratic | x^2-18x+81 | (x-9)(x-9) | factoring |
| 22 | Third Angle of Triangle | Third angle of triangle with angles 68 and 78 =  | 34 | third_angle_of_triangle |
| 23 | Solve a System of Equations in R^2 | -4x - 10y = 24, -4x - 3y = -4 | x = 4, y = -4 | system_of_equations |
| 24 | Distance between 2 points | Find the distance between (8, 5) and (13, 9) | sqrt(41) | distance_two_points |
| 25 | Pythagorean Theorem | The hypotenuse of a right triangle given the other two lengths 12 and 2 =  | 12.17 | pythagorean_theorem |
| 26 | Linear Equations | 19x + -13y = -450, 10x + 10y = 100 | x = -10, y = 20 | linear_equations |
| 27 | Prime Factorisation | Find prime factors of 59 | [59] | prime_factors |
| 28 | Fraction Multiplication | (6/1)*(3/10) | 9/5 | fraction_multiplication |
| 29 | Angle of a Regular Polygon | Find the angle of a regular polygon with 16 sides | 157.5 | angle_regular_polygon |
| 30 | Combinations of Objects | Number of combinations from 18 objects picked 6 at a time  | 18564 | combinations |
| 31 | Factorial | 3! =  | 6 | factorial |
| 32 | Surface Area of Cube | Surface area of cube with side = 19m is | 2166 m^2 | surface_area_cube |
| 33 | Surface Area of Cuboid | Surface area of cuboid with sides = 5m, 1m, 6m is | 82 m^2 | surface_area_cuboid |
| 34 | Surface Area of Cylinder | Surface area of cylinder with height = 15m and radius = 17m is | 3418 m^2 | surface_area_cylinder |
| 35 | Volum of Cube | Volume of cube with side = 10m is | 1000 m^3 | volume_cube |
| 36 | Volume of Cuboid | Volume of cuboid with sides = 10m, 16m, 1m is | 160 m^3 | volume_cuboid |
| 37 | Volume of cylinder | Volume of cylinder with height = 34m and radius = 16m is | 27344 m^3 | volume_cylinder |
| 38 | Surface Area of cone | Surface area of cone with height = 15m and radius = 2m is | 107 m^2 | surface_area_cone |
| 39 | Volume of cone | Volume of cone with height = 19m and radius = 9m is | 1611 m^3 | volume_cone |
| 40 | Common Factors | Common Factors of 56 and 69 =  | [1] | common_factors |
| 41 | Intersection of Two Lines | Find the point of intersection of the two lines: y = -2x - 10 and y = -8/5x - 5 | (-25/2, 15) | intersection_of_two_lines |
| 42 | Permutations | Number of Permutations from 17 objects picked 4 at a time =   | 57120 | permutation |
| 43 | Cross Product of 2 Vectors | [-16, 6, -14] X [-17, -6, -5] =  | [-114, 158, 198] | vector_cross |
| 44 | Compare Fractions | Which symbol represents the comparison between 1/10 and 8/7? | < | compare_fractions |
| 45 | Simple Interest | Simple interest for a principle amount of 8073 dollars, 8% rate of interest and for a time period of 3 years is =  | 1937.52 | simple_interest |
| 46 | Multiplication of two matrices | Multiply<table><tr><td>-1</td><td>-7</td></tr><tr><td>-7</td><td>2</td></tr><tr><td>-8</td><td>2</td></tr><tr><td>-8</td><td>2</td></tr></table>and<table><tr><td>9</td><td>-4</td><td>3</td></tr><tr><td>-9</td><td>-8</td><td>-1</td></tr></table> | <table><tr><td>54</td><td>60</td><td>4</td></tr><tr><td>-81</td><td>12</td><td>-23</td></tr><tr><td>-90</td><td>16</td><td>-26</td></tr><tr><td>-90</td><td>16</td><td>-26</td></tr></table> | matrix_multiplication |
| 47 | Cube Root | cuberoot of 440 upto 2 decimal places is: | 7.61 | cube_root |
| 48 | Power Rule Integration | 8x^5 + 1x^9 + 9x^9 + 5x^6 + 7x^7 | (8/5)x^6 + (1/9)x^10 + (9/9)x^10 + (5/6)x^7 + (7/7)x^8 + c | power_rule_integration |
| 49 | Fourth Angle of Quadrilateral | Fourth angle of quadrilateral with angles 11 , 199, 1 = | 149 | fourth_angle_of_quadrilateral |
| 50 | Quadratic Equation | Zeros of the Quadratic Equation 95x^2+190x+55=0 | [-0.35, -1.65] | quadratic_equation |
| 51 | HCF (Highest Common Factor) | HCF of 5 and 13 =  | 1 | hcf |
| 52 | Probability of a certain sum appearing on faces of dice | If 2 dice are rolled at the same time, the probability of getting a sum of 12 = | 1/36 | dice_sum_probability |
| 53 | Exponentiation | 20^6 = | 64000000 | exponentiation |
| 54 | Confidence interval For sample S | The confidence interval for sample [232, 260, 277, 253, 223, 287, 243, 240, 218, 271, 237, 276, 258, 250, 246, 226, 239, 295, 235, 247, 213, 210, 207, 236, 261, 211, 205, 284, 256, 299, 228, 267, 293, 200, 215] with 99% confidence is | (257.6870590779175, 233.6272266363682) | confidence_interval |
| 55 | Comparing surds | Fill in the blanks 75^(1/8) _ 68^(1/1) | < | surds_comparison |
| 56 | Fibonacci Series | The Fibonacci Series of the first 19 numbers is ? | [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584] | fibonacci_series |
| 57 | Trigonometric Values | What is tan(30)? | 1/√3 | basic_trigonometry |
| 58 | Sum of Angles of Polygon | Sum of angles of polygon with 8 sides =  | 1080 | sum_of_polygon_angles |
| 59 | Mean,Standard Deviation,Variance | Find the mean,standard deviation and variance for the data[48, 33, 41, 29, 9, 50, 43, 11, 16, 21, 23, 35, 45, 35, 19] | The Mean is 30.533333333333335 , Standard Deviation is 169.5822222222222, Variance is 13.022373908862479 | data_summary |
| 60 | Surface Area of Sphere | Surface area of Sphere with radius = 2m is | 50.26548245743669 m^2 | surface_area_sphere |
| 61 | Volume of Sphere | Volume of sphere with radius 76 m =  | 1838778.3689363108 m^3 | volume_sphere |
| 62 | nth Fibonacci number | What is the 27th Fibonacci number? | 196418 | nth_fibonacci_number |
| 63 | Profit or Loss Percent | Loss percent when CP = 459 and SP = 294 is:  | 35.947712418300654 | profit_loss_percent |
| 64 | Binary to Hexidecimal | 110 | 0x6 | binary_to_hex |
| 65 | Multiplication of 2 complex numbers | (20-11j) * (3+19j) =  | (269+347j) | multiply_complex_numbers |
| 66 | Geometric Progression | For the given GP [4, 40, 400, 4000, 40000, 400000] ,Find the value of a,common ratio,9th term value, sum upto 11th term | The value of a is 4, common ratio is 10 , 9th term is 400000000 , sum upto 11th term is 44444444444.0 | geometric_progression |
| 67 | Geometric Mean of N Numbers | Geometric mean of 2 numbers 65 and 22 =  | (65*22)^(1/2) = 37.815340802378074 | geometric_mean |
| 68 | Harmonic Mean of N Numbers | Harmonic mean of 4 numbers 9 , 8 , 47 , 73 =  |  4/((1/9) + (1/8) + (1/47) + (1/73)) = 14.75544671255992 | harmonic_mean |
| 69 | Euclidian norm or L2 norm of a vector | Euclidian norm or L2 norm of the vector[820.7491392802318, 209.6794919301974, 225.59292753758044, 537.8783420147682, 40.14693897510357, 648.8940804515304, 277.0690883822212, 741.9271329359917, 807.1036732602864, 608.7427632578269, 625.6879783489085, 834.4512357524056, 423.2785583193275, 709.5606560098445, 493.29922694432196, 903.1151397634669, 605.6380116528376] is: | 2515.129484208976 | euclidian_norm |
| 70 | Angle between 2 vectors | angle between the vectors [559.07, 674.48, 425.75, 871.89, 260.89, 31.64, 377.38, 818.43, 787.57, 616.13, 636.31, 369.24, 340.6, 670.85, 840.37, 865.02, 481.69, 803.47] and [93.25, 398.41, 530.05, 68.46, 241.04, 539.93, 983.85, 872.27, 426.31, 231.65, 657.98, 928.56, 347.83, 329.71, 693.94, 916.86, 144.78, 199.82] is: | 0.67 radians | angle_btw_vectors |
| 71 | Absolute difference between two numbers | Absolute difference between numbers -26 and 18 =  | 44 | absolute_difference |
| 72 | Dot Product of 2 Vectors | [19, -13, -8] . [6, 13, -19] =  | 97 | vector_dot |
| 73 | Binary 2's Complement | 2's complement of 100 = | 100 | binary_2s_complement |
| 74 | Inverse of a Matrix | Inverse of Matrix Matrix([[36, 69, 83], [67, 9, 47], [4, 79, 11]]) is: | Matrix([[-139/10321, 223/10321, 96/10321], [-549/268346, 32/134173, 3869/268346], [5257/268346, -1284/134173, -4299/268346]]) | invert_matrix |
| 75 | Area of a Sector | Given radius, 10 and angle, 349. Find the area of the sector. | Area of sector = 304.55995 | sector_area |
| 76 | Mean and Median | Given the series of numbers [3, 58, 55, 75, 53, 28, 68, 48, 42, 38]. find the arithmatic mean and mdian of the series | Arithmetic mean of the series is 46.8 and Arithmetic median of this series is 50.5 | mean_median |
| 77 | Determinant to 2x2 Matrix | Det([[72, 10], [43, 23]]) =  |  1226 | int_matrix_22_determinant |
| 78 | Compound Interest | Compound interest for a principle amount of 2783 dollars, 5% rate of interest and for a time period of 1 year is =  | 2922.15 | compound_interest |
| 79 | Decimal to Hexadecimal | Binary of 762= | 0x2fa | decimal_to_hexadeci |
| 80 | Percentage of a number | What is 70% of 55? | Required percentage = 38.50% | percentage |
| 81 | Celsius To Fahrenheit | Convert 67 degrees Celsius to degrees Fahrenheit = | 152.60000000000002 | celsius_to_fahrenheit |
| 82 | AP Term Calculation | Find the term number 79 of the AP series: -79, -103, -127 ...  | -1951 | arithmetic_progression_term |
| 83 | AP Sum Calculation | Find the sum of first 79 terms of the AP series: 10, 39, 68 ...  | 90139.0 | arithmetic_progression_sum |
| 84 | Converts decimal to octal | The decimal number 2575 in Octal is:  | 0o5017 | decimal_to_octal |
| 85 | Converts decimal to Roman Numerals | The number 1746 in Roman Numerals is:  | MDCCXLVI | decimal_to_roman_numerals |
| 86 | Degrees to Radians | Angle 92 in radians is =  | 1.61 | degree_to_rad |
| 87 | Radians to Degrees | Angle 3 in degrees is =  | 171.89 | radian_to_deg |
| 88 | Differentiation | differentiate w.r.t x : d(sin(x)+8*x^(-2))/dx | cos(x) - 16/x^3 | differentiation |
| 89 | Definite Integral of Quadratic Equation | The definite integral within limits 0 to 1 of the equation 45x^2 + 27x + 1 is =  | 29.5 | definite_integral |
| 90 | isprime | 67 | True | is_prime |
| 91 | Binary Coded Decimal to Integer | Integer of Binary Coded Decimal 9 is =  | 37382 | bcd_to_decimal |
| 92 | Complex To Polar Form | rexp(itheta) =  | 13.89exp(i-1.04) | complex_to_polar |
| 93 | Union,Intersection,Difference of Two Sets | Given the two sets a={3, 4, 5, 7, 9} ,b={10, 3, 6}.Find the Union,intersection,a-b,b-a and symmetric difference | Union is {3, 4, 5, 6, 7, 9, 10},Intersection is {3}, a-b is {9, 4, 5, 7},b-a is {10, 6}, Symmetric difference is {4, 5, 6, 7, 9, 10} | set_operation |
| 94 | Base Conversion | Convert 6322 from base 16 to base 4. | 12030202 | base_conversion |
| 95 | Curved surface area of a cylinder | What is the curved surface area of a cylinder of radius, 6 and height, 31? | CSA of cylinder = 1168.67 | curved_surface_area_cylinder |
| 96 | Perimeter of Polygons | The perimeter of a 3 sided polygon with lengths of [82, 14, 110]cm is:  | 206 | perimeter_of_polygons |
| 97 | Power of Powers | The 5^9^1 = 5^(9*1) = 5^9 | 1953125 | power_of_powers |
| 98 | Quotient of Powers with Same Base | The Quotient of 23^9 and 23^6 = 23^(9-6) = 23^3 | 12167 | quotient_of_power_same_base |
| 99 | Quotient of Powers with Same Power | The Quotient of 22^3 and 27^3 = (22/27)^3 = 0.8148148148148148^3 | 0.540974444952497 | quotient_of_power_same_power |
| 100 | complex Quadratic Equation | Find the roots of given Quadratic Equation 5x^2 + 8x + 2 = 0 | simplified solution : ((-0.31, -1.29)), generalized solution : ((-8 + sqrt(24))/2*5, (-8 - sqrt(24))/2*5) | complex_quadratic |
| 101 | Leap Year or Not | Year 2088  | is a leap year | is_leap_year |
| 102 | Minute to Hour conversion | Convert 262 minutes to Hours & Minutes | 4 hours and 22 minutes | minutes_to_hours |
| 103 | Decimal to Binary Coded Decimal | BCD of Decimal Number 3356 is =  | 13112 | decimal_to_bcd |
| 104 | Circumference | Circumference of circle with radius 32 | 201.06192982974676 | circumference |
| 105 | Combine Like terms | 8x^2 | 8x^2  | combine_like_terms |
| 106 | signum function | signum of -285 is = | -1 | signum_function |
| 107 | Conditional Probability | Someone tested positive for a nasty disease which only 0.30% of population have. Test sensitivity (true positive) is equal to SN= 94.82% whereas test specificity (true negative) SP= 96.80%. What is the probability that this guy really has that disease? | 8.19% | conditional_probability |
| 108 | Arc length of Angle | Given radius, 40 and angle, 184. Find the arc length of the angle. | Arc length of the angle = 128.45623 | arc_length |
| 109 | Binomial distribution | A manufacturer of metal pistons finds that, on average, 34.81% of the pistons they manufacture are rejected because they are incorrectly sized. What is the probability that a batch of 18 pistons will contain no more than 3 rejected pistons? | 8.07 | binomial_distribution |
| 110 | Stationary Points | f(x)=2*x^3 + 4*x^2 + x + 1 | (-2/3 - sqrt(10)/6,2*(-2/3 - sqrt(10)/6)**3 - sqrt(10)/6 + 1/3 + 4*(-2/3 - sqrt(10)/6)**2),(-2/3 + sqrt(10)/6,2*(-2/3 + sqrt(10)/6)**3 + 4*(-2/3 + sqrt(10)/6)**2 + 1/3 + sqrt(10)/6) | stationary_points |
| 111 | Expanding Factored Binomial | (-8x-1)(-4x+6) | 32*x^2-44*x-6 | expanding |
| 112 | Area of Circle | Area of circle with radius 48 | 7241.142857142857 | area_of_circle |
