from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
from django.contrib.auth import get_user_model, logout
from django.urls import reverse_lazy
from .models import Card, Transaction
from .forms import CardForm
from .utils import getDateFromShortString
from .filters import CardFilter
User = get_user_model()


# Create your views here.
class HomeView(ListView):
    model = Card
    filterset_class = CardFilter
    template_name:str = 'core/home.html'
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if not self.request.user.is_authenticated:
            context['object_list'] = []
            return context

        context['filter_obj'] = self.filterset_class(self.request.GET, queryset=self.model.objects.all())
        return context

    def get_queryset(self):
        if '_clear' in self.request.GET:
            return super().get_queryset()     
        
        card_qs = self.filterset_class(self.request.GET, queryset=Card.objects.all()).qs
        return Card.objects.filter(pk__in=card_qs)
             

class MyLoginView(LoginView):
    template_name: str = 'login.html'


def logoutUser(request):
    logout(request)
    return redirect('home')


####################
#   CRUD SECTION   #  
####################

def modifyDate(request):
    post_copy = request.POST.copy()
    post_copy['date_expired'] = post_copy['date_expired'] if 'date_expired' in post_copy else ''
    post_copy['date_expired'] = getDateFromShortString(post_copy['date_expired'])
    return post_copy['date_expired']


class CreateCardView(CreateView):
    model = Card
    form_class = CardForm
    template_name: str = 'core/create.html'
    success_url = reverse_lazy('home')


    def form_valid(self, form):
        form.instance.date_expired = modifyDate(self.request)
        return super().form_valid(form)


class UpdateCardView(UpdateView):
    model = Card
    fields = ('date_expired', 'status')
    template_name: str = 'core/update.html'
    success_url = reverse_lazy('home')


class DeleteCardView(DeleteView):
    model = Card
    template_name = 'delete.html'
    success_url = reverse_lazy('home')


#########################
# Activate / Deactivate #
#########################


def activateCard(request, pk):
    try:
        obj = Card.objects.get(pk=pk)
    except Exception:
        return redirect('home')
    
    if not obj.is_active:
        obj.activate()
        obj.save()
    
    return redirect('home')


def deactivateCard(request, pk):
    try:
        obj = Card.objects.get(pk=pk)
    except Exception as e:
        return redirect('home')

    if obj.is_active:
        obj.deactivate()
        obj.save()

    return redirect('home')


######################
# Transaction Views  #
######################


class TransactionListView(DetailView):
    model = Card
    template_name: str = 'core/transactions_list.html'
    
    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        
        if not self.request.user.is_authenticated:
            context['object'] = None
            return context
        
        context['card_transactions'] = Transaction.objects.select_related("card").filter(card=self.get_object()) 
        context['card_transactions_count'] = len(context['card_transactions'])

        return context


        