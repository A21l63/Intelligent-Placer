class Working_space:
    left_x = None
    right_x = None
    top_y = None
    bot_y = None

    def __init__(self, points):
        self.left_x = points[0]
        self.right_x = self.left_x + points[2]
        self.bot_y = points[1]
        self.top_y = self.bot_y + points[3]

