from django.shortcuts import render

from django.http import HttpResponse
from archive.models import Article
from django.http import HttpResponseRedirect
from django.contrib import messages
import os
# Create your views here.

def hello_world(request):
    return HttpResponse("hello world")

def article_content(request):
    article = Article.objects.all()[0]
    article_id = article.article_id
    title = article.title
    author = article.author
    abstract = article.abstract
    publish_date = article.publish_date

    return_str = title
    return HttpResponse(return_str)

def get_root(request):
    return render(request,'archive/index.html')

def get_upload_file(request):
    return render(request,'archive/upload.html')

def get_index_page(request):
    all_article = Article.objects.all()
    return render(request,'archive/classification.html',
                  {
                        'article_list':all_article
                    })

def search(request):
    #print("run here")
    all_article = Article.objects.all()
    #print(all_article)
    q = request.GET.get('q')
    if not q:
        error_msg = '请输入关键词再进行搜索'
        return render(request, 'archive/error.html', {'error_msg': error_msg})
    print(q)
    #q = "article: "+q
    post_list = all_article.filter(title__icontains=q)
    print(post_list)
    if post_list:
        return render(request, 'archive/result.html', {'article_list': post_list})
    error_msg = '没有找到相关文章'
    return render(request, 'archive/error.html', {'error_msg': error_msg})

def upload_file(request):
    if request.method == "POST":    # 请求方法为POST时，进行处理
        myFile =request.FILES.get("myfile", None)    # 获取上传的文件，如果没有文件，则默认为None
        print(myFile)
        if not myFile:
            print("upload failed")
            return HttpResponse("no files for upload!")
        destination = open('D:/upload_files/'+myFile.name,'wb+')    # 打开特定的文件进行二进制的写操作
        for chunk in myFile.chunks():      # 分块写入文件
            destination.write(chunk)
        destination.close()
        print("upload success")
        #messages.success(request,"upload success")
        return HttpResponse("上传成功!")
