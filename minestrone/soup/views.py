from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from django import forms

def jobs(request):
    return render_to_response('soup/jobs.html')

def editor(request):

    class FormAddJob(forms.Form):

        job_name = forms.CharField(
                max_length=128,
                required=True,
                label='Job name:'
        )
        queue_name = forms.CharField(
                max_length=128,
                required=True,
                label='Queue name:',
                initial='default'
        )

    if request.method == 'POST':
        form = FormAddJob(request.POST)
        if form.is_valid():
            # TODO: Enqueue the job!
            return HttpResponseRedirect('/jobs/')
    else:
        form = FormAddJob(auto_id=True)

    return render_to_response(
            'soup/editor.html',
            {'form': form},
            context_instance=RequestContext(request)
    )
