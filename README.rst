Work In Progress... TBC

=============
 ChartIt App
=============

This is an example application, a tutorial on putting together a decent
quality python web app. It explains step by step what's being done but
more importantly, why an action is taken.

You will find step by step's for cloning this project repository and using
it as a foundation to build your own python web application on top of as
well as helpful guidance on what to do at each step of the way in
developing your new app.


--------------
 Introduction
--------------

As a long term "ops guy" making the transition into the development world,
it's been useful for me to compile a simple example application that
covers state-of-the-art (2012/2013) python web development practices.

This is a broad topic, covering both the tools and workflow involved. For
me, the more insightful side is the workflow, but it's necessary to
describe the tools in order to cast light on a good quality workflow.


-----------------
 What's Covered?
-----------------

I mentioned a good quality workflow, for the purpose of this tutorial that
encompasses:

* Test Driven Development
* Workflow Automation
* Documentation
* Tooling

It encompasses a whole lot more in practice. However (excellent) books such
as Code Complete by Steve McConnell are a much better source than I can be
for insight into designing and implementing quality software.

The following tools are used to develop this application.

* `Bottle.py Micro-Framework <http://bottlepy.org/>`_
* `Fabric Automation <http://fabfile.org/>`_
* `Google App Engine <https://developers.google.com/appengine/docs/python/>`_
* `Sphinx Documentation <http://sphinx-doc.org/>`_
* `Nose Testing Framework <https://nose.readthedocs.org/en/latest/>`_
* `WebTest <http://webtest.pythonpaste.org/en/latest/>`_
* `Jenkins Continuous Integration <http://jenkins-ci.org/>`_
* `Python Virtual Env <http://www.virtualenv.org/en/latest/>`_
* `Virtual Env Wrapper <http://www.doughellmann.com/projects/virtualenvwrapper/>`_
* `IPython Shell <http://ipython.org>`_
* `Git Flow <http://nvie.com/posts/a-successful-git-branching-model/>`_

You can see a lot of current buzz-words in this list, which my sage
"ops guy" experience warns me is a sure sign this is all complete
bullshit. Buyer beware ;-)


-----------------
 Getting Started
-----------------

1.  I will assume you are starting with an empty repository, but you could
    save time by forking this repository and ammending it to suit your
    project, in which case you can skip the next steps.
2.  Create a git repository ``git init chartit`` then ``cd chartit``
3.  Add a file to get started, a readme file is normally a good shout for
    any new project ``touch README.rst`` this is ReStructuredText format
    which is less common currently than Markdown. However, RST is the
    most common Python documentation format and is well supported on
    GitHub.
4.  Next "stage" this README by doing ``git add .`` which says add
    everything in this dir, recursively. Although there is only 1 file
    currently, this will be handy knowledge later. Lastly commit the
    change with ``git commit -m 'Initial commit on ChartIt project'``
5.  We are following the git flow methodology for version control,
    therefore before we commence any real development effort, we must
    first create and switch to a development branch, which is one
    command: ``git checkout -b develop``
6.  We need to add a feature to the mainline develop branch, so let's 
    branch off of develop to contain this work:
    ``git checkout -b projectsetup develop``
7.  Next we'll populate the files necessary to launch a basic site in the
    App Engine development webserver.


-------------------
 Environment Setup
-------------------

This work item, or feature branch, will deliver a working basic app.
Ensure you have the `Python Google App Engine SDK <https://developers.google.com/appengine/downloads?hl=pt-br#Google_App_Engine_SDK_for_Python>`_ installed
locally. Also ensure you have the python virtualenv and virtualenvwrapper
tools installed. I am developing on a Mac so i will use the Python packaging
tools directly, on linux i may have used the distribution packaging tools
instead::

    $ easy_install virtualenv virtualenvwrapper
        # You must add a line to your bash / zsh / whatever .rc file, see
        # virtualenvwrapper documentation for assistance completing
        # installation.

Create a virtualenv for this project's development dependencies::

    $ mkvirtualenv chartit
    $ lsvirtualenv
    $ workon chartit    # Not necessary here, just demonstrating it's
                        # possible to switch between projects

Create the initial project structure in your repository working directory.
We are currently on the "projectsetup" branch:

*   app.yaml: Copy from this project, edit the "application:" line,
    everything else can remain.
*   index.yaml: Copy as-is from this project
*   ``mkdir application`` then ``touch application/__init__.py``

