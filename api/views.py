import json
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from .models import products


def getSort(data):
    """
    Assings a better format for passing into ORM
    this method eliminates the extra space of "+" sign
    and also inverts the "-" sign to the first site
    """
    sort = (data.get('sort')).split(',')
    sort = [x.strip() for x in sort]
    # It allows one or two values of param, and the order didn't cares
    if "-" in sort[0]:
        sort[0] = sort[0][-1]+sort[0][:-1]
    elif len(sort) > 1:
        sort[1] = sort[1][-1]+sort[1][:-1]
    return sort


def filterList(data):
    """
    This method provides the functionality to search by field,
    set what fields to retrive and sort it.
    But you can perform the three, two or just one action,
    no matter the order in URL

    It evaluates if the Request needs
    1. fields and sort and specific field
    2. fields and specific field
    3. sort and specific field
    4. only specific field
    5. and also it evaluates the same cases without specific field
    """
    fields = data.get('field').split(',') if data.get('field') else None
    sort = getSort(data) if data.get('sort') else None
    # It evaluates in every field 4 cases
    # ID case
    if data.get("id"):
        if fields != None and sort != None:
            listData = list(products.objects.filter(
                id=data.get("id")).values(*fields).order_by(*sort))
        elif fields != None:
            listData = list(products.objects.filter(
                id=data.get("id")).values(*fields))
        elif sort != None:
            listData = list(products.objects.filter(
                id=data.get("id")).values().order_by(*sort))
        else:
            listData = list(products.objects.filter(
                id=data.get("id")).values())
    # NAME case
    elif data.get("name"):
        if fields != None and sort != None:
            listData = list(products.objects.filter(
                name=data.get("name")).values(*fields).order_by(*sort))
        elif fields != None:
            listData = list(products.objects.filter(
                name=data.get("name")).values(*fields))
        elif sort != None:
            listData = list(products.objects.filter(
                name=data.get("name")).values().order_by(*sort))
        else:
            listData = list(products.objects.filter(
                name=data.get("name")).values())
    # BRAND case
    elif data.get("brand"):
        if fields != None and sort != None:
            listData = list(products.objects.filter(
                brand=data.get("brand")).values(*fields).order_by(*sort))
        elif fields != None:
            listData = list(products.objects.filter(
                brand=data.get("brand")).values(*fields))
        elif sort != None:
            listData = list(products.objects.filter(
                brand=data.get("brand")).values().order_by(*sort))
        else:
            listData = list(products.objects.filter(
                brand=data.get("brand")).values())
    # CREATED_AT case
    elif data.get("created_at"):
        if fields != None and sort != None:
            listData = list(products.objects.filter(
                created_at=data.get("created_at")).values(*fields).order_by(*sort))
        elif fields != None:
            listData = list(products.objects.filter(
                created_at=data.get("created_at")).values(*fields))
        elif sort != None:
            listData = list(products.objects.filter(
                created_at=data.get("created_at")).values().order_by(*sort))
        else:
            listData = list(products.objects.filter(
                created_at=data.get("created_at")).values())
    # UPDATED_AT case
    elif data.get("updated_at"):
        if fields != None and sort != None:
            listData = list(products.objects.filter(
                updated_at=data.get("updated_at")).values(*fields).order_by(*sort))
        elif fields != None:
            listData = list(products.objects.filter(
                updated_at=data.get("updated_at")).values(*fields))
        elif sort != None:
            listData = list(products.objects.filter(
                updated_at=data.get("updated_at")).values().order_by(*sort))
        else:
            listData = list(products.objects.filter(
                updated_at=data.get("updated_at")).values())
    # No SPECIFIC VALUE case
    else:
        if fields != None and sort != None:
            listData = list(products.objects.all().values(
                *fields).order_by(*sort))
        elif fields != None:
            listData = list(products.objects.all().values(*fields))
        elif sort != None:
            listData = list(products.objects.all().values().order_by(*sort))
    return listData


class ProductsView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    # Function that return only one record acording to pk value (URL)
    def get(self, request, pk=0):
        if pk > 0:
            productsList = list(products.objects.filter(id=pk).values())
            if len(productsList) > 0:
                context = {
                    "message": "Success",
                    "status_code": 200,
                    "products": productsList,
                }
            else:
                context = {
                    "message": "Not found",
                    "status_code": 400,
                }
        else:
            try:
                # Assign a list depending of which case apply
                if len(request.GET) > 0:
                    productsList = filterList(request.GET)
                # Just return all the objects because GET params aren't passed
                else:
                    productsList = list(products.objects.all().values())
                # Evaluates if list isn't empty
                if len(productsList) > 0:
                    context = {
                        "message": "Success",
                        "status_code": 200,
                        "products": productsList,
                    }
                else:
                    context = {
                        "message": "Not found",
                        "status_code": 400,
                    }
            except:
                context = {
                    "message": "Parameters aren't valid",
                    "status_code": 400,
                }
        return JsonResponse(context)

    def post(self, request):
        try:
            newProduct = products(
                name=request.POST["name"], brand=request.POST["brand"])
            newProduct.save()
            context = {
                "message": f"Product {newProduct.id} ({newProduct.name}) added",
                "status_code": 200,
            }
        except:
            context = {
                "message": "Parameters aren't valid",
                "status_code": 400,
            }
        return JsonResponse(context)

    def put(self, request, pk):
        product_exist = list(products.objects.filter(id=pk).values())
        if len(product_exist) > 0:
            product_exist = products.objects.get(id=pk)
            product_exist.name = request.GET["name"]
            product_exist.brand = request.GET["brand"]
            product_exist.save()
            context = {
                "message": f"Product {product_exist.id} Updated!",
                "status_code": 200,
            }
        else:
            context = {
                "message": "Parameters aren't valid",
                "status_code": 400,
            }
        return JsonResponse(context)

    def delete(self, request, pk):
        product_exist = list(products.objects.filter(id=pk).values())
        if len(product_exist) > 0:
            product_exist = products.objects.get(id=pk)
            product_exist.delete()
            context = {
                "message": f"Product {pk} was deleted successfully!",
                "status_code": 200,
            }
        else:
            context = {
                "message": "Parameters aren't valid",
                "status_code": 400,
            }
        return JsonResponse(context)
