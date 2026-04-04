while current_x < self.settings.screen_width - 2*alien_width:
            self._create_alien(current_x)
            current_x = current_x + 2 * alien_width