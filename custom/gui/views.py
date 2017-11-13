from __future__ import absolute_import  # Python 2 only
from jinja2 import Environment
import json
import itertools
import logging
from django.contrib.staticfiles.storage import staticfiles_storage
from django.core.urlresolvers import reverse
from django.contrib.auth import logout as log_out
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.contrib import messages
from django.forms.formsets import formset_factory
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.decorators.csrf import ensure_csrf_cookie
from custom.utils.models import Logger
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from django.views.generic.base import View

from custom.utils.models import Logger
from custom.users.models import MileStone
from custom.users.models import Advantage
from custom.users.models import AdvantageLink
from custom.users.models import Profile
from custom.gui.models import Slide
from custom.gui.models import Service
from custom.gui.models import FAQ
from custom.gui.models import QualifyQuestion
from custom.gui.models import QualifyQuestionnaire
from custom.blog.models import Category
from custom.blog.models import Post
from custom.messaging.models import Message

from rest_framework.parsers import JSONParser
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes, permission_classes
from rest_framework import generics
from restless.views import Endpoint

from custom.gui.serializers import GlobalSearchSerializer
from custom.gui.serializers import ServiceSerializer
from custom.blog.serializers import CategorySerializer


@api_view(['POST','GET'])
@renderer_classes((JSONRenderer,))
@permission_classes([AllowAny,])
#@ensure_csrf_cookie
def confirm_account_view(request):
    """
     A view that confirms the user
    """
    try:
       log = Logger(log="WE HAVE HIT THE ENDPOINT {}".format(request.body)) 
       log.save()
 #      data = json.loads(request.body).encode('utf-8')
       data = JSONParser().parse(request)
       log = Logger(log="WE HAVE HIT THE ENDPOINT {}".format(request.body))
       log.save()
       log = Logger(log='DATA WAS {}'.format(data))
       log.save()
       
       user_id = data['user_id'].encode('utf-8')
       username = data['username'].encode('utf-8')
       first = data['first'].encode('utf-8')
       last = data['last'].encode('utf-8')
       phone = data['phone'].encode('utf-8')
       email = data['email'].encode('utf-8')

       if email:
           users_email = User.objects.filter(~Q(id = int(user_id)), email=email)
       else:
           users_email = []

       if phone:
           users_phone = Profile.objects.filter(~Q(id = int(user_id)), phone=phone)       
       else:
           users_phone = []

       if username:
           users_username = Profile.objects.filter(~Q(id = int(user_id)), username=username)
       else:
           users_username = []

       content = None

       if len(users_email) > 0:
           content = {'user_activated': False,
                      'error': {'email':'already used'}}

       if len(users_phone) > 0:
           if not content:
               content = {}
               content['user_activated'] = False
           if content.get('error') == None:
               content['error'] = {}
           content['error']['phone']='already used'

       if len(users_username) > 0:
           if not content:
               content = {}
               content['user_activated'] = False
           if content.get('error') == None:
               content['error'] = {}
           content['error']['username']='already used'
            

       if content and len(content) > 0 :
           log = Logger(log="WE GOT ERRORS {}".format(content))
           log.save()
           return Response(content)

       user = User.objects.get(id=int(user_id))
       user.first_name = first
       user.last_name = last
       user.profile.first_name = first
       user.profile.last_name = last
       user.profile.email = email
       user.email = email
       user.profile.phone = phone
       user.username = username
       user.profile.username = username
       user.profile.save()
       user.save()
    except Exception as e:
       first = ''
       last = ''
       phone = ''
       email = ''
       username = ''
       user_id = ''
       content = {'user_activated': False, 
                 'error': str(e), 
                 'last': '',
                 'first':''}

              
       log = Logger(log='FAILED TO CONFIRM {}'.format(e))
       log.save()
    
    content = {'user_activated': True, 
               'first': first, 
               'last': last, 
               'phone': phone, 
               'email': email,
               'username': username,
               'user_id': user_id}
    user = User.objects.get(id=user_id)
    user.profile.email = email
    user.email = email
    user.profile.is_activated = True
    user.profile.phone = phone
    user.username = username
    user.profile.username = username
    user.profile.save()
    user.save()

    return Response(content)


