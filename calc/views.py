from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'base.htm')


def calc(request):
    try:
        c = ""
        n1 = ""
        n2 = ""
        if request.method == "POST":
            n1 = eval(request.POST.get("num1"))
            n2 = eval(request.POST.get("num2"))
            operation = request.POST.get("operation")

            if operation == "Addition":
                c = n1 + n2
            
            elif operation == "Subtraction":
                c = n1 - n2
            
            elif operation == "Multiplication":
                c = n1 * n2

            elif operation == "Division":
                c = n1 / n2

    except:
        print(f"INVALID INPUT")

    d = {
        "result" : c ,
        "n1" : n1,
        "n2" : n2,
    }

    print(c)
    return render(request, 'index.htm', d)
