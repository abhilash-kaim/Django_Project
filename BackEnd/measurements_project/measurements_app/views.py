from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import WaistMeasurement


@csrf_exempt
def get_waist_measurements(request):
    if request.method == 'POST':
        height = request.POST.get('height')
        age = request.POST.get('age')
        weight = request.POST.get('weight')

        waist_measurements = WaistMeasurement.objects.filter(
            height=height,
            age=age,
            weight=weight
        )

        waist_values = [measurement.waist for measurement in waist_measurements]

        return JsonResponse({'waist_measurements': waist_values}, status=200)

    return JsonResponse({'message': 'Invalid request method'}, status=400)


@csrf_exempt
def add_waist_measurement(request):
    if request.method == 'POST':
        height = request.POST.get('height')
        age = request.POST.get('age')
        weight = request.POST.get('weight')
        waist = request.POST.get('waist')

        WaistMeasurement.objects.create(
            height=height,
            age=age,
            weight=weight,
            waist=waist
        )

        return JsonResponse({'message': 'Measurement added successfully'}, status=201)

    return JsonResponse({'message': 'Invalid request method'}, status=400)
