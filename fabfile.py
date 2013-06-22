from fabric.api import local, run, env, put

def client(server='stop', name='hector'):
    """
    Usage:   fab -H <user@host> client:(<server-ip>|stop)[,<name>]
    Example: fab -H family@10.1.1.5 client:10.1.1.9,hector
    """
    run('killall -wq synergyc || :')
    if server != 'stop':
        run('synergyc --name ' + name + ' ' + server + '; sleep 1')

def server(conf='./stonk.conf'):
    """
    Usage:   fab -H <user@host> server:(<config-file>|stop)
    Example: fab -H localhost server:./stonk.conf
    """
    run('killall -wq synergys || :')
    if conf != 'stop':
        put(conf, '/tmp/synergys.conf')
        run('synergys --config /tmp/synergys.conf; sleep 1')

