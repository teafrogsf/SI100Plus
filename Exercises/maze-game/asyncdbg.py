import asyncio
import bdb
import cmd
import sys
import linecache

class AsyncDebugger(bdb.Bdb):
    def __init__(self):
        super().__init__()
        self.watch_expressions = []
        self._step_event = None

    def set_event_loop(self, loop):
        self.loop = loop

    async def user_line(self, frame):
        filename = frame.f_code.co_filename
        lineno = frame.f_lineno
        line = linecache.getline(filename, lineno).strip()
        print(f'Paused at {filename}:{lineno} - {line}')
        self.display_watch_expressions(frame)
        await self.interaction(frame)

    def display_watch_expressions(self, frame):
        if self.watch_expressions:
            print("Watch expressions:")
            for expr in self.watch_expressions:
                try:
                    value = eval(expr, frame.f_globals, frame.f_locals)
                    print(f"  {expr} = {value}")
                except Exception as e:
                    print(f"  {expr} = Error: {e}")

    async def interaction(self, frame):
        self.frame = frame

        if self._step_event is not None:
            self._step_event.set()  # Continue previous interaction

        self._step_event = asyncio.Event()
        DebuggerCLI(self).cmdloop()
        await self._step_event.wait()

class DebuggerCLI(cmd.Cmd):
    prompt = '(my-debugger) '

    def __init__(self, debugger):
        super().__init__()
        self.debugger = debugger

    def do_continue(self, arg):
        'Continue execution'
        self.debugger.set_continue()
        self.debugger.loop.call_soon_threadsafe(self.debugger._step_event.set)
        return True  # Exits the cmdloop

    def do_step(self, arg):
        'Step to the next line'
        self.debugger.set_step()
        self.debugger.loop.call_soon_threadsafe(self.debugger._step_event.set)
        return True

    def do_quit(self, arg):
        'Quit the debugger'
        self.debugger.set_quit()
        self.debugger.loop.call_soon_threadsafe(self.debugger._step_event.set)
        return True

    def do_watch(self, arg):
        'Add a watch expression: watch <expression>'
        if arg:
            self.debugger.watch_expressions.append(arg)
            print(f'Added watch expression: {arg}')
        else:
            print('Usage: watch <expression>')

    def do_unwatch(self, arg):
        'Remove a watch expression: unwatch <expression>'
        if arg in self.debugger.watch_expressions:
            self.debugger.watch_expressions.remove(arg)
            print(f'Removed watch expression: {arg}')
        else:
            print(f'No such watch expression: {arg}')

    def do_listwatches(self, arg):
        'List all watch expressions'
        if self.debugger.watch_expressions:
            print("Watch expressions:")
            for expr in self.debugger.watch_expressions:
                print(f"  {expr}")
        else:
            print("No watch expressions set.")

    def default(self, line):
        print(f'Unknown command: {line}')


async def test_function():
    x = 5
    await asyncio.sleep(1)
    y = 10
    z = x + y
    print(z)

if __name__ == '__main__':
    # loop = asyncio.get_event_loop()

    debugger = AsyncDebugger()
    debugger.set_event_loop(loop)
    
    # Wrap the test function with the debugger
    wrapped_test_function = debugger.runcall(test_function)

    # try:
    loop.run_until_complete(wrapped_test_function)
    # finally:
    #     loop.close()
