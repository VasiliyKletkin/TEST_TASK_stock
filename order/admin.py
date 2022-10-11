from urllib.error import HTTPError
from django.contrib import admin
from .models import Order
import requests
from .serializers import OrderSerializer
from django.conf import settings

# тут можно получать список всех складов
hosts = ['127.0.0.1:8001', '127.0.0.1:8002']

# тут можно получать какие модели имеют API
api_model = {
    Order: settings.API_V1 + "order/",
}


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'number', 'status']

    def save_model(self, request, obj, form, change):
        obj.user = request.user

        if obj.__class__ in api_model:

            project_host = request.get_host()
            path = request.path

            for host in hosts:
                if project_host != host:

                    serializer = OrderSerializer(obj)
                    response = None
                    try:
                            
                        if '/add/' in path:
                            response = requests.post(
                                "http://" + host + api_model[obj.__class__], serializer.data)

                        elif '/change/' in path:
                            response = requests.put(
                                "http://" + host + api_model[obj.__class__] + str(obj.id) + '/', serializer.data)
                    except requests.exceptions.HTTPError as e:
                         raise HTTPError("Ошибка синхронизации",
                                        response=e.response.text)

                    if not response:
                        print("Ошибка синхронизации" +
                              response.url + response.status_code)
                        raise HTTPError("Ошибка синхронизации",
                                        response=response)

            super().save_model(request, obj, form, change)
        else:
            super().save_model(request, obj, form, change)


admin.site.register(Order, OrderAdmin)
