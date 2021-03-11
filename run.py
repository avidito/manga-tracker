import click

# Basic OOP Format
from manga_tracker.log import Logger
from manga_tracker.bounty import BountyHandler
from manga_tracker.database import DatabaseEngine

# OOP CLI format
from manga_tracker import MangaTracker as mt

@click.group()
def cli():
    pass

@cli.command('crawl')
def crawl():
    # Deleted soon
    log = Logger('logs')
    bh = BountyHandler('bounty.json')
    db = DatabaseEngine('outputs')

    # Initiate job
    job_id = log.log_start()
    groups = bh.groups
    db.init_db(job_id)

    # Scraping each target
    mt.crawl(groups, log, db)

    # End job
    log.log_end()
    log.show_log()


if __name__ == '__main__':
    cli()
