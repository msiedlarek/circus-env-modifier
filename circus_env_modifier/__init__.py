import subprocess
import logging

__all__ = (
    'before_spawn',
)

logger = logging.getLogger(__name__)

def before_spawn(watcher, arbiter, hook_name, **kwargs):
    command = dict(watcher.options())['env_modification_command']
    process = subprocess.Popen(
        ['%s && env' % command],
        shell=True,
        env=watcher.env,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        universal_newlines=True
    )
    stdout, stderr = process.communicate()
    if process.returncode != 0:
        logger.error("Environment modification command failed: %s" % stderr)
        return False
    for line in stdout.split('\n'):
        try:
            name, value = line.split('=')
        except ValueError:
            continue
        watcher.env[name] = value
    return True
