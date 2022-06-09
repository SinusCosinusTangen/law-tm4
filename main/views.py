from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view

from main.models import Mahasiswa

# Create your views here.
@api_view(['POST'])
def update(request):
    try:
        mahasiswa = Mahasiswa(nama=request.data['nama'], npm=request.data['npm'])
        mahasiswa.save()
        response = {'status': 'OK'}
        return JsonResponse(response)
    except KeyError:
        response = {'status': 'KEY ERROR', 'message': 'Nama dan NPM harus diisi'}
        return JsonResponse(response)

@api_view(['GET'])
def read(request, npm):
    try:
        mahasiswa = Mahasiswa.objects.get(npm=npm)
        response = {'status': 'OK', 'npm': mahasiswa.npm, 'nama': mahasiswa.nama}
        return JsonResponse(response)
    except Mahasiswa.DoesNotExist:
        response = {'status': 'NOT FOUND'}
        return JsonResponse(response)