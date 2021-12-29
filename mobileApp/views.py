from django.db.models import Q
from django.shortcuts import render, redirect
from django.views import generic
from django.http import JsonResponse
from django.contrib import messages
# Create your views here.
from mobileApp.models import Mobile


def home(request):
    return render(request, 'home.html')


def add_mobile(request):
    brand_name = request.POST.get("brand_name")
    model = request.POST.get("model")
    jan_code = request.POST.get("jan_code")
    color = request.POST.get("color")

    jan_code_exist = Mobile.objects.filter(jan_code=jan_code).exists()
    if jan_code_exist:
        messages.error(
            request,
            "This code is already exist. Please provide unique JAN Code",
        )
        return render(request, 'home.html')
    else:
        mobile_ins = Mobile(brand_name=brand_name, model=model, jan_code=jan_code, color=color)
        mobile_ins.save()
        return render(request, 'home.html')


def mobile_list(request):
    d = request.POST.get("search_text")
    print(d)

    mobile_list = Mobile.objects.all()
    context = {
        "mobile_list": mobile_list
    }
    return render(request, 'mobile-list.html', context)


def delete_mobile(request, id):
    mobile_list = Mobile.objects.all()
    context = {
        "mobile_list": mobile_list
    }

    mobile_inst = Mobile.objects.filter(id=id).first()
    if mobile_inst is not None:
        mobile_inst.delete()

        return redirect('mobile-list')
    return render(request, 'mobile-list.html', context)


def delete_mobiles(request, *args, **kwargs):
    if request.method == "POST":
        print("delete multiple mobiles...")
        mobile_ids = request.POST.getlist('id[]')
        for id in mobile_ids:
            mobile = Mobile.objects.get(pk=id)
            mobile.delete()
        return redirect('mobile-list')

    # return render(request, 'mobile-list.html', context)


def search_mobile_list(request):
    print("search hitting: ")
    search_text = request.POST.get("series")
    print(search_text)
    mobile = Mobile.objects.filter(Q(model__contains=search_text) | Q(jan_code__contains=search_text)).values()
    print("mobile: ", list(mobile))

    context = {
        "mobile_list": mobile
    }


    return JsonResponse(data=list(mobile), safe=False)

