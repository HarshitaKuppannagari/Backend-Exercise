import typer
import pandas as pd
from typing import List
from get_papers_list.pubmed import fetch_papers

app = typer.Typer()

@app.command()
def fetch(
    query: List[str] = typer.Argument(..., help="Search query for PubMed"),
    file: str = typer.Option(None, "--file", "-f", help="File to save the CSV output"),
    debug: bool = typer.Option(False, "--debug", "-d", help="Enable debug mode")
) -> None:
    """
    Fetch PubMed papers and filter for non-academic authors.
    """
    query_str = " ".join(query)
    results = fetch_papers(query_str, debug)

    if not results:
        typer.echo("No results found.")
        raise typer.Exit(code=1)

    if file:
        df = pd.DataFrame(results)
        df.to_csv(file, index=False)
        typer.echo(f"✅ Saved {len(results)} records to {file}")
    else:
        for item in results:
            typer.echo(item)

if __name__ == "__main__":
    app()
