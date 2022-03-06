import typer
app = typer.Typer(no_args_is_help=True)

@app.command()
def greet(name: str, loud: bool = False):
    msg = f"Hello, {name}!"
    print(msg.upper() if loud else msg)

if __name__ == "__main__":
    app()
