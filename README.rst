paperslacktail. because you don't get enough slack messages already
------------------------------------------

paperslacktail, a tool that wraps the wonderful papertrail-cli gem and the slack api to stream syslog from papertrail straight into slack.

you'll need to have the papertrail gem installed.

examples of awesome
~~~~~~~~

::

    # stream all messages from your production papertrail group 
    paperslacktail --slack-token <slack-token> \
                   --slack-channel <slack-channel-id> \
                   '-c ~/.papertrail.yml -g Production'


usage
~~~~~
::

        usage: paperslacktail.py [-h] [--slack-token SLACK_TOKEN]
                                 [--slack-channel SLACK_CHANNEL] [--debug]
                                 papertrail-args

        stream syslog from papertrail to slack

        positional arguments:
        papertrail              arguments to pass to the papertrail command, like '-c
                                ~/.papertrail.yml -g Production'. Note that '-j -f' is
                                required and is passed by default. Pass this in
                                quotes.

        optional arguments:
        -h, --help                       show this help message and exit
        --slack-token SLACK_TOKEN        Slack token for your bot
        --slack-channel SLACK_CHANNEL    Slack channel to post to, like C0600UX9E
        --debug                          log to stdout


install
~~~~~~~

to install from source, clone the repo and ``python setup.py install``, alternatively you can simply ``pip install paperslacktail``

be sure to ``gem install papertrail`` so that you have the papertrail cli installed.

deploy with docker
~~~~~~~

paperslacktail can quickly be deployed as a docker container that is ready to rock.

simply provide the container a papertrail api token, a slack token, and a slack channel id and you're up and running.


::

    docker run -d -e 'PAPERTRAIL_API_TOKEN=<papertrail>' \
           evanscottgray/paperslacktail --slack-token <slack-token> \
                                        --slack-channel <slack-channel-id> \
                                        '-g Production'

links and things
~~~~~~~~~~~~~~~~

- Dockerhub_
- Github_
- PyPI_

.. _Dockerhub: https://registry.hub.docker.com/u/evanscottgray/paperslacktail/
.. _Github: https://github.com/evanscottgray/paperslacktail
.. _PyPI: https://pypi.python.org/pypi/paperslacktail
