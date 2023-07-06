# ATS (all the stuff) Study
<p align="center">
    <a href="#Subject">Subject</a>  |
    <a href="#Artifacts">Artifacts</a> |
    <a href="#TechReport">Tech Report</a> |
    <a href="#Problem">Problem</a> |
    <a href="#Collaborate">Collaborate</a> |
    <a href="#Journal">Journal</a>
</p>

<span id="Subject">

## Subject 🏆️

- So this is a repo where I try to do the code thing "right" (using the whole scope of good practices).

- I'm testing if the gains are actually good enough for using those as rules when developing software.

- I'll try to leave notes onto the README so you can take my experience somehow and create your own opinions about this subject.

- Enjoy!



<span id="Artifacts">

## Artifacts 📋️
> What is a good delivery?

- Reliable Version Management

  - Concise Commits
  - Issue referencing

- CI (continuous integration) routines

  - Auto-formatting
  - Test running
  - Documentation export

- Documentation

  - OpenAPI Docs
  - Docstring Docs

- Logging

  - Trace and store events when needed

- Portability

  - Easily build and run the application in other environment

- Publish

  - Manage to somehow make this available when in a "stable" state



<span id="TechReport">

## Technologies Report 💻️

> To achieve all the artifacts, what technology will be used?
>
> **NOTE**: Those may not be the best technologies for the use cases but I'm trying to setup a environment that can be replicated in my daily activities. Real life stuff 🥱

- Version Management
  - Git + GitHub (same as always)

- CI
  - GH Actions (better for no cloud investment)
  - Black, Flake8 and Pre-Commit routines
  - Pytest for testing

- Web
  - Fastapi (Async support + Automatic Swagger Documentation)
 
- Docs
  - [pdoc](https://pdoc3.github.io/pdoc/)

- Logging

  - Python logging built in library

- Portability

  - Docker

- Publish

  - I don't really now, maybe DockerHub


<span id="Problem">

## The problem 🐙

> Ended up realizing I need something to fix

- A Backend and CLI application for Task Management that generates stats about time invested in the tasks.
- It will work as Server and Client and will generate stats that will help the user trace their efforts by categories and etc.



<span id="Collaborate">

## Collaborate 🤝

> Want to go fast? Go alone. Want to go far? Go together.

- You can Collaborate with this project!

- Just make a fork, any PR will be reviewed and maybe implemented

- Any appointed issue will be considered



<span id="Journal">

## Journal ✍️

> Documentation of every obstacle in the way

#### The start

- Don't know where to begin
- I'll break some initial features
- Just wrote some issues in a Github Project, the first chapter, Hello World!

#### End of the first chapter

- After something like 4 hours in and more 5 or 6 of alternatives study I ended with a base setup of tools that is a little different from the one I thought in a first moment.
- I replaced the Flask framework for Fastapi for its capabilities in OpenApi automatic documentation and asynchronous support.
- The CI pipeline that I aimed for was Jenkins but I found it kinda strange to run in a local machine and so I choose the GH Actions that have exceeded my expectations and handled the whole thing very well.
- My opinions still the same at this point. The difference I felt the most was that the initial setup had a heavier investment of time and effort that actually seems to pay off but haven't yet.
- I'll need to make a front-end for this, f*ck!