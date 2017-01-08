class Hero:
    def __init__(self, sex=None):
        if sex is None:
            sex = 'N'
        self.sex = sex
