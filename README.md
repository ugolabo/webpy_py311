# webpy_project

A little Python site using the web.py framework.

Based on Exercise 52, from [Learn Python the Hard Way](http://learnpythonthehardway.org) by Zed Shaw, with a couple of bells and whistles.

- Project name: webpy_project (the parent directory).
- Website title: Starship Survival.
- The project runs on Python 2.7.
- Add the [web.py](http://webpy.org/install) package to Python (`pip install web.py==0.37`); other versions will not work.
- Clone the project; on your PC, the project directory must be organized as follow.

```text
└───webpy_project
    ├───bin
    ├───docs
    ├───gothonmap
    ├───sessions
    ├───static
    │   ├───css
    │   └───img
    └───templates
```

- The 'bin' subdir contains the script `app.py`, the engine. The engine refers to a map or story, in the 'gothonmap' subdir, and renders the website with the HTML templates, in the 'templates' subdir. The HTML templates are prettified with the 'static' subdir. web.py needs to account for sessions ('sessions' subdir). The 'docs' subdir is simply for documenting the project.
- In your terminal, at the 'webpy_project' level, launch the website with `python2 bin/app.py`.
- The terminal or the shell will show a local IP address: `http://localhost:8080`.
- Copy and paste this address in your browser to experience the website.
- If the Python script fails to launch the website, you might have a path problem; you must set the path for the project to execute.
- For Linux/Mac OS X users, please execute in the terminal:

```bash
export PYTHONPATH=$PYTHONPATH:.
```

- For Windows users, please execute in the shell:

```bash
$env:PYTHONPATH = "$env:PYTHONPATH;."
```

- Or set the path with Windows Advanced Systeme Parameters (consult the documentation for that matter).
- Then relaunch the script; `python2 bin/app.py` works on Linux/MacOSX.
- For Windows, you might need to try `py -2 bin/app.py` or `py -2.7 bin/app.py`.
- Consult the Python documentation otherwise.
- The site can also be hosted and run online.
    - Here is a bonified version: https://ugoproto.pythonanywhere.com/game
- Have fun!
