from django_filters import rest_framework
from rest_framework import generics, permissions
# from .models import Presupuesto, PresupuestoProducto
# from .serializers import PresupuestoSerializer
from .filters import PresupuestoFilter
# from usuarios.models import Usuario
from rest_framework import serializers
# from productos.models import Producto

# class ListarPresupuestosView(generics.ListAPIView):
#     serializer_class = PresupuestoSerializer
#     permission_classes = [permissions.IsAuthenticated]
#     filter_backends = [rest_framework.DjangoFilterBackend]
#     filterset_class = PresupuestoFilter

#     def get_queryset(self):
#         user = self.request.user
#         return Presupuesto.objects.filter(usuario=user)

# class AgregarPresupuestoView(generics.CreateAPIView):
#     queryset = Presupuesto.objects.all()
#     serializer_class = PresupuestoSerializer
#     permission_classes = [permissions.IsAuthenticated]

#     def perform_create(self, serializer):
#         usuario = self.request.user
#         empresa = usuario.empresa_seleccionada
#         print(f'Saving presupuesto for user: {usuario.id} and empresa: {empresa.id}')
#         serializer.save(usuario=usuario, empresa=empresa)

# class EditarPresupuestoView(generics.UpdateAPIView):
#     queryset = Presupuesto.objects.all()
#     serializer_class = PresupuestoSerializer
#     permission_classes = [permissions.IsAuthenticated]

# class EliminarPresupuestoView(generics.DestroyAPIView):
#     queryset = Presupuesto.objects.all()
#     serializer_class = PresupuestoSerializer
#     permission_classes = [permissions.IsAuthenticated]
#     lookup_field = 'numero_presupuesto'

# class DetallePresupuestoView(generics.RetrieveAPIView):
#     queryset = Presupuesto.objects.all()
#     serializer_class = PresupuestoSerializer
#     permission_classes = [permissions.IsAuthenticated]
#     lookup_field = 'numero_presupuesto'

# class ImpriPresupuestoView(generics.RetrieveAPIView):
#     queryset = Presupuesto.objects.all()
#     serializer_class = PresupuestoSerializer
#     permission_classes = [permissions.IsAuthenticated]
#     lookup_field = 'numero_presupuesto'

from rest_framework import generics, permissions
from .models import Presupuesto
from .serializers import PresupuestoSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

class ListarPresupuestosView(generics.ListAPIView):
    serializer_class = PresupuestoSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [rest_framework.DjangoFilterBackend]
    filterset_class = PresupuestoFilter

    def get_queryset(self):
        user = self.request.user
        return Presupuesto.objects.filter(usuario=user)

class AgregarPresupuestoView(generics.CreateAPIView):
    queryset = Presupuesto.objects.all()
    serializer_class = PresupuestoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        usuario = self.request.user
        empresa = usuario.empresa_seleccionada
        serializer.save(usuario=usuario, empresa=empresa)

class EliminarPresupuestoView(generics.DestroyAPIView):
    serializer_class = PresupuestoSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'numero_presupuesto'

    def get_queryset(self):
        return Presupuesto.objects.filter(usuario=self.request.user)

class DetallePresupuestoView(generics.RetrieveAPIView):
    serializer_class = PresupuestoSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'numero_presupuesto'

    def get_queryset(self):
        return Presupuesto.objects.filter(usuario=self.request.user)

class RemitirPresupuestoView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request, pk, format=None):
        try:
            presupuesto = Presupuesto.objects.get(pk=pk, usuario=request.user)
        except Presupuesto.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        presupuesto.remitido = True
        presupuesto.save()

        return Response({"status": "Presupuesto remitido correctamente"}, status=status.HTTP_200_OK)