############################################
## Add a New Post view                    ##
## Extends: restless Endpoint             ##
## METHOD:  GET, POST                     ##
## Type:    Endpoint View (JSON)          ##
############################################

class GetSearchResultsView(Endpoint):
    @csrf_exempt
    def get(self, request):

        try:
            query = request.params.get('q','')

            categories = Category.objects.filter(Q(name__icontains=query) | 
                                                 Q(code__icontains=query))


            services = Service.objects.filter(Q(description__icontains=query) | 
                                              Q(statement__icontains=query) | 
                                              Q(title__icontains=query) | 
                                              Q(service__icontains=query))

            posts = Post.objects.filter(Q(title__icontains=query) | 
                                        Q(body__icontains=query))
        #    res = chain(posts,categories)

            all_results = list(posts)

            serializer_categories = CategorySerializer(categories, many=True)
            serializer_services = ServiceSerializer(services, many=True)
            serializer_posts = GlobalSearchSerializer(posts, many=True)
                               
            return { 'posts': serializer_posts.data,
                     'services': serializer_services.data,
                     'categories':serializer_categories.data,
                     'q':query }

        except Exception,R:
            return {'message':'error '+str(R)}


    @csrf_exempt
    def post(self, request):


        try:

            query = request.data['q']
            categories = Category.objects.filter(Q(name__icontains=query) | 
                                                 Q(code__icontains=query))

            services = Service.objects.filter(Q(description__icontains=query) | 
                                              Q(statement__icontains=query) | 
                                              Q(title__icontains=query) | 
                                              Q(service__icontains=query))

            posts = Post.objects.filter(Q(title__icontains=query) | 
                                        Q(body__icontains=query))
        #    res = chain(posts,categories)
            all_results = list(posts)
            serializer_categories = CategorySerializer(categories,many=True)
            serializer_services = ServiceSerializer(services,many=True)
            serializer_posts = GlobalSearchSerializer(posts,many=True)

            return {'posts':serializer_posts.data,
                    'services':serializer_services.data,
                    'categories':serializer_categories.data,
                    'q':query}


        except Exception,R:

            log = Logger(log=str(R))
            log.save()
            return {'message':'error  '+str(R)}


class GlobalSearchList(generics.ListAPIView):
   serializer_class = GlobalSearchSerializer

   def get_queryset(self):
      query = self.request.QUERY_PARAMS.get('query', None)
      posts = Post.objects.filter(Q(title__icontains=query) | Q(body__icontains=query) | Q(category__icontains=query))
      users = User.objects.filter(username__icontains=query)
      all_results = list(chain(posts, users)) 
      all_results.sort(key=lambda x: x.created)
      return all_results


@ensure_csrf_cookie
def environment(**options):
    env = Environment(**options)
    env.globals.update({
       'static': staticfiles_storage.url,
       'url': reverse,
    })
    return env

@ensure_csrf_cookie
def index(request):
    return render(request, 'index.html',{'home':'index.html'})


