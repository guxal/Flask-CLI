#!/usr/bin/python3
"""
This is CLI for FLASK
"""
import typer
from flaskcli_pkg.commands import creates

app = typer.Typer()
app.add_typer(creates.app, name="create")


def main():
    app()

if __name__ == "__main__":
    main()
