from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.messages import constants
from django.contrib import messages

from .models import Building, City, Visits

def home(request):
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    city = request.GET.get('city')
    kind = request.GET.getlist('kind')
    cities = City.objects.all()

    if min_price or max_price or city or kind:
    
        if not min_price:
            min_price = 0
        if not max_price:
            max_price = 999999999
        if not kind:
            kind = ['A', 'H']

        real_estate = Building.objects.filter(value__gte=min_price).filter(value__lte=max_price).filter(immovable_type__in=kind).filter(city=city)

    else:
        real_estate = Building.objects.all()
    

    context = {
        'real_state': real_estate,
        'cities': cities
    }

    return render(request, 'home.html', context)


def building(request, id):

    if request.user.is_authenticated:
        building = get_object_or_404(Building, id=id)
        suggestions = Building.objects.filter(city=building.city).exclude(id=id)[:2]
        context = {
            'building': building, 
            'suggestions': suggestions, 
            'id': id
        }
        return render(request, 'building.html', context)
    else:
        messages.add_message(request, constants.WARNING, 'Login required')
        return redirect('/auth/login')


def schedule_visit(request):
    user = request.user
    day = request.POST.get('day')
    timetable = request.POST.get('timetable')
    id_building = request.POST.get('id_building')
    visit = Visits(
        building_id=id_building,
        user=user,
        day=day,
        timetable=timetable
    )
    visit.save()
    return redirect('/agendamentos')