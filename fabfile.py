from fabric.api import local, run, env, put

def client(server='stop', name='hector'):
    """Usage: fab -H family@10.1.1.5 client:(<server-ip>|stop)[,<name>]"""
    run('killall -wq synergyc || :')
    if server != 'stop':
        run('synergyc --name ' + name + ' ' + server + '; sleep 1')

def server(conf='./stonk.conf'):
    """Usage: fab -H localhost server:(<config-file>|stop)"""
    run('killall -wq synergys || :')
    if conf != 'stop':
        put(conf, '/tmp/sgys.conf')
        run('synergys --config /tmp/sgys.conf; sleep 1')

