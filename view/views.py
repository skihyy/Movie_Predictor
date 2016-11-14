from django.shortcuts import render_to_response, get_object_or_404, render
from django.http import HttpResponse
from django.template import RequestContext
from view.models import MovieScore, MovieInfo


# Create your views here.
def add(request):
    # return render_to_response('sample.html', {'sss':1}, context_instance=RequestContext(request))
    return render(request, 'sample.html')


def show(request):
    newMovieInfo = MovieInfo(
        request.POST["title"],
        request.POST["genre"],
        request.POST["actorID"],
        request.POST["directorID"],
        request.POST["length"]
    )

    newMovieInfo.save()
    result = get_object_or_404(MovieInfo, title=request.POST["title"]).id

    return render_to_response('sample.html', {'result': result},
                              context_instance=RequestContext(request))
