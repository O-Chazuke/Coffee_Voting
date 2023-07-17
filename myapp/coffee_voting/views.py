from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import get_object_or_404,render
from .models import Coffee,Voting
from django.db.models import Avg


class IndexView(generic.ListView):
    model = Coffee

class DetailView(generic.DetailView):
    model = Coffee
    #レーダーチャート用の平均値データ取り出し
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        results_time=get_object_or_404(Coffee, pk=self.kwargs.get('pk')).time
        minutes=(results_time % 3600) // 60
        seconds=results_time % 60
        context["results_time"]="{}分{}秒".format(minutes, seconds)
        results=Voting.objects.filter(coffee_id=self.kwargs['pk'])
        bitterness_result=results.aggregate(Avg('bitterness'))
        context['bitterness_avg']=bitterness_result['bitterness__avg']
        sourness_result=results.aggregate(Avg('sourness'))
        context['sourness_avg'] =sourness_result['sourness__avg']
        sweetness_result=results.aggregate(Avg('sweetness'))
        context['sweetness_avg'] =sweetness_result['sweetness__avg']
        richness_result=results.aggregate(Avg('richness'))
        context['richness_avg'] =richness_result['richness__avg']
        flavor_result=results.aggregate(Avg('flavor'))
        context['flavor_avg'] =flavor_result['flavor__avg']
        context['reviews']=results.values_list('review', flat=True)
        return context

class Coffee_CreateView(generic.edit.CreateView):
    model = Coffee
    fields = '__all__'

class UpdateView(generic.edit.UpdateView):
    model = Coffee
    fields = '__all__'

class DeleteView(generic.edit.DeleteView):
    model = Coffee
    success_url = reverse_lazy('coffee_voting:index')
    
    def dispatch(self, request, *args, **kwargs):
        if request.POST:
            obj = request.POST['delete_pass']
            if obj!='goma': #入力された合言葉が正しいか判断(この場合の正解合言葉はgoma)
                context={
                    'coffee': get_object_or_404(Coffee, pk=self.kwargs.get('pk')),
                    'error_message':'あいことばが違います'
                }
                return render(self.request,'coffee_voting/coffee_confirm_delete.html',context)
            
        return super(DeleteView, self).dispatch(request, *args, **kwargs)

class VotingView(generic.edit.CreateView):
    model = Voting
    fields = ['bitterness','sourness','sweetness','richness','flavor','review']
    template_name="coffee_voting/coffee_voting.html"
    
    #対応するCoffee.idの自動格納
    def form_valid(self, form):
        table = get_object_or_404(Coffee, pk=self.kwargs.get('pk'))
        form.instance.coffee_id = table
        return super().form_valid(form)
    
    #投票画面に豆の名前を表示するためのデータ取り出し
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['coffee_name']=Coffee.objects.filter(pk=self.kwargs['pk']).first()
        return context
