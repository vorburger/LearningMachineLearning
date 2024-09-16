---
title: 🔮 Artificial Intelligence yesterday, today and tomorrow

# https://sli.dev/resources/theme-gallery
theme: seriph

layout: center
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

# 🔮 Artificial Intelligence <br>yesterday, today and tomorrow

<br>

© 2024 by [Michael Vorburger.ch](https://www.vorburger.ch) (presenting in personal capacity and not representing employer)

Content licensed under [Creative Commons Attribution-ShareAlike 4.0 International](https://creativecommons.org/licenses/by-sa/4.0/?ref=chooser-v1).

_The source code of this presentation is [available on GitHub!](https://github.com/vorburger/LearningMachineLearning/tree/develop/docs/prez)_

<!--
I'll speak fast, let's chat together about questions during the breaks?
-->

---

# Agenda

<!-- TODO Find MD tool to extract and auto update insert TOC from headings, or make https://sli.dev/builtin/components#toc work -->

- The Past
- The Present
- The Future
- You?

---
layout: center
---

# Pop Quiz

What is _programming ❓_

---

# Interlude: What's _programming?_

Programming is to give computers (very) precise instructions, AKA _"Code",_ for what you want them to do, like:

- Print `hello, world`
- Variable `i = 7`
- `if` i is still 7 `then` _do-that_
- `for` loop 7 times

Written in a computer language - try out [Scratch](https://scratch.mit.edu), it's great to learn concepts!

<small>Or C++ or Java & Kotlin or C# or Python or JavaScript & TypeScript or Go or Rust.</small>

---

# The Past

_Artificial Intelligence_ (AI) started in the 1960s, and is a broad CS research field.

_Machine Learning_ (ML) is a subfield of AI specifically about

---

# The Present

_Large Language Models_

---

# Training & Inferring

- _Training_ is creating said _ML Models_ of _Parameters_ (from input data)
- _Inferring_ (AKA _serving)_ is giving a model new (unseen) input, to ask it for _"inferred"_ output

Training effort is (somewhat) proportional to size of input data.

Inferring effort is (comparatively) much smaller. Your (modern) Mobile Phone can do it!

<!--
Pictures of digits, cats & dogs, or texts...
-->

---

# What Data?

massive

web

There are some interesting open questions about this.

---

# Applications

- Coding: E.g. GitHub Copilot (and many others)
- Education: E.g. [Khan Academy's Khanmigo](https://www.youtube.com/watch?v=hJP5GqnTrNo&t=4s), or Homework with [Google Lens](https://lens.google)

<!--
TODO Try & screenshot
-->

---

# Personalized LLM

Large Models might know about "the world", but not "your world"... but:

- Creating _huge prompts_ works great, AKA "Chat with your PDFs"; try e.g. [NotebookLM](https://notebooklm.google).

- _Fine Tuning_ is another ML technique to efficiently adapt a previously pre-trained model with new data.

- _"Workflows"_ (e.g. LangChain's LangGraph, et al.)

---

# Cloud? Open Source?

ChatGPT & Google Gemini etc. run in the ☁️ Cloud.

But you can download Google's Gemma, Meta's Llama, Mistral, etc. to run them locally.

Do try e.g. 🦙 [Ollama](https://ollama.com) to run an [LLM @ Home on a GPU](https://github.com/vorburger/vorburger.ch-Notes/blob/develop/ml/ollama1.md).

PS: Their training is still proprietary - it's hard to DIY.

---

# The Future

Artificial general intelligence - AGI?

Not super duper clear to anyone what exactly this really means... 😄

Generally colloquially used as ~ _"[it can do some of your work](https://en.wikipedia.org/wiki/Artificial_general_intelligence#Tests_for_human-level_AGI)"._

We'll see; the next few years are going to be very interesting!

<!--
Turing Test, Robot College Student Test, Employment Test, Ikea Test, Coffee Test, Modern Turing Test
-->

---

# Gaps? #TBD

- Grounding in Facts, to cure Hallucinations (e.g. LLM + KB/KG with RAG)
- More Multi Modal, and Sensing ([watch Project Astra](https://deepmind.google/technologies/gemini/project-astra/)!)
- Interacting with Our World (Web, APIs)

<!--
Combining Large Language Models (LLMs) with Knowledge Graphs (KGs) and Retrieval-Augmented Generation (RAG) looks promising.

You would be surprised how difficult it is to build an Assistant that can buy movie tickets or make restaurant reservations only.

Something like Gemini's Extensions, to connect it to your Gmail & Google Docs, Google Maps or Flights, or YouTube are only the very early beginning.
-->

---

# You?

Machine Learning is a lot of fun! Get started with exploring it today:

1. [`gemini.google.com`](https://gemini.google.com)
1. [Google AI Explorables](https://pair.withgoogle.com/explorables/)

For developers:

1. [ML Zero to Hero x4 ~6' (=24') Videos](https://www.youtube.com/playlist?list=PLQY2H8rRoyvwWuPiWnuTDBHe7I0fMSsfO)
1. [Google Machine Learning Crash Course](https://developers.google.com/machine-learning/crash-course)
1. [TensorFlow Quickstart](https://www.tensorflow.org/tutorials/quickstart/beginner)
1. [TensorFlow Learn ML](https://www.tensorflow.org/resources/learn-ml)
1. [Google AI Build](https://ai.google/build)

More on [LearningMachineLearning](https://github.com/vorburger/LearningMachineLearning/blob/develop/docs/resources.md)...