Stage our changes so far: ``git add .`` we can verify current status
with ``git status``, next commit our progress with:
``git commit -m 'Added initial App Engine configuration and structure.'``

Now to install the bottle.py microframework and create the app handler:

*   bottle.py: Get the latest rather than the PyPI version, get it from
    https://raw.github.com/defnull/bottle/master/bottle.py


Edit ``application/__init__.py`` to look like::

    """
    ChartIt: A tutorial case study for python web development.

    .. moduleauthor:: Craig J Perry, <craigp84@gmail.com>

    """

    import os
    import bottle
    from application.app import app


    def in_gae_production():
        """As per `App Engine Docs <https://developers.google.com/appengine/docs/python/runtime#The_Environment>`_
        the ``SERVER_SOFTWARE`` env var contains "Google App Engine" in production.
        :returns: True when running on Google App Engine production
        """
        return True if "Google App Engine" in os.environ.get('SERVER_SOFTWARE', '') else False


    if not in_gae_production():
        bottle.debug(True)

    bottle.run(app=app, server='gae')


Edit ``application/app.py`` to look like::

    #!/usr/bin/env python

    """
    .. module:: app
        :platform: Google App Engine, GAE Dev Server
        :synopsis: Home of the main application logic

    .. moduleauthor:: Craig J Perry <craigp84@gmail.com>

    """

    from bottle import Bottle


    app = Bottle()


    @app.route('/', method='GET')
    def setup_complete():
        return "Environment Configured Correctly."

Here we have used Sphinx markers in the docstrings. We haven't bothered in
the ``setup_complete()`` method as it is only temporary to prove the env
works.

Now we are ready to launch the app in the dev server and ensure everything
works.

1.  ``deactivate`` to get rid of the virtualenv, this is only used for
    development dependencies but not during runtime or deployment.
2.  ``dev_appserver.py .`` then visit http://127.0.0.1:8080

Assuming this works, we've completed our feature in our git flow. Time to
check in:

1.  ``git status`` reveals some files we don't want to check-in: .pyc
2.  ``echo "*.pyc" > .gitignore``
3.  ``git add .`` then
    ``git commit -m 'Got basic app running in app engine dev server.'``

Ok, we've completed our first feature. Time to merge this branch in to the
main develop branch.

1.  ``git checkout develop``
2.  ``git merge --no-ff projectsetup`` Add a decriptive multi line comment
    about what this achieves and why it is being merged.
3.  Delete the now complete feature branch: ``git branch -d projectsetup``
4.  We should now push our changes upstream to the shared repository


------------------------------------------
 Setting Up A Shared (Private) Repository
------------------------------------------

Now that we have the basic project off the ground, we should share the
repository with the other developers in our team. I will be using a
Virtualbox instance running a flavour of Linux, but this could easily
be a real machine or an EC2 instance etc.

The host has had a user "gitrepos" added and the git toolset installed.

In my case on a vanilla Ubuntu 12.10 instance i did the following:

1.  ``sudo apt-get install git``
2.  ``sudo adduser --disabled-password gitrepos``
3.  ``sudo -u gitrepos -i``
4.  ``mkdir .ssh`` and ``touch .ssh/authorized_keys``
5.  ``git init --bare chartit.git``

On the local development machine, in my case my laptop:

1.  Push my ssh key to the gitrepos@devbox.local user's authorized_keys file:
    ``cat .ssh/id_rsa.pub | ssh gitrepos@server 'cat - >> .ssh/authorized_keys'``
2.  Now i can add the remote git repository:
    ``git remote add origin ssh://gitrepos@devbox.local/home/gitrepos/chartit.git``
3.  Now i can publish: ``git push origin master`` this branch contains nothing
    yet, but develop does: ``git push origin develop``

In line with the principle of least-privilege, i will restrict this user's
shell since multiple developers will have ssh login access here yet they
don't need shell access to this account.

1.  As gitrepos user ``mkdir git-shell-commands``
2.  As root user ``echo /usr/bin/git-shell >> /etc/shells`` then
    ``chsh -s /usr/bin/git-shell gitrepos``

-------------------
 Adding Unit Tests
-------------------

We have the basic environment setup, and we have a shared repository for
other developers to contribute to. Now before we crack on with implementing
the first feature (display a home page) we need a unit test to describe
the expected behaviour.

1.  Switch to our virtualenv, which captures all our development
    depedencies on this project: ``workon chartit``
2.  Install nose and some static analysis tools which will give us some
    insight into the quality of our code:
    ``pip install nose nosexcover coverage pep8 pylint``
