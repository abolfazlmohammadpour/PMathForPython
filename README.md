## PMath(ProfessionalMathematics), Version 0.1

### What Is PMath?
#### PMath Is An Open Source Professional Library Of Matehmatics For Python.
---
### How To Use?
#### For Using PMath In Your Project, First You Have To Clone PMath Repo In Your Project
`git clone https://github.com/ABOLFAZLMOHAMMADPOUR/PMathForPython.git`

`git clone https://gitlab.com/ABOLFAZLMOHAMMADPOUR/PMathForPython.git`
#### And Then You Have To Import PMath In Main File Of Your Project.
```
Project
└─ Source
   └─ PMath.py
   └─ main.py
```
main.py
```py
import PMath
```
#### Now You Can Use PMath In Your Project And Enjoying It.
---
### Working With PMath
#### PMath Is Contains Lots Of Functions Which You Can Doing Mathematics Operations With Them In Your Project.
---
### Calculating Divisors Of A Number With PMath
main.py
```py
import PMath

print(PMath.Calculating_Divisors(27))
print(PMath.Calculating_Divisors(-43))
```
Output
```
(1, 3, 9, 27)
(1, 43)
```
---
### Calculating Multiples Of A Number With PMath
main.py
```py
import PMath

print(PMath.Calculating_Multiples(27, From=1, To=5))
print(PMath.Calculating_Multiples(-43, 1, 8))
```
Output
```
(27, 54, 81, 108, 135)
(-43, -86, -129, -172, -215, -258, -301, -344)
```
---
### Calculating GCD(Greatest Common Divisor) Of A List Of Numbers
main.py
```py
import PMath

print(PMath.Calculating_GCD([-33, 39, 69]))
```
Output
```
3
```
---
### Calculating LCM(Least Common Multiple) Of A List Of Numbers From ... To ...
main.py
```py
import PMath

print(PMath.Calculating_LCM(1, 100, [33, 39, 69]))
print(PMath.Calculating_LCM(1, 1000, [33, 39, 69]))
```
Output
```
None
9867
```
---