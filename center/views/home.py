from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from center.models import Category, Product, Like
from django.core.paginator import Paginator
from django.db.models import Q, Count, Max


def Index(request):
    categories = Category.objects.all()

    if request.GET.get('catid'):
        cat_id = request.GET.get('catid')
        cat_id = int(cat_id[0])
        if cat_id != 0:
            if request.GET.get('lt'):
                lt = int(request.GET.get('lt'))
                gt = int(request.GET.get('gt'))
                prod = Product.objects.filter(Q(price__lt=lt) & Q(
                    price__gte=gt) & Q(category_id=cat_id))
            else:
                prod = Product.objects.filter(category_id=cat_id)
        else:
            if request.GET.get('lt'):
                lt = int(request.GET.get('lt'))
                gt = int(request.GET.get('gt'))
                prod = Product.objects.filter(
                    Q(price__lt=lt) & Q(price__gte=gt))
    else:
        cat_id = 0
        prod = Product.objects.all()
    for pr in prod:
        pr.numLikes = Like.objects.filter(product=pr).count()
    paging = Paginator(prod, 6)
    page = request.GET.get('page')
    products = paging.get_page(page)
    cat_id = int(cat_id)
    data = {'cats': categories, 'prods': products,
            'catNo': cat_id}
    return render(request, 'home/index.html', data)


def addAjaxLike(request):
    prodId = request.GET.get('prodId')
    productData = Product.objects.get(id=prodId)
    newLike = Like()
    newLike.product = productData
    newLike.save()
    numLikes = Like.objects.filter(product=productData).count()
    return JsonResponse(numLikes, safe=False)


def removeAjaxLike(request):
    prodId = request.GET.get('prodId')
    productData = Product.objects.get(id=prodId)
    objdelete = Like.objects.filter(product=productData).order_by("-id")[0]
    # oldLike = Like.objects.aggregate(Max('id'))
    # objdelete = Product.objects.get(id=oldLike)
    objdelete.delete()
    numLikes = Like.objects.filter(product=productData).count()
    return JsonResponse(numLikes, safe=False)
