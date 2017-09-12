import click
import cmd
import sys

class REPL(cmd.Cmd):
    intro = 'Welcome to Flipchain Decentralized Casino. Type help to list commands'
    prompt = 'flipchain > '

    def __init__(self, ctx):
        cmd.Cmd.__init__(self)
        self.ctx = ctx

    def default(self, line):
        subcommand = cli.commands.get(line)
        if subcommand:
            self.ctx.invoke(subcommand)
        else:
            return cmd.Cmd.default(self, line)

@click.group(invoke_without_command=True)
@click.pass_context
def cli(ctx):
    if ctx.invoked_subcommand is None:
        repl = REPL(ctx)
        repl.cmdloop()

@cli.command()
@click.option('--type', default='baccarat')
def list(type):
    '''Show list of public tables'''
    print 'list'

@cli.command()
@click.option('--type', help='Type of table to open (poker, baccarat)', default='baccarat')
@click.option('--scope', help='Make private table', is_flag=True)
@click.option('--amount', help='Initial amount to join table with', default=50)
def create(type, scope, amount):
    '''Create a table'''
    print 'create'

@cli.command()
@click.option('--table', help='Unique code of table', required=True)
@click.option('--amount', help='Initial amount to join table with', default=50)
def join(table, amount):
    '''Join an existing public table'''
    print 'join'

@cli.command()
def exit():
    '''Exit the CLI'''
    sys.exit(0)

if __name__ == "__main__":
    cli()
