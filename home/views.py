from django.shortcuts import render

# Create your views here.
def index(request):
    project_name = "What to Cook ?!"
    project_code = "w2c"
    page_title = "Titre de page"
    page_subtitle = ""

    context_dict = {
        "project_name":project_name,
        "project_code":project_code,
        "page_title":page_title,
        "page_subtitle":page_subtitle,
        }
    
    #import pudb; pu.db()

    return render(request, 'index.html',context=context_dict)
    