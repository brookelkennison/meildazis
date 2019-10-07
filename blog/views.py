# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from blog.forms import CommentForm
from blog.models import Post, Comment


# Create your views here.


def blog_index(request):
    post = Post.objects.all().order_by('-created_on')
    context = {
        'posts': post
    }
    return render(request, 'blog_index.html', context)


def blog_detail(request, post_id):
    post = Post.objects.get(pk=post_id)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post
            )
            comment.save()
    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
        "form": form,
    }
    return render(request, "blog_detail.html", context)