2.1 Nose finds and runs unit tests, it produces XUnit compatable
    reports which we will use with Jenkins reporting later
2.2 NoseXCover produces Cobertura like xml output of test coverage reports.
    Again we will use this with Jenkins to produce graphical reports.
2.3 Coverage is the acutal test coverage checking tool. It allows us to
    guage the completeness of our unit tests.
2.4 pep8 provides hints and warnings if the written Python code breaks
    conventions in the PEP8 standards document
2.5 PyLint is a static analysis and code quality monitoring tool. It will
    highlight problematic code.
3.  Create a tests directory: ``mkdir application/tests``

Our tests will need some pre-run setup, specifically we need to ammend the
python sys.path to look in the correct dir for the modules under test.
Create a test module __init__.py file with the following content::

    """
    Package level test setup. Run once for the whole package.

    .. moduleauthor:: Craig J Perry, <craigp84@gmail.com>

    """


    import sys


    def add_to_path(path='..'):
        """Prepend a given path to the python sys.path.

        >>> add_to_path('../a_module')

        :param path: directory location relative to this file
        :type path: str"""
        sys.path.insert(0, path)


    def setup():
        """Package level test fixture setup."""
        add_to_path()


    def teardown():
        """Package level test fixture teardown."""
        pass

We can make a commit to cover the work thus far: ``git add .`` then
``git commit -m 'Added unit testing framework code.'``

Create a test file ``application/tests/test_app.py`` with these contents::

    """
    Unit testing of the app.py module.

    .. moduleauthor:: Craig J Perry, <craigp84@gmail.com>

    """


    from unittest import TestCase
    from application.app import home


    class TestHome(TestCase):
        """Testing inputs and behaviours of the home page handler."""

        def test_home_with_valid_params(self):
            """Ensure home handler responds with a complete html output given
            valid inputs."""
            result = home()
            self.assertTrue("</html>" in result)

Now by running nosetests in our virtualenv, we should see a complaint
about missing google app engine libraries. We could add the libraries to
our virtualenv via pip install but the libs are currently out of date
(v1.5.1 on PyPI vs. v1.7.3 from google direct).

For unit testing, we shouldn't be depending on external libraries. By
looking through the stack trace, we can see it's the bottle.run() call
which is causing bottle.py to try to import from GAE. Let's ammend
the application __init__.py to avoid this by not running this statement
during unit test runs::

    """
    ChartIt: A tutorial case study for python web development.

    .. moduleauthor:: Craig J Perry, <craigp84@gmail.com>

    """

    import os
    import sys
    import bottle
    from application.app import app


    def in_gae_production():
        """As per `App Engine Docs <https://developers.google.com/appengine/docs/python/runtime#The_Environment>`_
        the ``SERVER_SOFTWARE`` env var contains "Google App Engine" in production.
        :returns: True when running on Google App Engine production
        """
        return True if "Google App Engine" in os.environ.get('SERVER_SOFTWARE', '') else False


    def running_as_unittest():
        """Verify whether the current execution context is within a unit test run.
        :returns: True when invoked as part of a unit test"""
        return "nosetests" in sys.argv


    if not in_gae_production():
        bottle.debug(True)

    if not running_as_unittest:
        # Avoid complaints about missing GAE libs in virtualenv
        bottle.run(app=app, server='gae')

Now we should see something similar to the below error::

    (chartit)#2156[craig@craigs-macbook-pro chartit2]$ nosetests
    E
    ======================================================================
    ERROR: Failure: ImportError (cannot import name home)
    ----------------------------------------------------------------------
    Traceback (most recent call last):
      File "/Users/craig/.venvs/chartit/lib/python2.7/site-packages/nose/loader.py", line 390, in loadTestsFromName
        addr.filename, addr.module)
      File "/Users/craig/.venvs/chartit/lib/python2.7/site-packages/nose/importer.py", line 39, in importFromPath
        return self.importFromDir(dir_path, fqname)
      File "/Users/craig/.venvs/chartit/lib/python2.7/site-packages/nose/importer.py", line 86, in importFromDir
        mod = load_module(part_fqname, fh, filename, desc)
      File "/Users/craig/Development/1st/chartit2/application/tests/test_app.py", line 10, in <module>
        from application.app import home
    ImportError: cannot import name home

    ----------------------------------------------------------------------
    Ran 1 test in 0.030s

    FAILED (errors=1)

This is expected, we have a unit test but no implementation to satisfy it.
We can make a commit to cover the addition of the (failing) unit test which
describes the behaviour we want from the home function when it is added.

