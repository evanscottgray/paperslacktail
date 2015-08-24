import argparse
import time
import json
import sys
from slackclient import SlackClient
from subprocess import PIPE, Popen
from threading import Thread
from Queue import Queue, Empty

app = {}
ON_POSIX = 'posix' in sys.builtin_module_names


def enqueue_output(out, queue):
    for line in iter(out.readline, b''):
        queue.put(line)
    out.close()


def parse_line(line):
    pt_data = json.loads(line)
    messages = extract_messages(pt_data)

    for m in messages:
        notify(m)


def extract_messages(pt_data):
    events = pt_data.get('events')
    messages = [{'msg': e.get('message'), 'ip': e.get('source_ip'),
                 'hostname': e.get('source_name')}
                for e in events if e.get('message') is not None]
    return messages


def get_slack_client():
    token = app.get('SLACK_TOKEN')
    sc = SlackClient(token)
    return sc


def post_slack(data):
    msg = 'HOST: |%s| MSG: |%s|' % (data.get('hostname'), data.get('msg'))
    app['slack_client'].api_call("chat.postMessage",
                                 channel=app.get('SLACK_CHANNEL'),
                                 text=msg)


def notify(data):
    methods = [post_slack]
    if app['debug']:
        print 'Notifying with %s for %s' % ([n.__name__ for n in methods],
                                            data)
    for m in methods:
        m(data)


def slacktail(pt_cmd='papertrail', pt_args=None):
    cmd = pt_cmd
    args = ['-j -f']

    if pt_args is not None:
        args.append(pt_args)
    pt = cmd + ' ' + ' '.join(args)
    p = Popen(pt.split(' '), stdout=PIPE, bufsize=1, close_fds=ON_POSIX)
    q = Queue()
    t = Thread(target=enqueue_output, args=(p.stdout, q))
    t.daemon = True
    t.start()

    while True:
        try:
            line = q.get_nowait()
        except Empty:
            pass
        else:
            parse_line(line)
        time.sleep(0.5)


def main():
    desc = 'stream syslog from papertrail to slack'
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('--slack-token',
                        help='Slack token for your bot')
    parser.add_argument('--slack-channel',
                        help='Slack channel to post to, like C0600UX9E')
    parser.add_argument('papertrail', help='arguments to pass to the \
                        papertrail command, like \'-c ~/.papertrail.yml -g \
                        Production\'. Note that \'-j -f\' is required and \
                        is passed by default. Pass this in quotes.')
    parser.add_argument('--debug', help='log to stdout', action='store_true')

    args = parser.parse_args()
    pt_args = args.papertrail

    app['debug'] = args.debug
    app['SLACK_CHANNEL'] = args.slack_channel
    app['SLACK_TOKEN'] = args.slack_token
    app['slack_client'] = get_slack_client()

    slacktail(pt_args=pt_args)

if __name__ == '__main__':
    main()
