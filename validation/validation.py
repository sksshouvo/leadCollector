class validation:
    def __init__(self):
        pass
    def google_map_check(self, link):
        if not link.__contains__("www.google.com/maps"):
            print("Invalid Google Map Link")
            return False
        return True