@ensure_csrf_cookie
def dashboard(request):
    
    milestones = MileStone.objects.all()
    advantage_links = AdvantageLink.objects.filter(advantage_id=1)
    slides = Slide.objects.all()
    faqs = FAQ.objects.all()
    posts = Post.objects.all()
    qquestions = QualifyQuestion.objects.all()
    categories = Category.objects.all()

    if request.user.is_authenticated():
        logout=True

        try:
           user_id = request.user.id
           username = request.user.username
           first_name = request.user.first_name
           last_name = request.user.last_name
           profile_image_path = ''
           logging.info("Loading dashboard")
        except Exception as e:
           logging.error("Error loading dashboard {0}".format(e))
           log = Logger(log='WE GOT SOME ERROR'+str(e))
           log.save()
           user_id = -1
           username = ''
           first_name = ''
           last_name = ''
           profile_image_path = ''

        if not request.user.profile.is_activated:
            return render(request, 'index-0.html',{'logout':logout,
                                                   'user_id':user_id,
                                                   'first':first_name,
                                                   'last':last_name,
                                                   'slides':slides,
                                                   'faqs':faqs,
                                                   'posts':posts,
                                                   'qualifying':qquestions,
                                                   'milestones':milestones,
                                                   'advantage_links':advantage_links,
                                                   'profile_image':""})# profile_image_path})

    else:

        user_id = -1
        logout=False
        username = ''
        first_name = ''
        last_name = ''
        profile_image_path = ''
        

        return render(request, 'index-0.html',{'logout':logout,
                                               'user_id':user_id,
                                               'first':first_name,
                                               'last':last_name,
                                               'slides':slides,
                                               'faqs':faqs,
                                               'posts':posts,
                                               'qualifying':qquestions,
                                               'milestones':milestones,
                                               'advantage_links':advantage_links,
                                               'profile_image':""})# profile_image_path})

    
    try:
        messages = Message.objects.filter(receiver_id=user_id, is_seen=False) 
        total_unseen = len(messages)
        log = Logger(log='total unseen is %d'%total_unseen)
        log.save()
    except Exception as e:
        total_unseen = 0
        log = Logger(log='Failed on total unseen  %s'%str(e))
        log.save()


    return render(request, 'dashboard.html',{'logout':logout,
                                           'user_id':user_id,
                                           'first':first_name,
                                           'last':last_name,
                                           'slides':slides,
                                           'faqs':faqs,
                                           'total_unseen': total_unseen,
                                           'qualifying':qquestions,
                                           'posts':posts,
                                           'categories':categories,
                                           'milestones':milestones,
                                           'advantage_links':advantage_links,
                                           'profile_image':profile_image_path})



@ensure_csrf_cookie
def home(request):
    milestones = MileStone.objects.all()
    advantage_links = AdvantageLink.objects.filter(advantage_id=1)
    slides = Slide.objects.all()
    faqs = FAQ.objects.all()
    posts = post = Post.objects.all()
    qquestions = QualifyQuestion.objects.all()

    if request.user.is_authenticated():
        logout=True
        try:
           user_id = request.user.id
           username = request.user.username
           first_name = request.user.first_name
           last_name = request.user.last_name
           profile_image_path = '' 
        except Exception, R:
           log = Logger(log='WE GOT SOME ERROR'+str(R))
           log.save()
           user_id = -1
           username = ''
           first_name = ''
           last_name = ''
           profile_image_path = ''

    else:
        user_id = -1
        logout=False
        username = ''
        first_name = ''
        last_name = ''
        profile_image_path = ''
 
    return render(request, 'index-0.html',{'logout':logout,
                                           'user_id':user_id,
                                           'first':first_name,
                                           'last':last_name,
                                           'slides':slides,
                                           'faqs':faqs,
                                           'qualifying':qquestions,
                                           'posts':posts,
                                           'milestones':milestones,
                                           'advantage_links':advantage_links,
                                           'profile_image':profile_image_path})

