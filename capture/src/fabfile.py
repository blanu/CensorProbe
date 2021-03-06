# fabfile.py is a Fabric configuraton file defining tasks which can be executed
# remotely. Remote tasks execution allows for client and server components to
# be executed on different machines, allowing for the traffic between them to
# travel across the Internet and therefore giving more representative traces
# than when run over loopback.
# It can be used manually with the "fab" command, but is normally launched
# from a paver task defined in pavement.py.

import os

from fabric.api import cd, run, env

env.use_ssh_config = True

# Bootstrap by installing CensorProbe source, updating to latest version, and running bootstrap.py
#def bootstrap():
#  if run('test -d CensorProbe').failed:
#    run('git clone https://gitweb.torproject.org/user/blanu/CensorProbe.git')
#  with cd('CensorProbe'):
#    run('git pull origin master')
#    if run('test -d bin').failed:
#      run('python bootstrap.py')

# Install dependencies: libevent, tor, and obfs2
def prepare():
  with cd('CensorProbe'):
    run('source bin/activate')
    run('paver libevent')
    run('paver tor')
    run('paver obfsproxy')

# Run obfs2 server
def run_obfsproxy_server():
  with cd('CensorProbe'):
    run('paver run_local_obfsproxy_server')

# Kill obfs2 server
def kill_obfsproxy():
  with cd('CensorProbe'):
    run('paver kill_local_obfsproxy')

# Run Dust server
def run_dust_server():
  with cd('CensorProbe'):
    run('paver run_local_dust_server')

# Kill Dust server
def kill_dust():
  with cd('CensorProbe'):
    run('paver kill_local_dust')

# Run Tor bridge
def run_tor_bridge():
  with cd('CensorProbe'):
    run('paver run_local_tor_bridge')

# Kill Tor bridge
def kill_tor():
  with cd('CensorProbe'):
    run('paver kill_local_tor')

def run_dust_replay_http_server():
  with cd('CensorProbe/capture'):
    run('paver run_local_dust_replay_http_server')

# Kill Dust server
def kill_dust_replay_http_server():
  with cd('CensorProbe/capture'):
    run('paver kill_local_dust_replay_http_server')

def list():
  run('ls *.zip')
