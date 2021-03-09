import json

class BountyHandler:
    """
    Module to Use and Manage Bounty List
    """
    def __init__(self, path):
        self.path = path
        self.targets = self.read_bounty()

    def read_bounty(self):
        """
        Validate and read bounty list.
        """
        with open(self.path, 'r') as f:
            bounty = json.loads(f.read())
        return bounty['targets']

    # Update Bounty File
    # Loggin Bounty File
