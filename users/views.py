from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserCreateForm
from .models import User
from django.shortcuts import reverse
from django.shortcuts import render

# Create your views here.


class UserListView(LoginRequiredMixin, ListView):
    template_name = "users/user_list.html"
    queryset = User.objects.all()
    context_object_name = "users"
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(UserListView, self).get_context_data(**kwargs)
        books = self.get_queryset()
        page = self.request.GET.get('page')
        paginator = Paginator(books, self.paginate_by)
        try:
            books = paginator.page(page)
        except PageNotAnInteger:
            books = paginator.page(1)
        except EmptyPage:
            books = paginator.page(paginator.num_pages)
        context['books'] = books
        return context

class UserCreateView(LoginRequiredMixin, CreateView):
    template_name = "users/user_create.html"
    form_class = UserCreateForm
    context_object_name = "user-create"

    def get_success_url(self):
        return reverse("user-list")

class UserUpdateView(UpdateView):
    model = User
    template_name = "users/user_update.html"
    context_object_name = "user-update"
    fields = (
        'first_name',
        'last_name',
        'username',
        'email',
        'phone',
        'is_admin',
    )

    def get_success_url(self):
        return reverse('user-list')

class UserDeleteView(DeleteView):
    model = User
    template_name = "users/user_delete.html"

    def get_success_url(self):
        return reverse('user-list')
