# view.py

from django.http import HttpResponse
from django.shortcuts import render, resolve_url


def index(request):
    return render(request, 'index.html')


def analyze(request):
    # print(request.GET.get('text', 'default1'))
    # here we are taking the input from user using the checkbox if that check box is clicked we will see in the terminal as on and the input user given. If check box is not enabled we will see will the default value,
    text_to_analyze = request.GET.get('text', 'off')
    # Please keep in mind that here the first parameter that is "text" is the name from the html page from which we are taking the input from the user
    removepun = request.GET.get('removepunc', 'off')
    capitalize = request.GET.get('capitalize', 'off')
    newline = request.GET.get('newline', 'off')
    space = request.GET.get('space', 'off')
    char_count = request.GET.get('char_count', 'off')
    result=""
    if removepun == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        result = ""
        print(text_to_analyze)
        for i in text_to_analyze:
            if i not in punctuations:
                result = result + i
        print(result)
        text_to_analyze=result
        dict = {"purpose": "Removed puncuation", "after": result}
        # return render(request, "analyze.html", dict)
    if capitalize == "on":
        result = text_to_analyze.upper()
        dict = {"purpose": "Captilzed", "after": result}
        # return render(request, "analyze.html", dict)
    if (newline == "on"):
        for i in text_to_analyze:
            if i != "\n":
                result = result + i
        text_to_analyze=result
        dict = {"purpose": "New line removed", "after": result}
        # return render(request, "analyze.html", dict)
    if (space == "on"):
        for i,char in enumerate(text_to_analyze):
            if not(text_to_analyze[i] == " " and text_to_analyze[i+1]==" "):
            # i dont know why the above one is working and below one is giving the string index out of range
            # if (text_to_analyze[i]!=" ") and (text_to_analyze[i+1] !=" "):
                result = result + char
        text_to_analyze=result
        dict = {"purpose": "After removal of the space", "after": result}
        # return render(request, "analyze.html", dict)
    if (char_count == "on"):
        for i,char in enumerate(text_to_analyze):
            pass
        text_to_analyze=result
        dict = {"purpose": "Number of the charecter", "after": i+1}
    return render(request, "analyze.html", dict)


def ex11(request):
    s = '''<a href="https://facebook.com/" target="main">FaceBook</a>
    <a href="https://Google.com/" target="main">Google</a>
    <a href="https://Amazon.com/" target="main">Amazon</a>
    <a href="https://safiqmahammad.com/" target="main">My website</a>
    '''
    return HttpResponse(s)