@ensure_csrf_cookie
def about(request):
    milestones = MileStone.objects.all()
    advantage_links = AdvantageLink.objects.filter(advantage_id=1)
    slides = Slide.objects.all()
    faqs = FAQ.objects.all()
    posts = Post.objects.all()
    qquestions = QualifyQuestion.objects.all()

    if request.user.is_authenticated():
        logout=True
        try:
           user_id = request.user.id
           username = request.user.username
           first_name = request.user.first_name
           last_name = request.user.last_name
           profile_image_path = ''
        except Exception, R:
           log = Logger(log='WE GOT SOME ERROR'+str(R))
           log.save()
           user_id = -1
           username = ''
           first_name = ''
           last_name = ''
           profile_image_path = ''

    else:
        user_id = -1
        logout=False
        username = ''
        first_name = ''
        last_name = ''
        profile_image_path = ''

    return render(request, 'index-0.html',{'logout':logout,
                                           'user_id':user_id,
                                           'first':first_name,
                                           'last':last_name,
                                           'service':'about',
                                           'slides':slides,
                                           'faqs':faqs,
                                           'qualifying':qquestions,
                                           'posts':posts,
                                           'milestones':milestones,
                                           'advantage_links':advantage_links,
                                           'profile_image':profile_image_path})


@ensure_csrf_cookie
def services(request,service):
    milestones = MileStone.objects.all()
    advantage_links = AdvantageLink.objects.filter(advantage_id=1)
    slides = Slide.objects.all()
    faqs = FAQ.objects.all()
    posts = Post.objects.all()
    qquestions = QualifyQuestion.objects.all()

    if request.user.is_authenticated():
        logout=True
        try:
           user_id = request.user.id
           username = request.user.username
           first_name = request.user.first_name
           last_name = request.user.last_name
           profile_image_path = ''
        except Exception, R:
           log = Logger(log='WE GOT SOME ERROR'+str(R))
           log.save()
           user_id = -1
           username = ''
           first_name = ''
           last_name = ''
           profile_image_path = ''

    else:
        user_id = -1
        logout=False
        username = ''
        first_name = ''
        last_name = ''
        profile_image_path = ''

    return render(request, 'index-0.html',{'logout':logout,
                                           'user_id':user_id,
                                           'first':first_name,
                                           'last':last_name,
                                           'service':service,
                                           'slides':slides,
                                           'faqs':faqs,
                                           'qualifying':qquestions,
                                           'posts':posts,
                                           'milestones':milestones,
                                           'advantage_links':advantage_links,
                                           'profile_image':profile_image_path})

@ensure_csrf_cookie
def posts(request,page):
    milestones = MileStone.objects.all()
    advantage_links = AdvantageLink.objects.filter(advantage_id=1)
    slides = Slide.objects.all()
    faqs = FAQ.objects.all()
    posts = Post.objects.all()
    qquestions = QualifyQuestion.objects.all()

    if request.user.is_authenticated():
        logout=True
        try:
           user_id = request.user.id
           username = request.user.username
           first_name = request.user.first_name
           last_name = request.user.last_name
           profile_image_path = ''
        except Exception, R:
           log = Logger(log='WE GOT SOME ERROR'+str(R))
           log.save()
           user_id = -1
           username = ''
           first_name = ''
           last_name = ''
           profile_image_path = ''

    else:
        user_id = -1
        logout=False
        username = ''
        first_name = ''
        last_name = ''
        profile_image_path = ''

    return render(request, 'index-0.html',{'logout':logout,
                                           'user_id':user_id,
                                           'first':first_name,
                                           'last':last_name,
                                           'service':"blog",
                                           'slides':slides,
                                           'faqs':faqs,
                                           'qualifying':qquestions,
                                           'posts':posts,
                                           'milestones':milestones,
                                           'advantage_links':advantage_links,
                                           'profile_image':profile_image_path})


