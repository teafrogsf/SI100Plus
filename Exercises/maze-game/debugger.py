import bdb
import cmd
import sys

class MyDebugger(bdb.Bdb):
    def user_line(self, frame):
        filename = frame.f_code.co_filename
        lineno = frame.f_lineno
        line = linecache.getline(filename, lineno).strip()
        print(f'Paused at {filename}:{lineno} - {line}')
        self.interaction(frame)

    def interaction(self, frame):
        self.frame = frame
        DebuggerCLI(self).cmdloop()

class DebuggerCLI(cmd.Cmd):
    prompt = '(my-debugger) '

    def __init__(self, debugger):
        super().__init__()
        self.debugger = debugger

    def do_continue(self, arg):
        'Continue execution'
        self.debugger.set_continue()
        return True  # Exits the cmdloop

    def do_step(self, arg):
        'Step to the next line'
        self.debugger.set_step()
        return True

    def do_quit(self, arg):
        'Quit the debugger'
        self.debugger.set_quit()
        return True

    do_next = do_step  # Alias 'next' to 'step'

    def default(self, line):
        print(f'Unknown command: {line}')

if __name__ == '__main__':
    # Example usage
    import linecache
    
    def test_function():
        x = 5
        y = 10
        z = x + y
        print(z)
    
    debugger = MyDebugger()
    debugger.run('test_function()')
