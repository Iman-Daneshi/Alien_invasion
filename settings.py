class Settings:
    '''a class to store all settings for Alien Invasion.'''
    
    def __init__(self, msg = ''):
        '''initialize the game's settings'''
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230) 
        # ship settings
        self.ship_limits = 3

        # bullet settings
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.allowed_bullets = 3
        # alien settings
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
        
        # how quickly the game speeds up
        self.speedup_scale = 1.1
        # How quickly the alien point values increase
        self.score_scale = 1.5
        self.initialize_dynamic_settings(msg)
        # score 
        self.alien_points = 10
    
    def initialize_dynamic_settings(self,msg):
        """Initialize settings that change throughout the game."""
        if msg == 'Easy':
            self.ship_speed = 1.5
            self.bullet_speed = 3.0
            self.alien_speed = 0.2
            # number of times the ship should shoot a star
            self.alien_kills = 1 
        elif msg == 'Normal':
            self.ship_speed = 1.5
            self.bullet_speed = 3.0
            self.alien_speed = 0.4
            self.alien_kills = 2
        elif msg == 'Hard':
            self.ship_speed = 1.5
            self.bullet_speed = 3.0
            self.alien_speed = 0.6
            self.alien_kills = 3
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
        self.shooted_aliens_list = []

    def increase_speed(self):
        """Increase speed settings."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)