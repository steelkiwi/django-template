from fabric.api import run, env, cd, prefix, task, sudo, warn_only
import json
import subprocess
import requests


class Slack(object):

    web_hook_url = 'https://hooks.slack.com/services/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'
    server_update_template = '''```Staging server updated by {author_name}```'''

    @classmethod
    def send_server_update(cls, **params):
        print('Sending slack notification')

        author_name = subprocess.check_output(['git', 'config', 'user.name']).strip()
        params.update(author_name=author_name)

        server_update_msg = cls.server_update_template.format(**params)
        data = dict(channel='#{{cookiecutter.repo_name}}', text=server_update_msg)
        response = requests.post(url=cls.web_hook_url, data=json.dumps(data))

        print('Response {}'.format(response))


@task
def test():
    env.hosts = ['{{cookiecutter.domain_name}}:2215']
    env.user = 'webmaster'
    env.path = '/home/webmaster/project'
    env.branch = 'master'
    env.settings = 'production'



env.use_ssh_config = True

ENV_COMMAND = 'source /home/webmaster/venv/bin/activate'


@task
def manage(command):
    with cd(env.path), prefix(ENV_COMMAND):
        run('python manage.py {} --settings=config.settings.{}' .format(command, env.settings), shell=False)


@task
def update():
    with cd(env.path):
        run('git pull origin {}'.format(env.branch))
        run('find . -name "*.pyc" -exec rm -f {} \;')
        requirements()
        migrate()
        collectstatic()
        restart()
        # compile()
    # send slack notification
    Slack.send_server_update(env=env)


@task
def requirements():
    with cd(env.path), prefix(ENV_COMMAND):
        run('pip install --exists-action=s -r requirements.txt')


@task
def migrate():
    with cd(env.path):
        manage('migrate --no-initial-data')


@task
def collectstatic():
    with cd(env.path):
        # manage('collectstatic_js_reverse')
        manage('collectstatic --noinput')


@task
def restart():
    run('supervisorctl restart all')


@task
def start():
    run('supervisorctl start all')


@task
def stop():
    run('supervisorctl stop all')


@task
def status():
    run('supervisorctl status')


@task
def compile():
    with cd(env.path):
        manage('compilemessages')
