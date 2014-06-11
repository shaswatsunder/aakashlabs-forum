# Imports {{{
from PIL import Image as PImage
import itertools
from aakashlabs.settings import MEDIA_URL
from forum.models import *

from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404

from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Count

    
def main(request, url):
    context = RequestContext(request)
    if url == 'latest' :
        posts=Post.objects.all().order_by("-created_date")
        context_dict = {
            'posts': posts,}
    elif url == 'votes':
        posts=Post.objects.all().order_by("-count")
        context_dict = {
            'posts': posts,}
        
    elif url == 'unanswered':
        posts=Post.objects.all()
        replies = Reply.objects.all()
        files = []
    
        for p in posts :
            a=0
            for r in replies :
                if r.title.title == p.title :
                    a=1
            if a == 0:
                files.append(p)
            context_dict = {
                'posts': files,}
    
    elif url == 'frequent':
        posts=Post.objects.all()
        categories = Category.objects.all()
        replies = Reply.objects.all()
        for c in categories:
            temp=0
	    for p in posts:
		if p.category.category == c.category :
			temp = temp+1
	p.count=temp
        new_posts=Post.objects.all().order_by("-count")		
        context_dict = {
            'posts': new_posts,'replies':replies,}

    elif url == '':
        posts= Post.objects.all()
        context_dict = {
            'posts': posts,}
 
   
    return render_to_response('forum/latest.html', context_dict, context)
    
    
def question_link(request, id, url):
    context = RequestContext(request)
    if url == 'question_link/(?P<id>\d+)':
        post = Post.objects.get(pk=id)
        replies = Reply.objects.filter(title=post)

        context_dict = {
            'post': post,
            'replies': replies,
        }
    
    return render_to_response("forum/question_link.html", context_dict, context)

def latest_link(request, id):
    context = RequestContext(request)

    post = Post.objects.get(pk=id)
    replies = Reply.objects.filter(title=post)
   
    context_dict = {
        'post': post,
        'replies': replies,
    }
    
    return render_to_response("forum/latest_link.html", context_dict, context)

def votes_link(request, id):
    context = RequestContext(request)

    post = Post.objects.get(pk=id)
    replies = Reply.objects.filter(title=post)
   
    context_dict = {
        'post': post,
        'replies': replies,
    }
    
    return render_to_response("forum/votes_link.html", context_dict, context)



