# git init
# git list
# git git config --global user.name "wilson perez"
# git config --global user.email "wilpec2017@gmail.com"
# git config --global --unset-all user.email "wilpec2045@gmail.com"
#  git config --lits
import os
os.system("cls")

def suma (a,b):
    c = a + b
    print ("La suma de a + b es. ",c)
def resta (a,b):
    c = a - b
    print ("La resta de a - b es. ",c)
def multi (a,b):
    c = a * b
    print ("La multiplicación de a * b es. ",c)
def division (a,b):
    if b ==0:
        print(" la división no se puede realizar")
    else:
        c = a/b
        print ("La division de a / b es. ",c)

suma(2,4)
resta(2,4)
multi(2,4)
division(2,0)
#   >>>>>>>>>>>>>> calculadora>>>>>>>>>>>>>>>>>>

