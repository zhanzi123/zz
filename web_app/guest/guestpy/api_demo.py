from sign.models import Event,Guest
from django.db.utils import IntegrityError
import time
# 添加嘉宾接口
def add_guest(request):
    # 首先获取传过来的数据信息
    eid = request.POST.get("eid","")
    name = request.POST.get('name','')
    limit = request.POST.get('limit', '')
    status = request.POST.get('status', '')
    address = request.POST.get('address', '')
    start_time = request.POST.get('start_time', '')

    if eid =="" or name =="" or limit =="" or status =="" or address =="" or start_time =="":
        return JsonResponse({'status':10021,'message':'parameter error'})
    result = Event.objects.filter(id=eid)
    if result:
        return JsonResponse({'status':10022,'message':'event id already exists'})
    result = Event.objects.filter(name=name)
    if result:
        return JsonResponse({'status': 10023, 'message': 'event name already exists'})
    if status == "":
        status = 1

    try:
        Event.objects.create(id=eid,name=name,limit=limit,address=address,status=int(status),start_time=start_time)
    except ValidationError as e:
        error = 'start_time format error.it must be in YYYY-MM-DD HH:MM:SS format.'
        return JsonResponse({'status': 10024, 'message':error})
    return JsonResponse({'status': 200, 'message': 'add event success'})