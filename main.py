from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen

from random import randint



class PongPaddle(Widget):
    score = NumericProperty(0)

    def bounce_ball(self, ball):
        if self.collide_widget(ball):
            vx, vy = ball.velocity
            offset = (ball.center_y - self.center_y) / (self.height / 2)
            bounced = Vector(-1 * vx, vy)
            vel = bounced * 1.1
            ball.velocity = vel.x, vel.y + offset



class PongBall(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)

    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos




class PongGame(Widget):
    ball = ObjectProperty(None)

    player1 = ObjectProperty(None)
    player2 = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(PongGame, self).__init__(**kwargs)
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)

    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        if keycode[1] == 'w':

            self.player1.y += 10
            #print(type(self.player1.size))
            #print("y : ", self.player1.y)
            #print("height : ", self.height)
            #print(self.player1.y - self.player1.size[1])
            if self.player1.y + self.player1.size[1] > self.height:
                self.player1.y = self.height-self.player1.size[1]


        elif keycode[1] == 's':
            self.player1.y -= 10
            #print(self.player1.center_y)
            #print(self.y)
            #print(self.player1.y)
            #print(self.player1.size[1])
            if self.player1.y < self.y:
                self.player1.y = self.y


        elif keycode[1] == 'up':
            self.player2.y += 10
            if self.player2.y + self.player2.size[1] > self.height:
                self.player2.y = self.height-self.player2.size[1]



        elif keycode[1] == 'down':
            self.player2.center_y -= 10
            if self.player2.y < self.y:
                self.player2.y = self.y

        return True

    def serve_ball(self, vel=(4, 0)):
        self.ball.center = self.center
        self.ball.velocity = vel

    def update(self, dt):
        self.ball.move()

        self.player1.bounce_ball(self.ball)
        self.player2.bounce_ball(self.ball)

        if (self.ball.y < 0) or (self.ball.top > self.height):
            self.ball.velocity_y *= -1

        if self.ball.x < self.x:
            self.player2.score += 1
            self.serve_ball(vel=(4, 0))

        if self.ball.right > self.width:
            self.player1.score += 1
            self.serve_ball(vel=(-4, 0))

        def on_touch_move(self, touch):
            if touch.x < self.width / 3:
                self.player1.center_y = touch.y
            if touch.x > self.width - self.width / 3:
                self.player2.center_y = touch.y



class GameScreen(Screen):
    def __init__(self, **kwargs):
        super(GameScreen, self).__init__(**kwargs)
        self.game = PongGame()
        self.add_widget(self.game)
        #self.game.serve_ball()
        Clock.schedule_interval(self.game.update, 1.0/60.0)




class PongApp(App):
    def build(self):
        """
        game = PongGame()
        game.serve_ball()
        Clock.schedule_interval(game.update, 1.0/60.0)
        return game
        """
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(GameScreen(name='Pong'))
        return sm

if __name__ == '__main__':
    PongApp().run()
