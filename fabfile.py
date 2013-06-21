from fabric.api import local, run, env, put

def hector(ip):
    env.hosts = ['family@' + ip]

def client(server='stop'):
    """Usage: fab hector:<hector-ip> client:[<server-ip>|stop]"""
    run('killall -wq synergyc || :')
    if server != 'stop':
        run('synergyc --name hector ' + server + '; sleep 1')
        #run('/usr/bin/screen -d -m /usr/bin/synergyc -f --name hector ' + server)

def server(stop='start'):
    """Usage: fab server[:stop]"""
    local('killall -wq synergys || :')
    if stop != 'stop':
        local('synergys --config ./stonk-home.conf')

