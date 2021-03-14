class OutputHandler:
    """
    Handler to create and show job outputs.
    """
    @staticmethod
    def init_output(path, delimiter='|', columns=['alias', 'title', 'ongoing', 'updated_at', 'latest_chapter', 'latest_chapter_link']):
        """
        Initiate output file.
        """
        with open('{}.txt'.format(path), 'w') as f:
            f.write(delimiter.join(columns) + '\n')

    @staticmethod
    def load_data(out_path, alias, data, columns=['alias', 'title', 'ongoing', 'updated_at', 'latest_chapter', 'latest_chapter_link']):
        """
        Convert data to row format and load to database
        """
        # Transform data to row format
        trans_data = ''
        for col in columns[1:]:
            trans_data += '|{}'.format(data[col])
        row = alias + trans_data

        # Load to database
        with open('{}.txt'.format(out_path), 'a', encoding="utf-8") as f:
            f.write(row + '\n')

    @staticmethod
    def show_output(out_path='outputs', delimiter='|'):
        """
        Show full crawling result in table format.
        """
        with open('{}.txt'.format(out_path), 'r', encoding="utf-8") as f:
            raw = f.read()
        result = [row.split(delimiter) for row in raw.split('\n')]

        # Showing result
        print(*result[0], sep=' | ')
        print("-" * 50)
        for row in result[1:]:
            print(*row, sep=' | ')
