
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .models import Sale, Position, Purchase, Liuxiangpinzhong
import csv
from django.http import HttpResponse

# Create your views here.


def _get_userid(request):
    """
    此方法根据 当前登录用户的 id 去 数据库查询 已经绑定的品种。
    :param request:  调用者的 request
    :return: 返回一个 品种列表 ['862458', '865484', ] 给模型 in 用
    """
    UserID = request.user.id
    UserPinZhong = Liuxiangpinzhong.objects.filter(liuxiangid=UserID)
    UserPinZhongList = [item.spbh_c for item in UserPinZhong]
    return UserPinZhongList


def _home_page(request):
    return render(request, 'home.html')


def _login_page(request):
    if request.method == 'POST':
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        users = authenticate(username=user, password=pwd)
        if users and users.is_active:
            login(request, users)
            return redirect('_home')
    return render(request, 'login.html')


def _sale_page(request):

    upzlist = _get_userid(request)
    sale_data = list(Sale.objects.filter(spbh__in=upzlist))
    sale_context = {
        'Sale': sale_data
    }

    return render(request, 'Sale.html', sale_context)


def _position_page(request):
    upzlist = _get_userid(request)
    position_date = list(Position.objects.filter(spbh__in=upzlist))


    position_context = {
        'Position': position_date
    }

    return render(request, 'Position.html', position_context)


def _purchase_page(request):
    upzlist = _get_userid(request)
    purchase_date = list(Purchase.objects.filter(spbh__in=upzlist))
    purchase_context = {
        'Purchase': purchase_date
    }

    return render(request, 'Purchase.html', purchase_context)


def _sale_Csv(request):
    # 销售数据
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="SomeFile.csv"'
    writer = csv.writer(response)

    upzlist = _get_userid(request)
    sale_data = list(Sale.objects.filter(spbh__in=upzlist))
    writer.writerow(['商品编号', '商品名称', '商品规格', '生产厂家', '数量', '单位名称', '保质期', '批号', '日期', '含税单价', '含税金额', '开票员'])
    for item in sale_data:
        writer.writerow([item.spbh, item.spmch, item.shpgg, item.shengccj, item.shl, item.dwmch, item.sxrq, item.pihao2, item.rq, item.hshj, item.hsje, item.kaipy])
    return response


def _position_Csv(request):
    # 库存数据
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="SomeFile.csv"'
    writer = csv.writer(response)

    upzlist = _get_userid(request)
    position_date = list(Position.objects.filter(spbh__in=upzlist))
    writer.writerow(['商品编号', '商品名称', '商品规格', '生产厂家', '数量', '单位名称', '保质期', '批号', '入库日期'])
    for item in position_date:
        writer.writerow([item.spbh, item.spmch, item.shpgg, item.shengccj, item.shl, item.dwmch, item.sxrq, item.pihao2, item.rkrq])
    return response


def _purchase_Csv(request):
    # 采购数据
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="SomeFile.csv"'
    writer = csv.writer(response)


    upzlist = _get_userid(request)
    purchase_date = list(Purchase.objects.filter(spbh__in=upzlist))

    writer.writerow(['商品编号', '商品名称', '商品规格', '生产厂家', '数量', '单位名称', '保质期', '批号', '入库日期', '含税单价', '含税金额'])
    for item in purchase_date:
        writer.writerow([item.spbh, item.spmch, item.shpgg, item.shengccj, item.shl2, item.dwmch, item.sxrq, item.pihao2, item.rq, item.hshj, item.hsje])
    return response
