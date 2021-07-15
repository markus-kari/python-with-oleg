Here will be the projects Oleg instructs me to do.
VSC will be linked.
# This is a fun comment! This shall be merged!


# Next: Virtual environnements =)
## Installing Pipenv
https://www.pythontutorial.net/python-basics/install-pipenv-windows/

## Dont forget to change "username" (need admin rights)
[Environment]::SetEnvironmentVariable("Path", $env:Path + ";c:\Users\username\AppData\Roaming\Python\Python38\Site-Packages", "Machine")
[Environment]::SetEnvironmentVariable("Path", $env:Path + ";C:\Users\username\AppData\Roaming\Python\Python38\Scripts", "Machine")
[Environment]::SetEnvironmentVariable("PIPENV_VENV_IN_PROJECT", "1", "Machine")

## Creating Virtual environnement
```ps
pipenv install
```

-> Creates folder ".venv"
    a copy of python interpreter and all your installed modules go in there
-> Creates Pipfile
    Its like a directory of your installed modules
-> Creates Pipfile.lock
    It describes exact version of modules installed by pipenv


## activating environnement
```ps
pipenv shell
```

## installing modules
```ps
pipenv install uvicorn
pipenv install starlette
```

## running example
```ps
uvicorn example:app --reload
```

done for the first part =)

# Next Task make a simple login thing
