from django.shortcuts import render


# Create your views here.
def index(request):
    view_data = {
        'page_title': 'Dashboard',
        'page_header': 'Dashboard'
    }
    return render(request, 'regular_expense/index.html', view_data)