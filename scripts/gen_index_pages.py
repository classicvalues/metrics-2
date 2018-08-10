"""
This script creates the index.html for all the projects (and orgs).

e.g.
/metrics/twitter
/metrics/twitter/twemoji
"""

from glob import glob
import os

PATH_TO_METRICS_POSTS = "_posts"
PATH_TO_GRAPHS = "graphs"

ALL_ORGS = filter(os.path.isdir, glob(PATH_TO_METRICS_POSTS + "/*"))
ALL_PROJECTS = filter(os.path.isdir, glob(PATH_TO_METRICS_POSTS + "/*/*"))

project_text = """\
---
layout: default
permalink: /{org}/{repo}/
---
Welcome to {repo}'s metrics homepage!
<br><br>
Latest WEEKLY Report - <a href="{weekly_metrics_link}">{weekly_metrics_link}</a>
<br>
Latest MONTHLY Report - <a href="{monthly_metrics_link}">{monthly_metrics_link}</a>
<br>
"""

for project in ALL_PROJECTS:
    print("LOG: Starting with", project)
    _, org, repo = project.split("/")
    weekly_metrics_link = "https://twitter.github.io/metrics/{}/{}/WEEKLY".format(org, repo)
    monthly_metrics_link = "https://twitter.github.io/metrics/{}/{}/MONTHLY".format(org, repo)
    _text = project_text.format(org=org,
                                repo=repo,
                                weekly_metrics_link=weekly_metrics_link,
                                monthly_metrics_link=monthly_metrics_link)
    file_path = project + "/" + "2018-05-29-index.md"  # Don't change the date. This prevents duplicate posts.
    with open(file_path, "w+") as f:
        f.write(_text)
    print("LOG: Wrote to", file_path)

org_text = """\
---
layout: default
permalink: /{org}/
---
Welcome to {org}'s metrics homepage!
<br><br>
Latest WEEKLY Report - <a href="{weekly_metrics_link}">{weekly_metrics_link}</a>
<br>
Latest MONTHLY Report - <a href="{monthly_metrics_link}">{monthly_metrics_link}</a>
<br>

"""

for _org in ALL_ORGS:
    print("LOG: Starting with", _org)
    _, org = _org.split("/")
    weekly_metrics_link = "https://twitter.github.io/metrics/{}/WEEKLY".format(org)
    monthly_metrics_link = "https://twitter.github.io/metrics/{}/MONTHLY".format(org)
    _text = org_text.format(org=org,
                                weekly_metrics_link=weekly_metrics_link,
                                monthly_metrics_link=monthly_metrics_link)

    # Add graphs
    all_graphs = glob(PATH_TO_GRAPHS + "/" + org + "/*.svg")
    # Might be helpful - https://stackoverflow.com/questions/22051573/how-to-hide-image-broken-icon-using-only-css-html-without-js
    # To arrange the images - http://jsfiddle.net/89dtxt6s/1645/
    for graph in all_graphs:
        # _text += '<img src="{{{{ site.url }}}}{{{{ site.baseurl }}}}/{}">\n'.format(graph)
        _text += '<object type="image/svg+xml" data="{{{{ site.url }}}}{{{{ site.baseurl }}}}/{}">\n'.format(graph)
        _text += '\tYour browser does not support SVG\n\n'
        _text += '</object>\n'
        # _text += open(graph).read()
        # _text += "\n\n"

    file_path = _org + "/" + "2018-05-29-index.md"  # Don't change the date. This prevents duplicate posts.
    with open(file_path, "w+") as f:
        f.write(_text)
    print("LOG: Wrote to", file_path)