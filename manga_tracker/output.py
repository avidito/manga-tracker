from datetime import datetime, timedelta
import operator

class OutputHandler:
    """
    [Static Method] Handler to create and show job outputs.
    """

    @staticmethod
    def _output_viz(data):
        """
        Format data for output visualisation.

        Params
        ------
            data        : list. Output data in 2D list format.

        Returns
        -------
            formatted   : list. Formatted output data for output visualization.
        """
        _tr = (
            lambda x: x,                                              # website
            lambda x: x,                                              # alias
            lambda x: ''.join((x[:17], '...')) if len(x) > 20 else x, # title
            lambda x: 'Ongoing' if (x) else 'Completed',              # ongoing
            lambda x: x,                                              # updated_at
            lambda x: ''.join((x[:17], '...')) if len(x) > 20 else x, # latest_chapter
            lambda x: ''.join((x[:17], '...')) if len(x) > 20 else x, # latest_chapter_link
        )
        formatted = [[_tr[i](val) for i, val in enumerate(row)] for row in data]
        return formatted[0], formatted[1:]

    @staticmethod
    def init_output(path, columns, delimiter):
        """
        Initiate output file by pathname.

        Paramaters
        ----------
            path        : str. Relative pathname for output file directory (result directory).
            columns     : list. List of columns name for output table.
            delimiter   : str. Delimiter used for separating data.
        """
        out_path = path + '/outputs.txt'
        with open(out_path, 'w') as f:
            f.write(delimiter.join(columns) + '\n')

    @staticmethod
    def load_data(path, website, alias, data, columns, delimiter):
        """
        Convert data to row format and load to database.

        Parameters
        ----------
            path        : str. Relative pathname for output file directory (result directory).
            website     : str. Website's name for output data.
            alias       : str. Defined manga alias for output and log result.
            data        : dict. Extracted data that want to be loaded to outputs file.
            columns     : list. List of columns name for output table.
            delimiter   : str. Delimiter used for separating data.
        """
        # Transform data to row format
        trans_data = ''
        for col in columns[2:]:
            trans_data += '{}{}'.format(delimiter, data[col])
        row = ''.join([website, '|', alias, trans_data])

        # Load to database
        out_path = path + '/outputs.txt'
        with open(out_path, 'a', encoding="utf-8") as f:
            f.write(row + '\n')

    @staticmethod
    def show_output(path, delimiter):
        """
        Show full crawling result in table format.

        Parameters
        ----------
            path        : str. Relative pathname for output file directory (result directory).
            delimiter   : str. Delimiter used for separating data.

        Returns
        -------
            output      : list. Output data in 2D list format.
        """
        out_path = path + '/outputs.txt'
        with open(out_path, 'r', encoding="utf-8") as f:
            raw = f.read()[:-1]
        output = [row.split(delimiter) for row in raw.split('\n')]

        # Format Visualization
        header, content = OutputHandler._output_viz(output)
        content.sort(key=operator.itemgetter(0, 1))
        formatted = [header] + content
        return formatted

    @staticmethod
    def result(path, delimiter):
        """
        Show crawling result summary.

        Parameters
        ----------
            path        : str. Relative pathname for output file directory (result directory).
            delimiter   : str (default="|"). Delimiter used for separating data.
        """
        out_path = path + '/outputs.txt'
        with open(out_path, 'r', encoding="utf-8") as f:
            raw = f.read()
        result = [row.split(delimiter) for row in raw.strip().split('\n')]

        # Grouping by Update Time
        updated_today = []
        updated_last_7 = []
        updated_last_30 = []
        updated_older = []
        today_date = datetime.now().date()
        for row in result[1:]:
            date = datetime.strptime(row[4], '%d-%m-%Y %H:%M').date()
            if (date == today_date):
                updated_today.append(row)
            elif (date >= (today_date - timedelta(days=7))):
                updated_last_7.append(row)
            elif (date >= (today_date - timedelta(days=30))):
                updated_last_30.append(row)
            else:
                updated_older.append(row)

        # Show Report
        print("--- Manga Tracker Web-Crawling Result ---")
        print("Updated Today:")
        for row in updated_today:
            print(row)
        print("\nUpdated in the Last 7 Days:")
        for row in updated_last_7:
            print(row)
        print("\nUpdated in the Last 30 Days:")
        for row in updated_last_30:
            print(row)
        print("\nUpdated More Than 30 Days ago:")
        for row in updated_older:
            print(row)