@ensure_csrf_cookie
def post(request):
    milestones = MileStone.objects.all()
    advantage_links = AdvantageLink.objects.filter(advantage_id=1)
    slides = Slide.objects.all()
    faqs = FAQ.objects.all()
    posts = Post.objects.all()
    qquestions = QualifyQuestion.objects.all()

    if request.user.is_authenticated():
        logout=True
        try:
           user_id = request.user.id
           username = request.user.username
           first_name = request.user.first_name
           last_name = request.user.last_name
           profile_image_path = ''
        except Exception, R:
           log = Logger(log='WE GOT SOME ERROR'+str(R))
           log.save()
           user_id = -1
           username = ''
           first_name = ''
           last_name = ''
           profile_image_path = ''

    else:
        user_id = -1
        logout=False
        username = ''
        first_name = ''
        last_name = ''
        profile_image_path = ''

    return render(request, 'index-0.html',{'logout':logout,
                                           'user_id':user_id,
                                           'first':first_name,
                                           'last':last_name,
                                           'service':"blog",
                                           'slides':slides,
                                           'faqs':faqs,
                                           'qualifying':qquestions,   
                                           'posts':posts,
                                           'milestones':milestones,
                                           'advantage_links':advantage_links,
                                           'profile_image':profile_image_path})


@ensure_csrf_cookie
def pricing(request):
    if request.user.is_authenticated():
        logout=True
        try:
           user_id = request.user.id
           profile = User.objects.get(id=request.user.id)
           username = request.user.username
           first_name = request.user.first_name
           last_name = request.user.last_name
           profile_image_path = profile.profile_image_path
        except Exception, R:
           log = Logger(log='WE GOT SOME ERROR'+str(R))
           log.save()
           user_id = -1
           username = ''
           first_name = ''
           last_name = ''
           profile_image_path = ''

    else:
        user_id = -1
        logout=False
        username = ''
        first_name = ''
        last_name = ''
        profile_image_path = ''

    return render(request, 'index-3.html',{'logout':logout,
                                           'user_id':user_id,
                                           'first':first_name,
                                           'last':last_name,
                                           'profile_image':profile_image_path})

@ensure_csrf_cookie
def ask(request):
    if request.user.is_authenticated():
        logout=True
        try:
           user_id = request.user.id
           profile = User.objects.get(id=request.user.id)
           username = request.user.username
           first_name = request.user.first_name
           last_name = request.user.last_name
           profile_image_path = profile.profile_image_path
        except Exception, R:
           user_id = -1
           username = ''
           first_name = ''
           last_name = ''
           profile_image_path = ''

    else:
        user_id = -1
        logout=False
        username = ''
        first_name = ''
        last_name = ''
        profile_image_path = ''

    return render(request, 'index-3.html',{'logout':logout,
                                           'user_id':user_id,
                                           'first':first_name,
                                           'last':last_name,
                                           'profile_image':profile_image_path})

@ensure_csrf_cookie
def contacts(request):
    if request.user.is_authenticated():
        logout=True
        try:
           user_id = request.user.id
           profile = User.objects.get(id=request.user.id)
           username = request.user.username
           first_name = request.user.first_name
           last_name = request.user.last_name
           profile_image_path = profile.profile_image_path
 
        except Exception, R:
           log = Logger(log='WE GOT SOME ERROR'+str(R))
           log.save()
           user_id = -1
           username = ''
           first_name = ''
           last_name = ''
           profile_image_path = ''

    else:
        user_id = -1
        logout=False
        username = ''
        first_name = ''
        last_name = ''
        profile_image_path = ''

    return render(request, 'index-4.html',{'logout':logout,
                                           'user_id':user_id,
                                           'first':first_name,
                                           'last':last_name,
                                           'profile_image':profile_image_path})

@ensure_csrf_cookie
def payment(request):
    milestones = MileStone.objects.all()
    advantage_links = AdvantageLink.objects.filter(advantage_id=1)
    slides = Slide.objects.all()
    faqs = FAQ.objects.all()
    posts = Post.objects.all()
    qquestions = QualifyQuestion.objects.all()

    if request.user.is_authenticated():
        logout=True
        try:
           user_id = request.user.id
           username = request.user.username
           first_name = request.user.first_name
           last_name = request.user.last_name
           profile_image_path = ''
        except Exception, R:
           log = Logger(log='WE GOT SOME ERROR'+str(R))
           log.save()
           user_id = -1
           username = ''
           first_name = ''
           last_name = ''
           profile_image_path = ''

    else:
        user_id = -1
        logout=False
        username = ''
        first_name = ''
        last_name = ''
        profile_image_path = ''

    return render(request, 'index-0.html',{'logout':logout,
                                           'user_id':user_id,
                                           'first':first_name,
                                           'last':last_name,
                                           'service':'payment',
                                           'slides':slides,
                                           'faqs':faqs,
                                           'posts':posts,
                                           'qualifying':qquestions, 
                                           'milestones':milestones,
                                           'advantage_links':advantage_links,
                                           'profile_image':profile_image_path})


