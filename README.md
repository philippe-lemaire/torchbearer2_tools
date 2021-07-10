# Intro
This is a set of tools to help understand and run the upcoming table top RPG Torchbearer 2nd Edition by Thor Olavsrud and Luke Crane.

# Startup the project

The initial setup.

Create virtualenv and install the project:
```bash
sudo apt-get install virtualenv python-pip python-dev
deactivate; virtualenv ~/venv ; source ~/venv/bin/activate ;\
    pip install pip -U; pip install -r requirements.txt
```

Unittest test:
```bash
make clean install test
```

```bash
##   e.g. if group is "{group}" and project_name is "torchbearer2_tools"
git remote add origin git@github.com:{group}/torchbearer2_tools.git
git push -u origin master
git push -u origin --tags
```

Functionnal test with a script:

```bash
cd
mkdir tmp
cd tmp
torchbearer2_tools-run
```

# Install

Go to `https://github.com/{group}/torchbearer2_tools` to see the project, manage issues,
setup you ssh public key, ...

Create a python3 virtualenv and activate it:

```bash
sudo apt-get install virtualenv python-pip python-dev
deactivate; virtualenv -ppython3 ~/venv ; source ~/venv/bin/activate
```

Clone the project and install it:

```bash
git clone git@github.com:{group}/torchbearer2_tools.git
cd torchbearer2_tools
pip install -r requirements.txt
make clean install test                # install and test
```
Functionnal test with a script:

```bash
cd
mkdir tmp
cd tmp
torchbearer2_tools-run
```
