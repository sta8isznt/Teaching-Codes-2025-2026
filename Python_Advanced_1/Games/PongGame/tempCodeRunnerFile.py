def _check_events(self):
        """Check for user events"""
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()   # Closes Pygame Graphics
                sys.exit()  # Closes the window