@ensure_csrf_cookie
def toast(request):
    if request.user.is_authenticated():
        logout=True
        try:
           user_id = request.user.id
           profile = User.objects.get(id=request.user.id)
           username = request.user.username
           first_name = request.user.first_name
           last_name = request.user.last_name
           profile_image_path = profile.profile_image_path
        except Exception, R:
           log = Logger(log='WE GOT SOME ERROR'+str(R))
           log.save()
           user_id = -1
           username = ''
           first_name = ''
           last_name = ''
           profile_image_path = ''

    else:
        user_id = -1
        logout=False
        username = ''
        first_name = ''
        last_name = ''
        profile_image_path = ''

    return render(request, 'toast.html',{'logout':logout,
                                           'first':first_name,
                                           'user_id':user_id,
                                           'last':last_name,
                                           'profile_image':profile_image_path})


@ensure_csrf_cookie
def blog(request):
    if request.user.is_authenticated():
        logout=True
    else:
        logout=False

    return render(request, 'blog.html',{'blog':'blog.html'})

@ensure_csrf_cookie
def divorce(request):
    if request.user.is_authenticated():
        logout=True
        try: 
           user_id = request.user.id
           username = request.user.username
           first_name = request.user.first_name
           last_name = request.user.last_name
           profile_image_path = profile.profile_image_path
        except Exception, R:

           log = Logger(log='WE GOT SOME ERROR'+str(R))
           log.save()
           user_id = -1
           username = ''
           first_name = ''
           last_name = ''
           profile_image_path = ''

    else:
        logout=False
        username = ''
        first_name = ''
        last_name = ''
        profile_image_path = ''

    return render(request, 'divorce.html',{'divorce':'divorce.html','logout':logout,
                                                                    'user_id':user_id,
                                                                    'first':first_name,
                                                                    'last':last_name,
                                                                    'profile_image':profile_image_path})

@ensure_csrf_cookie
def logout(request):
    log_out(request)
    milestones = MileStone.objects.all()
    advantage_links = AdvantageLink.objects.filter(advantage_id=1)
    slides = Slide.objects.all()

    if request.user.is_authenticated():
        logout=True
        try:
           user_id = request.user.id
           username = request.user.username
           first_name = request.user.first_name
           last_name = request.user.last_name
           profile_image_path = ''
        except Exception, R:
           log = Logger(log='WE GOT SOME ERROR'+str(R))
           log.save()
           user_id = -1
           username = ''
           first_name = ''
           last_name = ''
           profile_image_path = ''

    else:
        user_id = -1
        logout=False
        username = ''
        first_name = ''
        last_name = ''
        profile_image_path = ''

    return HttpResponseRedirect('/')


