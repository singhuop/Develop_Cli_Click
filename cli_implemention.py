import click
@click.group()
def main():
    """
    Simple Arithmatic  Operation
    """
    pass
@main.command()
@click.option("--num",nargs=2,type=int)
def sum1(num):
    a,b=num
    s=a+b
    click.echo(f"{s}")
@main.command()
@click.option("--num",nargs=2,type=int)
def mul(num):
    a,b=num
    s=a*b
    click.echo(f"{s}")
@main.command()
@click.option("--num",nargs=2,type=int)
def sub1(num):
    a,b=num
    s=a-b
    click.echo(f"{s}")
@main.command()
@click.option("--num",nargs=2,type=int)
def div1(num):
    a,b=num
    s=a//b
    click.echo(f"{s}")
if __name__ == "__main__":
    main()



