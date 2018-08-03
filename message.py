class Message:
    def __init__(self):
        self.dt = None
        self.date_str = None
        self.channel = None
        self.text = None
        self.subtype = None
        self.user = None
        self.ts = None
        self.files = None


    def __str__(self):
            return(f'User: {self.user} | {self.text}')

    def __repr__(self):
            return(f'User: {self.user} | {self.text}')
