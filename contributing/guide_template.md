---
title: [How-to-Guide template]
contributors: [Johan Gustafsson]
description: Add a plain text description here.
affiliations: [Australian BioCommons]
---

> Before you start using this template!
> 1. Add your name to the contributors section of the guide above
> 2. Make sure to also add your name to [`contributors.yml`](_data/contributors.yml)
> 3. Add a plain text description to the section above
> 4. Add affiliations to the section above: make sure to also update [`affiliations.yml`](_data/affiliations.yml)
> 5. Add citation information in the format provided below:

**Note:** if this guide helped you, please cite it as follows
> Citation information goes here!

## heading 1

Content goes here!

Adding an image:

>{% include image.html file="Australian-Biocommons-Logo-Horizontal-144dpi-Transparent.png" caption="Fig 1. Australian BioCommons logo"%}

{% include image.html file="Australian-Biocommons-Logo-Horizontal-144dpi-Transparent.png" caption="Fig 1. Australian BioCommons logo"%}

See [this link](https://elixir-belgium.github.io/elixir-toolkit-theme/markdown_cheat_sheet#images) for more info on images.

### heading 2

Content goes here!

Below is an example callout, which comes in multiple styles: `note`, `important`, `tip` and `warning`.
The bold section of the script below should include one of these styles. The text in *italics* can be modified as needed.
        
>{% include callout.html type="**note**" content="*callout content text*" %}

{% include callout.html type="note" content="If you need help, the Galaxy community is both approachable and helpful. [Ask them questions!](https://help.galaxyproject.org/)" %}

See examples of these callouts [here](https://elixir-belgium.github.io/elixir-toolkit-theme/markdown_cheat_sheet#message-boxes).

#### heading 3

Content goes here!
