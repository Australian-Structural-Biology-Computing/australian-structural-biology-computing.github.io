---
description: WorkflowHub table
title: Workflows
page_id: workflows
toc: false
datatable: true
---

The interactive table below allows you to search for workflows [registered by Australian Structural Biology Computing comminity members on WorkflowHub](https://dev.workflowhub.eu/programmes/10). If you would like to add your bioinformatics workflows to [WorkflowHub](https://workflowhub.eu/), please see this [getting started guide](https://about.workflowhub.eu/docs/getting-started/).

{% comment %}
<div class="d-flex flex-column">
  <div class="mb-2">
    <button
      class="btn btn-secondary text-light"
      type="button"
      data-bs-toggle="collapse"
      data-bs-target="#collapse1"
      aria-expanded="false"
      aria-controls="collapseExample"
    >
      Can’t find the workflows you need? Click here to see other options for
      finding computational workflows.
      <i class="fa-solid fa-circle-chevron-down ms-1"></i>
    </button>
    <div class="collapse" id="collapse1">
      <div class="card card-body">
        <ul>
          <li>
            {% tool "workflowhub" %}
          </li>
          <li>
            {% tool "dockstore" %}
          </li>
          <li>
            {% tool "nf-core" %}
          </li>
          <li>
            {% tool "snakemake-registry" %}
          </li>
        </ul>
      </div>
    </div>
  </div>
</div>
{% endcomment %}

<div markdown="0"> 
{% include table.html url = "https://dev.workflowhub.eu" %}
</div>