from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from todo.models import TaskList, Task

def task_lists(request):
	task_lists = TaskList.objects.all()
	json_tasks = [l.to_json() for l in task_lists]
	return JsonResponse(json_tasks, safe=False)

def task_list_detail(request, pk):
	try:
		task_list = TaskList.objects.get(id = pk)
	except TaskList.DoesNotExist as e:
		return JsonResponse({'error': str(e)})

	return JsonResponse(task_list.to_json())

def tasks(request, pk):
	try:
		task_list = TaskList.objects.get(id = pk)
	except TaskList.DoesNotExist as e:
		return JsonResponse({'error': str(e)})

	tasks = task_list.task_set.all()
	json_tasks = [t.to_json() for t in tasks]
	return JsonResponse(json_tasks, safe = False)


# def task_lists(request):
#     tasks = TaskList.objects.all()
#     json_tasks = [t.to_json() for t in tasks]
#     data = {
#         'task_list': json_tasks
#     }
#     return JsonResponse(data, safe=False)
#
# def task_lists_num(request, pk):
#     json_tasks = TaskList.objects.get(id = pk).to_json()
#     data = {
#         'task_list': json_tasks
#     }
#     return JsonResponse(data, safe=False)
#
# def task_lists_num_tasks(request, num):
#     json_tasks_1 = TaskList.objects.get(id = num)
#     json_tasks_2 = json_tasks_1.objects.all()
#     json_tasks = [t.to_json() for t in json_tasks_2]
#     data = {
#         'task_list': json_tasks
#     }
#     return JsonResponse(data, safe=False)