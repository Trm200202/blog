from django.shortcuts import render
from .models import ProfileData, About, SocialLink, Tools, Service,Project, Category, Post
# Create your views here.
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404


def home(request):
    # Django ORM < SQL Queries
    profile = ProfileData.objects.first()
    about = About.objects.first()                                           
    links = SocialLink.objects.all()
    Tool = Tools.objects.all()#bilish darajalarim
    services = Service.objects.all()
    projects = Project.objects.all()#loyihalar ro'yxati
    cotegorys = Category.objects.all()#
    context = {"profile" : profile,
                "about" : about, 
                'links': links, 
                'tools' : Tool, 
                'sevices': services,
                'projects': projects,
                'cotegorys': cotegorys}
    return render(request, 'index.html', context)


def about(request):
    toolss = Tools.objects.all()
    about = About.objects.first()
    return render(request, "about-us.html", context={"tools": toolss, "about":about})


def portfolio(request):
    return render(request, "portfolio.html")

def blog(request):
    posts = Post.objects.all()

    profile= ProfileData.objects.first()

    links = SocialLink.objects.all()

    search = request.GET.get("search")

    if search:
        posts = posts.filter(name__icontains=search)

    #pagination 
    paginator = Paginator(posts, 3)
    page_number = request.GET.get("page")
    page_objs = paginator.get_page(page_number)

    #popular post list
    popular_posts = Post.objects.all()[:2]

    return render(request, "blog.html", {'posts':page_objs, 
                                         "profile":profile, 
                                         "links":links,
                                          "popular_posts":popular_posts})


def blog_detail(request, pk):
    post = get_object_or_404(Post, id=pk)

    return render(request, "single-blog.html", {"post":post})