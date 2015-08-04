paperslacktail. because you don't get enough slack messages already
------------------------------------------

examples of awesome
~~~~~~~~

::

    # stream all messages from your production papertrail group 
    paperslacktail --slack-token <token> --slack-channel <channel> '-c ~/.papertrail.yml -g Production'


usage
~~~~~
::
    usage: paperslacktail.py [-h] [--slack-token SLACK_TOKEN]
                            [--slack-channel SLACK_CHANNEL] [--debug]
                            papertrail

    stream syslog from papertrail to slack

    positional arguments:
    papertrail            arguments to pass to the papertrail command, like '-c
                            ~/.papertrail.yml -g Production'. Note that '-j -f' is
                            required and is passed by default. Pass this in
                            quotes.

    optional arguments:
    -h, --help            show this help message and exit
    --slack-token SLACK_TOKEN
                            Slack token for your bot
    --slack-channel SLACK_CHANNEL
                            Slack channel to post to, like C0600UX9E
    --debug               log to stdout


install
~~~~~~~

clone the repo and ``python setup.py install``
