# -*- coding: utf-8 -*-

from django.shortcuts import render


# 接收POST请求数据
from django.template.context_processors import csrf


def search_post(request):
    ctx = {}
    ctx.update(csrf(request))
    if request.POST:
        ctx['rlt'] = request.POST['q']
        # q = .cleaned_data['q']
        # posts = Post.objects.filter(text__icontains=q)
        # context = {'q': q, 'posts': posts}
        # return_str = render_to_string('part_views/_post_search.html', context)
        # return HttpResponse(json.dumps(return_str), content_type='application/json')
    return render(request, "post/home.html", ctx)
