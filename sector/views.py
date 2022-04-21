from django.shortcuts import redirect, render
from sector.models import Sector


def sector(request):
    sector = Sector.objects.all()
    data = {
        'sector': sector,
    }
    return render(request, 'sector/sector.html', data)


def addsector(request):
    if request.method == "POST":
        sector_name = request.POST['sector_name']
        sector = Sector(sector_name=sector_name)
        sector.save()
        return redirect('sector')
    return render(request, 'sector/add.html')
