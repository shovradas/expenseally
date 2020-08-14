from django.shortcuts import render, HttpResponse


# Create your views here.
def index(request):
    view_data = {
        'page_title': 'Dashboard',
        'page_header': 'Your Dashboard'
    }
    return render(request, 'regular_expense/index.html', view_data)


def add_expense(request):
    view_data = {
        'page_title': 'Add Expense',
        'page_header': 'Expense | Add New'
    }
    return render(request, 'regular_expense/add-expense.html', view_data)


def manage_expense(request):
    view_data = {
        'page_title': 'Manage Expense',
        'page_header': 'Expense | Manage'
    }
    return render(request, 'regular_expense/manage-expense.html', view_data)


def expense_settings(request):
    view_data = {
        'page_title': 'Expense Settings',
        'page_header': 'Expense | Settings'
    }
    return render(request, 'regular_expense/expense-settings.html', view_data)


# def about(request):
#     developedBy = "Shovra, Rumi, Jahangir"
#
#     html = '<!DOCTYPE html>'
#     html += '<html>'
#     html += '<body>'
#     html += 'About ExpenseAlly'
#     html += '<br/>Developed by: '
#     html += developedBy
#     html += '<body>'
#     html += '</body>'
#     html += '</html>'
#     return HttpResponse(html)

# def about(request):
#     model = {
#         "developed_by": "Shovra, Rumi, Jahangir"
#     }
#     return render(request, 'about.html', model)
