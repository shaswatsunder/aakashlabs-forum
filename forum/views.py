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
        """ to fetch the latest posts with titles as link """                       
        posts=Post.objects.all().order_by("-created_date")
        context_dict = {
            'posts': posts,}
    
        
    elif url == 'unanswered':
        """ to fetch the unanswered posts with titles as link """
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
    
   
    elif url == '':
        """ to fetch all posts with titles as link """
        posts= Post.objects.all()
        context_dict = {
            'posts': posts,}
 
   
    return render_to_response('forum/allqueries.html', context_dict, context)
    

def allqueries_link(request, id):
    
    context = RequestContext(request) # to display the latest, unanswered and  all posts with replies 

    post = Post.objects.get(pk=id)
    replies = Reply.objects.filter(title=post)
    comments = Comment.objects.filter(answer=Reply.objects.get(pk=id))
   
    context_dict = {
        'post': post,
        'replies': replies,
        'comments': comments,
    }
    
    return render_to_response("forum/allqueries_link.html", context_dict, context)

def frequent(request):
    """ to fetch the frequent posts with titles as link """
    context = RequestContext(request)
    posts=Post.objects.all().order_by("-count")
    context_dict = {
            'posts': posts,}
    return render_to_response('forum/frequent.html', context_dict, context)
    
def votes(request):
    """ to fetch the most voted posts with titles as link """
    context = RequestContext(request)
    posts=Post.objects.all().order_by("-count")
    context_dict = {
            'posts': posts,}
    return render_to_response('forum/votes.html', context_dict, context)
    

def frequent_link(request, id):
        """ to display the frequent posts with replies """
	context = RequestContext(request)
	post = Post.objects.get(pk=id)
	post.count = post.count + 1
	post.save()
	replies = Reply.objects.filter(title=post)
	context_dict = {
        	'post': post,
          	'replies': replies,
          }
	return render_to_response("forum/allqueries_link.html", context_dict, context)

def votes_link(request, id):
        """ to display the most voted posts with replies """
	context = RequestContext(request)
	post = Post.objects.get(pk=id)
	post.count = post.count + 1
	post.save()
	replies = Reply.objects.filter(title=post)
	context_dict = {
        	'post': post,
          	'replies': replies,
          }
	return render_to_response("forum/allqueries_link.html", context_dict, context)










