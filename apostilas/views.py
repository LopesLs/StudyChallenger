from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy

from .models import Apostila, ViewApostila
from .forms import ApostilaForm


class NewApostilaRequestHandler(LoginRequiredMixin, CreateView):
    model = Apostila
    form_class = ApostilaForm
    template_name = "apostila_create.html"
    success_url = reverse_lazy("apostila_create")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(NewApostilaRequestHandler, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["apostilas"] = Apostila.objects.filter(user=self.request.user)
        context["total_views"] = ViewApostila.objects.filter(
            apostila__user=self.request.user
        ).count()
        return context


class ApostilaDetailRequestHandler(LoginRequiredMixin, DetailView):
    model = Apostila
    template_name = "apostila_detail.html"
    context_object_name = "apostila"

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()

        view = ViewApostila(ip=request.META["REMOTE_ADDR"], apostila=self.object)

        view.save()

        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["views_unicas"] = (
            ViewApostila.objects.filter(apostila=self.object)
            .values("ip")
            .distinct()
            .count()
        )
        context["total_views"] = ViewApostila.objects.filter(
            apostila=self.object
        ).count()

        return context
