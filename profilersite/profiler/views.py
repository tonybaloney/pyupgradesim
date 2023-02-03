from django.http import HttpRequest
from django.shortcuts import render
from django.contrib import messages

import pathlib

# Create your views here.
from collections import defaultdict

import pandas as pd
from bokeh.embed import components
from bokeh.models import NumeralTickFormatter
from bokeh.plotting import figure
from bokeh.resources import INLINE
from django_q.tasks import async_task, fetch_group, queue_size

def home(request: HttpRequest):
    if request.method == 'POST':
        if 'version' in request.POST and request.POST['version']:
            for version in request.POST.getlist('version'):
                time = int(request.POST['time'])
                users = int(request.POST['users'])
                name = async_task('profiler.tasks.test_version', version, time, users, group="loadtest")
                messages.add_message(request, messages.INFO, f'Queued test \'{name}\' of {version} for {time} seconds with {users} users')

    # file to save the model
    quantiles = [0.5, 0.66, 0.75, 0.8, 0.9, 0.95]
    stats = defaultdict(dict)

    for version in ['3.8', '3.9', '3.10', '3.11']:
        path = pathlib.Path.cwd().parent.joinpath(f'results/results_{version}_fullstats.csv')
        df = pd.read_csv(path).drop(['exception', 'start_time', 'response_length'], axis=1)
        df.round({'response_time': 2})

        groups = df.groupby(['request_type', 'name'])
        
        for name, group in groups:
            qu = group.quantile(quantiles, numeric_only=True)
            stats[' '.join(name)][version] = qu

    scripts = []
    divs = []
    urls = []

    for url, data in stats.items():
        graph = figure(title = f"Load Test for {url}", x_axis_label = 'Quantile', y_axis_label = 'Response time (ms)')
        colors = iter(['red', 'green', 'blue', 'purple', 'brown', 'orange'])
        for version, data in data.items():
            graph.line(quantiles, data['response_time'], legend_label=version, line_color=next(colors), line_width=2)

        graph.xaxis.formatter = NumeralTickFormatter(format='0 %')
        # render template
        script, div = components(graph)
        scripts.append(script)
        divs.append(div)
        urls.append(url)
        
    # grab the static resources
    js_resources = INLINE.render_js()
    css_resources = INLINE.render_css()

    return render(
            request,
        'ui.html',
        context = {
            "plot_scripts":scripts,
            "plot_divs":divs,
            "urls": urls,
            "js_resources":js_resources,
            "css_resources":css_resources,
            "tasks": tasks,
        }
    )


def tasks(request, number=10):
    return render(request, 'tasks.html', context={'tasks': fetch_group('loadtest')[:number], 'queued': queue_size()})