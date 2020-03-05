#!/usr/bin/python3
"""
This is CLI for FLASK
"""
import typer
from commands import creates

app = typer.Typer()
app.add_typer(creates.app, name="create")

if __name__ == "__main__":
    app()