@ensure_csrf_cookie
def check_qualify(request):

    milestones = MileStone.objects.all()
    advantage_links = AdvantageLink.objects.filter(advantage_id=1)
    slides = Slide.objects.all()
    faqs = FAQ.objects.all()
    posts = Post.objects.all()
    qquestions = QualifyQuestion.objects.all()

    if request.user.is_authenticated():
        logout=True
        try:
           user_id = request.user.id
           username = request.user.username
           first_name = request.user.first_name
           last_name = request.user.last_name
           profile_image_path = ''
        except Exception, R:
           log = Logger(log='WE GOT SOME ERROR'+str(R))
           log.save()
           user_id = -1
           username = ''
           first_name = ''
           last_name = ''
           profile_image_path = ''

    else:
        user_id = -1
        logout=False
        username = ''
        first_name = ''
        last_name = ''
        profile_image_path = ''

    return render(request, 'index-0.html',{'logout':logout,
                                           'user_id':user_id,
                                           'first':first_name,
                                           'last':last_name,
                                           'service':'qualify',
                                           'slides':slides,
                                           'faqs':faqs,
                                           'qualifying':qquestions,
                                           'posts':posts,
                                           'milestones':milestones,
                                           'advantage_links':advantage_links,
                                           'profile_image':profile_image_path})


@ensure_csrf_cookie
def contact(request):

    milestones = MileStone.objects.all()
    advantage_links = AdvantageLink.objects.filter(advantage_id=1)
    slides = Slide.objects.all()
    faqs = FAQ.objects.all()
    posts = Post.objects.all()
    qquestions = QualifyQuestion.objects.all()

    if request.user.is_authenticated():
        logout=True
        try:
           user_id = request.user.id
           username = request.user.username
           first_name = request.user.first_name
           last_name = request.user.last_name
           profile_image_path = ''
        except Exception, R:
           log = Logger(log='WE GOT SOME ERROR'+str(R))
           log.save()
           user_id = -1
           username = ''
           first_name = ''
           last_name = ''
           profile_image_path = ''

    else:
        user_id = -1
        logout=False
        username = ''
        first_name = ''
        last_name = ''
        profile_image_path = ''

    return render(request, 'index-0.html',{'logout':logout,
                                           'user_id':user_id,
                                           'first':first_name,
                                           'last':last_name,
                                           'qualifying':qquestions,
                                           'service':'contact',
                                           'slides':slides,
                                           'faqs':faqs,
                                           'posts':posts,
                                           'milestones':milestones,
                                           'advantage_links':advantage_links,
                                           'profile_image':profile_image_path})

@ensure_csrf_cookie
def pricing(request):

    milestones = MileStone.objects.all()
    advantage_links = AdvantageLink.objects.filter(advantage_id=1)
    slides = Slide.objects.all()
    faqs = FAQ.objects.all()
    posts = Post.objects.all()
    qquestions = QualifyQuestion.objects.all()

    if request.user.is_authenticated():
        logout=True
        try:
           user_id = request.user.id
           username = request.user.username
           first_name = request.user.first_name
           last_name = request.user.last_name
           profile_image_path = ''
        except Exception, R:
           log = Logger(log='WE GOT SOME ERROR'+str(R))
           log.save()
           user_id = -1
           username = ''
           first_name = ''
           last_name = ''
           profile_image_path = ''

    else:
        user_id = -1
        logout=False
        username = ''
        first_name = ''
        last_name = ''
        profile_image_path = ''

    return render(request, 'index-0.html',{'logout':logout,
                                           'user_id':user_id,
                                           'first':first_name,
                                           'last':last_name,
                                           'qualifying':qquestions,
                                           'service':'pricing',
                                           'slides':slides,
                                           'faqs':faqs,
                                           'posts':posts,
                                           'milestones':milestones,
                                           'advantage_links':advantage_links,
                                           'profile_image':profile_image_path})


class DashboardLogoutViewMixin(object):
    def get_context_data(self,**kwargs):
        context = super(DashboardLogoutViewMixin,
                  self).get_context_data(**kwargs)
        return context


class DashboardLogoutView(DashboardLogoutViewMixin, TemplateView):
    template_name = "inedex-0.html"
    def get(self, request):
        threshold=180
        if request.user.is_authenticated():
               logout(request)
        return render(request, 'index-0.html',{ 'FB_APP_ID' : settings.SOCIAL_AUTH_FACEBOOK_KEY,'logout':False })
 
