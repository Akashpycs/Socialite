from django.shortcuts import redirect, HttpResponse, render
from django.http import HttpResponse, JsonResponse
from comment.forms import CommentForm
from comment.models import Comment
from userpage.models import Post


def post_comment(request):
    if request.method == 'POST':

        if request.POST.get('action') == 'delete':
            id = request.POST.get('nodeid')
            c = Comment.objects.get(id=id)
            c.delete()
            return JsonResponse({'remove': id})

        else:

            post_id = request.POST.get('post_id')
            post = Post.objects.get(id=post_id)

            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():

                node_id = request.POST.get('nodeid')

                user_comment = comment_form.save(commit=False)
                result = comment_form.cleaned_data.get('content')

                user = request.user.username
                user_comment.post = post
                user_comment.name = request.user
                user_comment.save()
                node_id = user_comment.id

                return JsonResponse({'result': result, 'user': user, 'node_id': node_id})
