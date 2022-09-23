# CutterPython
### Description
Cutter is an awesome tool but didn't have method to execute Python script dynamically.

This is a simple plugin to "Execute" python script written for Cutter by selecting script file as IDAPython.

Also, it helps to print what exception was thrown from executed script on console.

### Installation
Just put CutterPython.py to "python" folder in "plugins" forlder you could find in [Edit] - [Preferences] - [Plugins].

It works just like IDAPython's run script, and shortcut key is the same.(Alt+F7)

### Errors to fix
When the plugin is executed, following error messages are shown on console.

* Only C and default locale supported with the posix collation implementation
* Only C and default locale supported with the posix collation implementation
* Case insensitive sorting unsupported in the posix collation implementation
* Numeric mode unsupported in the posix collation implementation

### Things to consider
In this script, the location of here($$) is decided by script. In IDAPython, it remains as it was. 

If you want here($$) is as it was, add two lines of code in Executor method: 
* Before first line of Executor: StartAddr=cutter.cmd("s")
* After the last line of Executor(aligned with first line of Executor): cutter.cmd("s {}".format(StartAddr))

These two lines would make the here as it was.

Also, it only "Executes" python script. So be careful when you use.
