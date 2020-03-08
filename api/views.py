import json

from django.views.generic import ListView, DeleteView,CreateView
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict

from todo.models import Todo


class ApiTodoLV(ListView):
    model = Todo

    def render_to_response(self, context, **response_kwargs):
        todoList = list(context['object_list'].values())

        return JsonResponse(data=todoList, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class ApiTodoDelV(DeleteView):
    model = Todo

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return JsonResponse(data={}, status=204)


@method_decorator(csrf_exempt, name='dispatch')
class ApiTodoCV(CreateView):
    model = Todo
    fields = '__all__'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['data'] = json.loads(self.request.body)
        return kwargs

    def form_valid(self, form):
        self.object = form.save()
        newTodo = model_to_dict(self.object)
        return JsonResponse(data=newTodo, status=201)

    def form_invalid(self, form):
        return JsonResponse(data=form.errors, status=400)
