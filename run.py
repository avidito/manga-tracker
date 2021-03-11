import click

# OOP CLI format
from manga_tracker import MangaTracker

@click.group()
def cli():
    """
    CLI Program to Track Updated Manga using Web-Scraping (bs4).
    """
    pass

@cli.command('crawl')
def crawl():
    """
    Start crawling process.
    """
    handler = MangaTracker.init_job()
    MangaTracker.crawl(**handler)

@cli.command('show-bounty')
def show_bounty():
    """
    Show all targets in bounty list.
    """
    result = MangaTracker.show_bounty()
    print(result)

if __name__ == '__main__':
    cli()
