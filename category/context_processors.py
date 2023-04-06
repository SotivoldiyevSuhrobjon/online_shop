from .models import Category

def menu_category_list(request):
    category = Category.objects.all()
    print(dict(category=category))
    return dict(category=category)