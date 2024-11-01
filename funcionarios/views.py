from django.shortcuts import render

def funcionario(request):
    return render (request, 'funcionarios/base_templates/base.html')