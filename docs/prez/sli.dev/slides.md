---
title: 🔮 Artificial Intelligence yesterday, today and tomorrow

# https://sli.dev/resources/theme-gallery
theme: seriph

layout: intro
class: text-center

# https://sli.dev/features/drawing
drawings:
  enabled: true
  persist: false

# slide transition: https://sli.dev/guide/animations.html#slide-transitions
transition: fade

# enable MDC Syntax: https://sli.dev/features/mdc
mdc: true
---

# 🔮 Artificial Intelligence <br>🏯 yesterday, 🕒 today and tomorrow 🚀

<br>

© 2024 by [Michael Vorburger.ch](https://www.vorburger.ch) (presenting in personal capacity and not representing employer)

Content licensed under [Creative Commons Attribution-ShareAlike 4.0 International](https://creativecommons.org/licenses/by-sa/4.0/?ref=chooser-v1).

_The source code of this presentation is [available on GitHub!](https://github.com/vorburger/LearningMachineLearning/tree/develop/docs/prez)_

<!--
I'll speak fast, let's chat together about questions during the breaks?
-->

---
layout: image
image: /images/google-gemini.png
backgroundSize: contain
---

# 🫢

<!--
How does this work? What does this mean for the future?

Prompt: _Can you make this sound cooler?_

_Michael Vorburger has been fascinated by the creative power of computers from an early age. He is an avid hacker by night, see https://www.vorburger.ch, and currently works on ML technical infrastructure in management for Google by day. He is presenting at this event in his personal capacity, not representing his employer._

::right::

# Output 🫢

How does this work? What does this mean for the future?

_By night, Michael Vorburger transforms into a digital alchemist, coaxing unseen potential from the very ones and zeros that form our world. An avid hacker with a website that whispers secrets of the craft (https://www.vorburger.ch), he spends his days architecting the intricate machinery of Machine Learning infrastructure for Google. While tonight, he sheds his corporate cloak to share his personal visions, untethered and electrifying._
-->

---
layout: quote
---

_“AI is one of the most important things humanity is working on. It is more profound than (...) electricity or fire."_

Sundar Pichai, Google CEO, [2018](https://www.cnbc.com/2018/02/01/google-ceo-sundar-pichai-ai-is-more-important-than-fire-electricity.html).

<br/>

_"It really was a huge surprise, when, in 2022, **AI woke up**."_

Bill Gates, in his _What's Next?_ (Netflix)

<br/>

❓ What do _you_ think?

---
layout: image
image: /images/wordcloud.svg
backgroundSize: contain
---

<!--
https://www.jasondavies.com/wordcloud/
-->

---

# History 🏯

<br>

_Artificial Intelligence_ (AI) arguably [started in 🏺 antiquity](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence).

_[Modern day AI](https://en.wikipedia.org/wiki/Outline_of_artificial_intelligence)_ from ~1960s, with emergence of Computer Science.

Initially 🔣 _"[symbolic](https://en.wikipedia.org/wiki/Symbolic_artificial_intelligence)"_ with _"rules",_ e.g. _Expert Systems_ à la [Cyc](https://en.wikipedia.org/wiki/Cyc); AI ❄️ Winters.

_Machine Learning_ (ML), with _Deep Learning_ for _Generative AI_ are subfields of AI - with a different take; why?

<!--
To give you a timeline, a scientific paper that is often referred to as a breakthrough milestone is the Transformer's by Researchers at Google, published (only) in 2017.

But let's take a quick detour...

* https://arxiv.org/abs/1706.03762
* https://proceedings.neurips.cc/paper_files/paper/2017/file/3f5ee243547dee91fbd053c1c4a845aa-Paper.pdf
* https://research.google/blog/transformer-a-novel-neural-network-architecture-for-language-understanding/
* https://www.wired.com/story/eight-google-employees-invented-modern-ai-transformers-paper/
-->

---
layout: fact
---

# What is _programming ❓_

---

# What is _programming?_

<br>

Programming is to give computers (very) precise instructions, AKA _"Code",_ for what you want them to do, like:

- Print `hello, world`
- Variable `i = 7`
- `if` i is still 7 `then` _do-that_
- `for` loop 7 times

Written in a computer language - try out [Scratch](https://scratch.mit.edu), it's great to learn concepts!

<small>(Or C++ or Java & Kotlin or C# or Python or JavaScript & TypeScript or Go or Rust, etc.)</small>

---
layout: fact
---

# How did you learn your mother tongue?

---
layout: two-cols-header
---

# How _did_ you learn your mother tongue?

::left::

## a)

I 👶 was 💻 _programmed_ by being 🍼 fed many 🔪 chopped up grammar and vocabulary 📖 books, and thus learned syntax and semantics to sound smart!

::right::

## b)

I 🐤 babbled incoherently for **years**, until, after _a lot of_ visual 😙 and 👂 audio cue _reinforcements,_ I **finally** figured out how to make sense!

<!--
Quick show of hands... who a) ... who b) ❓ 😆
-->

---

# Machine Learning (ML)

The idea of ML is ~ just to treat computers as 👶 babies, instead of _programming_ them! For example:

- Chess through _trial & error_ - instead _rules_
- _Vision_ with example images - instead of _algorithms_
- _Machine translation_ by "reading" human translated books - instead grammar
- _Large Language Models_ (LLM) by "reading" _A LOT_ of text, and then reply to prompts

The basic idea is not that new ([backpropagation](https://en.wikipedia.org/wiki/Backpropagation) ~1980s?), but it turned out to be a lot more 🚀 _"fun"_ with the emerging increasing availability of _Big Data_ and massive cloud storage & super compute cluster infrastructures, starting ~2010s.

---
layout: center
---

# Magic?

Is ML 🪄 magic? Not at all... the basic idea is really quite simply, actually! To illustrate:

🏫 Remember? `y = a*x + b` 🧮

Given a _training data set_ of some _points_ (x,y) representing car fuel efficiency,

where X is car weight an Y is KMs per Liter of Gas...

...find `a` and `b` - and that's a (2D) ML model, of 2 parameters!

Given car's _weight_ (X), you can _predict_ its gas consumption (Y).

---
layout: image
image: /images/car-data-points-with-model.png
backgroundSize: contain
---

<!--
Picture says more than words? But how did we find the a & b parameter...
-->

---
layout: image
image: /videos/linear_regression.gif
backgroundSize: contain
---

<!--
We literally just make a computer program try out values for a and b, to try to make the model have "good accuracy" - in this case, that just means "making the red line as close to those green points as it can be".

A large language model really is (kind of) similar to this - except that instead of have 2 parameters, for a and b, it has more - many more...

Copyright © 2020-2021 Gajanan Bhat. All rights reserved.

<https://gbhat.com>
-->

---
layout: image
image: /videos/Multi-Linear Regression Model Visualization.gif
backgroundSize: contain
---

<!--
... imagine, that instead of only having to find x2 parameters, a & b, for X car weight and Y gas (or 🔋 electricity!) consumption, you need more parameters, e.g. for Pie Sales, Price, and Advertising cost?

PS: This is technically mathematically not entirely accurate (because it's not really about spatial dimensions, but function parameters; really a quadratic or N polynomial function on 2-D X & Y would in a sense be more accurately making this point) - but this is a just a better visual illustration! ;-)

<https://github.com/rafiag/DTI2020/blob/main/images/Multi-Linear%20Regression%20Model%20Visualization.gif>
-->

---

# GenAI ML Models

GenAI ML Models really are just such parameters...

... except that a real LLM is _a little bit_ bigger!

E.g. [Google's open source Gemma](https://ai.google.dev/gemma) (v2) has **27 billion** 👍 parameters!

(And [Google's Gemini Models](https://deepmind.google/technologies/gemini/) are even bigger.)

💬 Words to 1️⃣2️⃣3️⃣ numbers & 🧮 _prediction!_

Or 🗣️ voice. Or 🖼️ images. Or 🎥 videos.

Often _Pipelines_ of \* N models.

<!--
Instead of just 2 or 3 such parameters, as seen previously.

In reality often not just 1 model, but Pipelines with Workflows connecting several models.
-->

---
layout: two-cols-header
---

# Training & Inferring

Separate phases

::left::

_Training_ is **creating** _ML Models_

of _Parameters_ - from input training data.

Effort (~) proportional to size of input data.

<br/>

_Finding `a` & `b` etc. (**27B!**) parameters._

::right::

_Inferring_ (AKA _serving)_ is giving a model new

(unseen) input, asking it to _"infer"_ output.

Effort is (comparatively) much smaller.

<br/>

_Calculating `Y` given `X`, having `a` & `b`._

<!--
Pictures of digits, cats & dogs, or texts...

📱 Mobile Phones can ✨ do (~) inference locally.

No ☁️ Cloud (DC) is more 🔏 #private & #fast.
-->

---

# Training Data

<br>

You need a massive amount of text of images or video to train Large Models with billions of parameters...

... and there are some interesting open questions around this.

---
layout: image
image: /images/TPU_v5L_Pod_-_Front_View_-_Web.max-2600x2600.jpg
backgroundSize: contain
---

---

# Cloud? Open Source?

ChatGPT & Google Gemini etc. run in the ☁️ Cloud.

You can download e.g. Google's Gemma, Meta's Llama, Mistral, etc. to run them yourself "at home".

Do try e.g. 🦙 [Ollama](https://ollama.com) to run an [LLM @ Home on a GPU](https://github.com/vorburger/vorburger.ch-Notes/blob/develop/ml/ollama1.md).

PS: Training is still proprietary - it's hard to DIY.

---

# Personalized LLM

Large Models might know about "the world", not (yet) "your world"... but:

- Huge prompts _("context window size")_ to "chat with your PDFs" works; try e.g. [NotebookLM](https://notebooklm.google)!

- _Fine Tuning_ is another ML technique to efficiently adapt a previously pre-trained model with new data.

- _"Workflows"_ (e.g. LangChain's LangGraph, et al.)

---
layout: image
image: /images/star-trek-scotty.gif
---

---

# The Future?

Artificial general intelligence - AGI? Superintelligence?

Not super clear what exactly _"AGI"_ really means...

Generally used as ~ _"[it can do some of your work](https://en.wikipedia.org/wiki/Artificial_general_intelligence#Tests_for_human-level_AGI)"._

_Matrix_ of 🤖 _Terminator_ taking ☠️ over?

More like 🧠 humans' latest 🛠️ tool...

Jobs will change, yes - but haven't they always? 🐎

The next few years are going to be very interesting!

<!--
I didn't come here with a horse carriage, like I would have just a 100 year ago; and we don't have coachmen anymore, we didn't need that job anymore.

But in the bright side, there A LOT of new jobs nowadays which didn't exist 100 years ago.

Turing Test, Robot College Student Test, Employment Test, Ikea Test, Coffee Test, Modern Turing Test
-->

---
layout: image
image: /images/KITT_Speaks_Spanish_Knight_Rider-ezgif.com-video-to-gif-converter.gif
---

---

# Applications

- 💬 Chat Bots, [Image](https://huggingface.co/spaces/nyxai-lab/perspectives-on-ai) & [Movie Generation](https://www.youtube.com/@aicinemaof)
- 💻 Coding: E.g. GitHub Copilot (and others)
- 🏢 Productivity: E.g. documents, email summary; or Meeting Minutes transcription
- ⚕️ **Health:** E.g. [Google's Health AI](https://ai.google/discover/healthai/) for breast cancer 🩻 [screening](https://www.youtube.com/watch?v=CzgMUVPduZA) or expanding access to ultrasound
- ⚛️ **Science:** E.g. Google DeepMind's 🧬 [AlphaFold](https://www.youtube.com/watch?v=gg7WjuFs8F4) (open [access](https://alphafoldserver.com/)), or 🧮 [Math](https://deepmind.google/discover/blog/ai-solves-imo-problems-at-silver-medal-level/) 🏅 Olympiad
- 🎒 **Education:** E.g. [Khan Academy's Khanmigo](https://www.youtube.com/watch?v=hJP5GqnTrNo&t=4s), or Homework with [Google Lens](https://lens.google)
- Deepfakes & misinformation spam - **and** their detection

Is (some of) this _"creative"?_ You tell me...

<!--
AlphaFold "protein folding" breakthrough unlocking research of new medicines

AlphaProof & AlphaGeometry solved 4 / 6 problems from this year’s International Mathematical Olympiad (IMO);
https://www.theguardian.com/technology/article/2024/jul/25/google-deepmind-takes-step-closer-to-cracking-top-level-maths

Khan also e.g. https://www.youtube.com/watch?v=_EfEoSP7oYQ (after aforementioned TED Talk)

TODO Try Google Lens with Homework & screenshot it
-->

---
layout: image
image: /images/alphafold.png
backgroundSize: contain
---

---

# Gaps?

It's still early days. But more is coming - and (very) quickly...

- _Explainable Neural Networks (XNNs)_
- Grounding in Facts, to cure Hallucinations (e.g. LLM + KB/KG with RAG; or [_"neuro-symbolic"_](https://en.wikipedia.org/wiki/Neuro-symbolic_AI))
- More Multi Modal, and Sensing ([watch Project Astra](https://deepmind.google/technologies/gemini/project-astra/)!) #latency
- Interacting with Our World (Web, APIs)
- New UX? Knowledge agent design?

<!--
Combining Large Language Models (LLMs) with Knowledge Graphs (KGs) and Retrieval-Augmented Generation (RAG) looks promising.

You would be surprised how difficult it is to build an Assistant that can buy movie tickets or make restaurant reservations only.

Something like Gemini's Extensions, to connect it to your Gmail & Google Docs, Google Maps or Flights, or YouTube are only the very early beginning.
-->

---
layout: image
image: /videos/Optimism-Captain.webp
backgroundSize: contain
---

<!--
To quote Dr. Phlox, from Star Trek: "Optimism, Captain!"

# Optimism

<SlidevVideo v-click autoplay controls>
  < ! -- Anything that can go in an HTML video element. - - >
  <source src="/videos/Optimism-Captain.mp4" type="video/mp4" />
  <p>
    Your browser does not support videos. You may download it <a href="/videos/Optimism-Captain.mp4">here</a>.
  </p>
</SlidevVideo>
-->

---

# You?

Machine Learning is a lot of fun! Get started with exploring it today:

1. [`gemini.google.com`](https://gemini.google.com) to learn _"Prompt Engineering"_
1. [Google AI Explorables](https://pair.withgoogle.com/explorables/)

For developers:

1. [ML Zero to Hero x4 ~6' (=24') Videos](https://www.youtube.com/playlist?list=PLQY2H8rRoyvwWuPiWnuTDBHe7I0fMSsfO)
1. [Google Machine Learning Crash Course](https://developers.google.com/machine-learning/crash-course)
1. [TensorFlow Quickstart](https://www.tensorflow.org/tutorials/quickstart/beginner)
1. [TensorFlow Learn ML](https://www.tensorflow.org/resources/learn-ml)
1. [Google AI Build](https://ai.google/build)

More on [LearningMachineLearning](https://github.com/vorburger/LearningMachineLearning/blob/develop/docs/resources.md) - contributions welcome.
