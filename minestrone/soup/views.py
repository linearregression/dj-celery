from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, FormView
from django import forms

from minestrone.soup import tasks

class JobsView(TemplateView):
    template_name = 'soup/jobs.html'

class EditorView(FormView):

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

    template_name = 'soup/editor.html'
    success_url = '/jobs/'
    form_class = FormAddJob

    def form_valid(self, form):
        name = form.cleaned_data['job_name']
        queue = form.cleaned_data['queue_name']
        tasks.lazy_job.apply_async(args=[name], rounting_key=queue)
        return HttpResponseRedirect(self.get_success_url())