Now we can implement the home() function to satisfy the unit test. Amend
the app.py to look like::

    #!/usr/bin/env python

    """
    .. module:: app
        :platform: Google App Engine, GAE Dev Server
        :synopsis: Home of the main application logic

    .. moduleauthor:: Craig J Perry <craigp84@gmail.com>

    """

    from bottle import Bottle, template


    app = Bottle()


    @app.route('/', method='GET')
    def home():
        """The home page handler serves a static template."""
        return template('home')

This implementation renders a template named 'home.tpl' which is located
in the views/ directory. Add the views/ dir and put the below in home.tpl::

    %# The home page view / template
    <!doctype html>
    <html>
        <head>
            <title>ChartIt! Simple Charting Service</title>
        </head>
        <body>
            <h1>ChartIt!</h1>
            <p>A simple charting service on the network.</p>
        </body>
    </html>

Now running nostests passes. Also invoking the dev_appserver (outside of
the virtualenv) results in the expected response from the root url.

So far our directory structure looks like::

    chartit/
        .git/
        .gitignore
        app.yaml
        application/
            __init__.py
            app.py
            tests/
                __init__.py
                test_app.py
        bottle.py
        index.yaml
        requirements.txt
        README.rst
        views/
            home.tpl

The root dir of the project is starting to get cluttered. Later we will
move bottle.py into a lib/ subdir. We could also benefit from moving
just the files required for running on Google App Engine, moved under
a GAE dir::

    chartit/
        .git/
        .gitignore
        docs/
        requirements.txt
        README.rst
        gae-root/
            app.yaml
            application/
                __init__.py
                app.py
                tests/
                    __init__.py
                    test_app.py
            lib/
                bottle.py
            index.yaml
            views/
                home.tpl
        reports/
            coverage.xml
            nosetests.xml
            pylint.out
            pep8.out


----------------------------------
 Git Flow Recap - Merging Feature
----------------------------------

Time for another commit. This time we have completed a feature and can now
also push it up to the shared develop branch.

1.  ``git add .``
2.  ``git commit``
3.  ``git checkout develop``
4.  ``git merge --no-ff homepage``
5.  Remove the completed feature branch: ``git branch -d homepage``
6.  View the history of the develop branch with ``git log``
7.  We should sync with the upstream develop branch ``git pull develop``
    will perform a git fetch then a git merge for the develop branch. This
    would be the time any conflicts with the current HEAD are revealed, we
    can address the conflicts with other developer's changes before pushing
    up our changes. This practice helps to ensure a stable develop branch.
8.  ``git push origin develop``


------------------------
 Continuous Integration
------------------------

Now that we have our git workflow in place to allow working alongside
other developers, and we have our first feature in place (a place holder
home page!) we are ready for continuous integration.

Back on the development server, where i earlier hosted the git repo, i
will install Jenkins and its dependencies. You can do this manually:

1.  Install `Java <oracle.com>`_
2.  Install `Tomcat <http://tomcat.apache.org>`_
3.  Install `Jenkins <http://jenkins-ci.org>`_

Alternatively, install using your distribution's package manager.

Here are the steps i took to install manually on a vanilla Ubuntu 12.10
server instance:


 Shared DevBox Configuration
-----------------------------

I assume here you are using Ubuntu 12.10, however there is absolutely no
reason you cannot use another flavour of Linux, or even another OS altogether.

1.  ``sudo apt-get install avahi-daemon`` this will allow you to ssh to
    devbox.local (our your hosts name) without configuring a DNS server from
    a machine which supports Zeroconf / Bonjour, such as a Mac or another
    Linux host with avahi installed
2.  ``sudo apt-get install python-virtualenv virtualenvwrapper`` this will
    also pull down ``build-essential`` which is a useful collection of compilers
    and basic software building utilities. Logout and login again to have
    your shell gain virtualenvwrapper features such as ``lsvirtualenv`` and
    ``mkvirtualenv`` or ``workon``


 JDK Installation
------------------

1.  Downloaded the latest jdk from Oracle in .tar.gz format
2.  Extracted the archive with ``tar xzvf jdk.XXX.tar.gz``
3.  Moved the JDK into the correct place for Ubuntu: ``sudo mkdir /usr/lib/jvm``
    then ``sudo mv jdkXXXX /usr/lib/jvm``
