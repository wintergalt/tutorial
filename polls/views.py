#from django.template import Context, loader
from polls.models import Poll
from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response, get_object_or_404

# Old index version (see how render_to_response() works better)
#def index(request):
#    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
#    t = loader.get_template('polls/index.html')
#    c = Context({
#        'latest_poll_list': latest_poll_list,
#    })
#    return HttpResponse(t.render(c))

# Old detail version
#def index(request):
#    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
#    return render_to_response('polls/index.html', {'latest_poll_list': latest_poll_list})
def index(request):
    p = get_object_or_404(Poll, pk=poll_id)
    return render_to_response('polls/index.html', {'poll': p})

def detail(request, poll_id):
    try:
        p = Poll.objects.get(pk=poll_id)
    except Poll.DoesNotExist:
        raise Http404
    return render_to_response('polls/detail.html', {'poll': p})

def results(request, poll_id):
    return HttpResponse("You are looking at the results of poll: %s." % poll_id)

def vote(request, poll_id):
    return HttpResponse('You are voting on poll: %s.' % poll_id)