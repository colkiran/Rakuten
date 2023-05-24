from django.shortcuts import render

# Create your views here.

def setcookie(request):
    response = render(request, "setcookie.html")
    response.set_cookie('prdname', 'adidas')
    return response

def getcookie(request):
    prdname = request.COOKIES['prdname']
    return render(request, 'getcookie.html', {'pname':prdname})

def delcookie(request):
    response = render(request, 'deletecookie.html')
    response.delete_cookie('prdname')
    return response

