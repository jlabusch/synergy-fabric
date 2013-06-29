# synergy-fabric

Fabric scripts for managing `synergys` and `synergyc`. Basically a simple non-graphical alternative to
the excellent <a href="http://code.google.com/p/quicksynergy/">quicksynergy</a>.

By all means use quicksynergy to generate your `synergys` config files, but once you have them
use this fabric script to handle repeated invocations.

### Example: Share the keyboard/mouse from `laptop` to `mediapc`

1. Create a `synergys` config
<pre>
    laptop$ cat > laptop.conf
    section: screens
    	laptop:
    	mediapc:
    end
    section: links
    	laptop:
    		right = mediapc
    	mediapc:
    		left = laptop
    end
</pre>

2. Start the server on `laptop`
<pre>
    laptop$ fab -H localhost server:./laptop.conf
</pre>

3. Start the client on `mediapc`
<pre>
    laptop$ fab -H media-pc client:laptop,media-pc
</pre>

### Helpers

If you're using <a href="https://github.com/jlabusch/vmdns">vmdns</a> then `synner` can generate the appropriate fabric invocations for you.

Test:
<pre>
    laptop$ ./synner start mediapc laptop
    fab -H $(vmdns laptop) server:./laptop.conf; fab -H $(vmdns mediapc) client:$(vmdns laptop),mediapc
</pre>

Execute:
<pre>
    laptop$ eval $(./synner start mediapc laptop)
</pre>

## License

GPLv3 - http://www.gnu.org/licenses/gpl-3.0.txt
