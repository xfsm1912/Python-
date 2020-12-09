# TradingMonitor/views.py

from django.shortcuts import render
from .models import Position


def render_positions(request, asset):
    positions = Position.objects.filter(asset=asset)
    context = {'asset': asset, 'position': positions}
    return render(request, 'positions.html', context)


