from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework import viewsets
from .serializers import Local_statSerializer
from .models import Local_stat


# Create your views here.
# class Dept_chartView(TemplateView):
#     template_name = 'stats/chart.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["qs"] = Local_stat
#         return context


def index(request):
    return render(request, "stats/templates/base_stat.html")

class Dept_chartView(viewsets.ModelViewSet):
    queryset = Local_stat.objects.all().order_by('department')
    serializer_class = Local_statSerializer

