from django.http import HttpResponse

def Fibonacci(n):
 
    # Check if input is 0 then it will
    # print incorrect input
    print(n)
    if n < 0:
        print("Incorrect input")
 
    # Check if n is 0
    # then it will return 0
    elif n == 0:
        return 0
 
    # Check if n is 1,2
    # it will return 1
    elif n == 1 or n == 2:
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)
 
 
# Driver Program


def index(request, value):    
    return HttpResponse(Fibonacci(value))

def index2(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def index3(request):
    a = [1] * (10 ** 6)
    b = [2] * (2 * 10 ** 7)
    del b
    return a