4.  Updated the alternatives system to reflect the newly installed JDK. There
    were too many commands to do manually so i created a for loop in bash which
    filters out only the commands i wanted to register with the system::

    for cmd in /usr/lib/jvm/jdk1.7.0_09/bin/[jkpr]*; do
        cmd=$( basename $cmd )
        echo "Registering $cmd with the system alternatives mechanism..."
        sudo update-alternatives --install /usr/bin/$cmd $cmd /usr/lib/jvm/jdk1.7.0_09/bin/$cmd 1
    done

I used ``java -version`` and ``javac -version`` to confirm these were
setup correctly.

If this is not the only JDK installed on your Ubuntu server, you may run into
an unexpected version being returned in the above test, in that case you can
invoke ``sudo update-alternatives --config java`` and repeat for each command
(you could alter the above for-loop).


 Tomcat Installation
---------------------

1.  Create a user to host the Jenkins installation:
    ``sudo adduser --disabled-password jenkins``
2.  Download and unzip the latest Tomcat version in the jenkins user's home
    dir
3.  Created a ``.cron-env.sh`` file with env var: ``export JAVA_HOME="/usr/lib/jvm/jdk1.7.0_09"``
4.  Added a crontab entry for the jenkins user:
    ``@reboot ( . ~/.cron-env.sh; apache-tomcat-7.0.33/bin/startup.sh ) > apache-tomcat-7.0.33/logs/startup.log 2>&1``
    NB: This is less than ideal, there is no graceful shutdown on a server
    reboot. A better approach would be to use upstart.
5.  Edit apache-tomcat-7.0.33/conf/tomcat-users.xml and add in::

    <role rolename="manager-gui" />
    <user username="manager" password="manager" roles="manager-gui" />

6.  Restart tomcat, ensure you can now login with the details you configured at
    `tomcat <http://devbox.local:8080/manager/html>`_


 Jenkins Installation
----------------------

1.  Add the following env var to .cron-env.sh
    ``export CATALINA_OPTS="-DJENKINS_HOME=/home/jenkins/jenkins-ci -Xmx256m"``
2.  Download the jenkins .war file and deploy via the tomcat manager url
3.  Visit `Manage Jenkins <http://devbox.local:8080/jenkins/configure>`_
4.  Install the git plugin for jenkins
5.  Configure the shell used for jobs to be ``/bin/bash -l`` (use cygwin bash on windows)
5.  Use the "New Job" menu item to create a new job named "ChartIt -
    develop Branch" and of type "Free-Style software project" then hit "Ok"
6.  Fill in a description for the job
7.  Choose "Discard old builds" or your disk will eventually fill up. Set
    "Max # of builds to keep" to something generous like 100. History of
    builds tends to be useful in practice. 
8.  Choose "Source Code Management" and select git, use the repo url
    ``ssh://gitrepos@devbox.local/home/gitrepos/chartit.git`` now we should
    setup ssh-key based authentication for the jenkins user to the gitrepos
    user. An alternative would be to specify a local dir path. However by
    using ssh we decouple the repository host from the jenkins host which
    may be useful in future as your infrastructure grows. Also it means that
    you can tell which processes are accessing the git repositories just by
    doing a ps and grepping for gitrepos user.
8.1.    As jenkins user, do ``ssh-keygen -t rsa -N''``
8.2.    As root user ``cat ~jenkins/.ssh/id_dsa.pub >> ~gitrepos/.ssh/authorized_keys``
8.3.    As jenkins user, ssh to gitrepos@devbox.local and accept the first time
        warning about host identity
9.  Specify "branches to build" as "develop"
10. Specify "build triggers" as "Poll SCM" and set a schedule of "*/5 * * * *"
    which means jenkins will poll the shared git repo's develop branch every 5 mins
11. Under "build" choose "Execute shell" and specify a command of::

    MY_ENV=$RANDOM
    . /etc/bash_completion.d/virtualenvwrapper
    mkvirtualenv chartit-develop-$MY_ENV || /bin/true
    workon chartit-develop-$MY_ENV || /bin/true
    pip install -r requirements.txt
    nosetests --with-xunit --with-xcoverage --cover-package=application 
    pylint -f parseable --ignore=tests application > pylint.out 2>&1 || /bin/true
    pep8 --show-pep8 --exclude test\* application > pep8.out 2>&1 || /bin/true
    deactivate
    rmvirtualenv chartit-develop-$MY_ENV

12. Install the Jenkins Violations & Cobertura plugins

    


-----------------------
 Continuous Deployment
-----------------------

Fabfile
 * Version bumps for git flow
 * Push to prod
