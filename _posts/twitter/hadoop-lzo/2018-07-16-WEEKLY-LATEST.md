---
layout: weekly-metrics-v0.1
title: TwiterOSS Metrics Report for twitter/hadoop-lzo | WEEKLY-2018-07-16
permalink: /twitter/hadoop-lzo/WEEKLY/

owner: twitter
repo: hadoop-lzo
reportID: WEEKLY-2018-07-16
datestampThisWeek: 2018-07-16
datestampLastWeek: 2018-07-06
---

<table style="width: 100%">
    <tr>
        <th>Metric</th>
        <th>This Week</th>
        <th>Last Week</th>
        <th>+/-</th>
    </tr>
    {% for item in site.data["twitter"]["hadoop-lzo"]["WEEKLY-2018-07-16"]["data"] %}
    <tr>
        <th>{{ item[0] }}</th>
        <th>{{ item[1]["this_week"] }}</th>
        <th>{{ item[1]["last_week"] }}</th>
        <th>{{ item[1]["diff"] }}</th>
    </tr>
    {% endfor %}
</table>
