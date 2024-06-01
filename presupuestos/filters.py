import django_filters
from django.db.models import Q
from .models import Presupuesto

class PresupuestoFilter(django_filters.FilterSet):
    fecha_inicio = django_filters.CharFilter(field_name="fecha", lookup_expr='gte')
    fecha_fin = django_filters.CharFilter(field_name="fecha", lookup_expr='lte')
    palabra_clave = django_filters.CharFilter(method='filter_by_keyword')

    class Meta:
        model = Presupuesto
        fields = ['fecha']

    def filter_by_keyword(self, queryset, name, value):
        return queryset.filter(
            Q(cliente__nombre_apellido__icontains=value) |
            Q(cliente__numero_identificacion__icontains=value) |
            Q(cliente__pais__icontains=value) |
            Q(cliente__provincia__icontains=value) |
            Q(cliente__localidad__icontains=value) |
            Q(cliente__domicilio__icontains=value) |
            Q(cliente__email__icontains=value) |
            Q(cliente__telefono__icontains=value) |
            Q(productos__producto__nombre__icontains=value) |
            Q(productos__producto__codigo_sku__icontains=value) |
            Q(productos__producto__codigo_barra__icontains=value) |
            Q(productos__producto__categoria__icontains=value) |
            Q(productos__producto__precio_venta_usd__icontains=value) |
            Q(productos__producto__observaciones__icontains=value) |
            Q(observaciones__icontains=value)
        )