# synergy-fabric

Fabric scripts for managing `synergys` and `synergyc`. Basically a simple non-graphical alternative to
the excellent <a href="http://code.google.com/p/quicksynergy/">quicksynergy</a>.

By all means use quicksynergy to generate your `synergys` config files, but once you have them
use this fabric script to handle repeated invocations.

## Usage

<pre>
> fab -l
Available commands:

    client  Usage:   fab -H <user@host> client:(<server-ip>|stop)[,<name>]
    server  Usage:   fab -H <user@host> server:(<config-file>|stop)

> fab -d client
Displaying detailed information for task 'client':

    Usage:   fab -H <user@host> client:(<server-ip>|stop)[,<name>]
    Example: fab -H family@10.1.1.5 client:10.1.1.9,hector

> fab -d server
Displaying detailed information for task 'server':

    Usage:   fab -H <user@host> server:(<config-file>|stop)
    Example: fab -H localhost server:./stonk.conf

</pre>

## License

GPLv3 - http://www.gnu.org/licenses/gpl-3.0.txt
