from django.utils.decorators import method_decorator
from django.views.generic import (
    TemplateView,
)
from django.contrib.auth.decorators import login_required
from .models import Passage
from .tables import PassageTable
from .filters import PassageFilter
from django_tables2.views import SingleTableMixin
from django_tables2.export.views import ExportMixin
from django_filters.views import FilterView
from django.contrib.auth.mixins import PermissionRequiredMixin


class HomeView(TemplateView):
    template_name = 'logscope/home.html'


@method_decorator(login_required, name='dispatch')
class PassageTableView(PermissionRequiredMixin, ExportMixin, SingleTableMixin, FilterView):
    model = Passage
    template_name = 'logscope/passage.html'
    permission_required = ('passages.can_view',)
    table_class = PassageTable
    filterset_class = PassageFilter


@method_decorator(login_required, name='dispatch')
class AnalyticsView(TemplateView):
    template_name = 'logscope/analytics.html'


@method_decorator(login_required, name='dispatch')
class MicrosoftAnalyticsView(TemplateView):
    template_name = 'logscope/microsoft_analytics.html'


@method_decorator(login_required, name='dispatch')
class LocationAnalyticsView(TemplateView):
    template_name = 'logscope/usage_by_location.html'


class WikiView(TemplateView):
    template_name = 'logscope/wiki.html'
