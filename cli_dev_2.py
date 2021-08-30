import click
@click.group()
def main():
    """
    Simple Python Program Implimention
    """
    pass
@main.command()
@click.argument('vals', type=int,nargs=-1)
def sum1(vals):
    s=0
    for i in list(vals):
        s=s+i
    click.echo(f"{s}")
@main.command()
@click.argument('vals',type=int,nargs=-1)
def max_list(vals):
    vals=list(vals)
    max=vals[0]
    for i in range(1,len(vals)):
        if vals[i] >max:
            max=vals[i]
    print("max value from list :{}".format(max))
@main.command()
@click.argument('string1',type=str)
def reverse_string(string1):
    rev_str=string1[::-1]
    click.echo(rev_str)
if __name__ == "__main__":
    main()