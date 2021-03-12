from datetime import datetime

class LogHandler:
    """
    Module to Read, Load, and Represent Job Logs
    """
    def __init__(self, path):
        self.path = path
        self.column = ['alias', 'title', 'authors', 'ongoing', 'genres', 'updated_at', 'latest_chapter', 'latest_chapter_link']

    @staticmethod
    def _dtlog(msg):
        """
        Embed Log Time to Message
        """
        now = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        return "{} {}\n".format(now, msg)

    @staticmethod
    def log_start(path):
        """
        Create start of job log.
        """
        # Init Job Id
        dt_start_time = datetime.now()
        job_id = dt_start_time.strftime("%Y%m%d%H%M")
        LogHandler.logging(path, job_id, 'Job Id: {}'.format(job_id))

        # Log Start Time
        start_time = dt_start_time.strftime('%d/%m/%Y %H:%M:%S')
        LogHandler.logging(path, job_id, 'Start Time: {}'.format(start_time))

        return job_id

    @staticmethod
    def log_scrape(path, job_id, title, response):
        """
        Create scraping log.
        """
        LogHandler.logging(path, job_id, '{} - Response: {}'.format(title, response))

    @staticmethod
    def log_end(path, job_id):
        """
        Create end of job log.
        """
        end_time = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        LogHandler.logging(path, job_id, 'End Time: {}\n'.format(end_time))

    @staticmethod
    def logging(path, job_id, msg):
        """
        Create initiation activity log.
        """
        with open('{}\{}.txt'.format(path, job_id), 'a') as f:
            f.write(LogHandler._dtlog(msg))

    def show_log(self, job_id=None):
        """
        Get log from corresponding job.
        """
        job_id = job_id if (job_id) else self.job_id

        # Get Log
        with open('{}\{}.txt'.format(self.path, job_id), 'r') as f:
            log = f.read()
        print(log)
