---
title: Contributing
page_id: contributing
toc: false
#type: resources
redirect_from: /website/contributing
---


A key aim of the community is to enable sharing of knowledge, methods (i.e. software and workflows), and expertise: to accelerate progress across the community, foster collaborations, and reduce replication of effort.

Here, we outline an initial set of contribution mechanisms that are intended to allow for community sharing, and 
attribution of credit to those who have created the work being shared.

{% include callout.html type="important" content="Additional contribution guidelines will be added as they are prioritised by the community." %}


## Sharing computational workflows

{% include callout.html type="important" content="Workflows from a [ASBC community collection on the WorkflowHub registry](https://workflowhub.eu/collections/40) will be automatically imported and displayed on a dedicated software page soon. Additional instructions will be available soon. For now, if you would like your workflows listed on the website when the integration with WorkflowHub is ready, please follow the instructions below." %}


#### 1. [Register as a WorkflowHub user and either set up, or join, a Team](https://about.workflowhub.eu/docs/organising-and-setup/)


#### 2. [Register your workflow(s) on WorkflowHub](https://about.workflowhub.eu/docs/registering_workflows/registering-a-workflow/)


#### 3. Annotate these workflows by adding the minimum metadata highlighted here

<div class="resource-table-wrapper table-responsive mt-4 mb-5" markdown="1">

| Field                      | Description / extra information |
|----------------------------|--------------------------------------------------------------------|
| Workflow title             | Make sure the title is descriptive and highlights what the workflow does.|
| Creator(s)               | If you have included a `CITATION.cff` file in your GitHub repository, WorkflowHub can parse this and automatically populate the creator field. |
| Description              | Note that descriptions included in GitHub repository README files will be automatically parsed by WorkflowHub. |
| Maturity                 | Indicate if the workflow is `mature` or a `work-in-progress`. |
| License                    | Note that if a license file is included in your GitHub repository it will be automatically parsed by WorkflowHub. |
| EDAM Topics and Operations | Add concepts from [EDAM](https://github.com/edamontology/edamontology) as standardised short descriptions of workflow domain, purpose, and function. You can search for EDAM terms within the WorkflowHub workflow registration wizard. You can also use [EDAM browser](https://edamontology.github.io/edam-browser/) to explore and search the EDAM ontology for appropriate concepts. |
{: .tooltable .table .table-bordered .table-striped .w-100}

</div>

The metadata included above is based on a BioCommons [example available here](https://australianbiocommons.github.io/how-to-workflowhub-space/new_workflow#add-minimum-metadata).
