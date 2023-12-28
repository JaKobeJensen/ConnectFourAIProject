from pygame import Rect, Surface, draw, font, mouse
from pygame.font import Font, SysFont
from pygame.math import Vector2
from pygame.sprite import Sprite


class Object(Sprite):
    def __init__(
        self,
        name: str,
        image: Surface,
        position: tuple[int, int] = (0, 0),
        direction_angle: float = 0.0,
        velocity: float = 0.0,
        terminal_velocity: float = 10.0,
        acceleration: float = 0.0,
        visible: bool = True,
    ) -> None:
        Sprite.__init__(self)
        self._name = name
        self._image: Surface = image
        self._position: Vector2 = Vector2(position)
        self._rect: Rect = Rect((self.x, self.y), (self.width, self.height))
        self._direction_vector: Vector2 = Vector2((1, 0)).normalize()
        self._direction_vector.rotate_ip(direction_angle)
        self._velocity: float = velocity
        self.terminal_velocity: float = terminal_velocity
        self.acceleration: float = acceleration
        self.visible: bool = visible
        return

    @property
    def name(self) -> str:
        return self._name

    @property
    def image(self) -> Surface:
        return self._image

    @image.setter
    def image(self, new_image: Surface) -> None:
        self._image = new_image
        self._rect = Rect((self.x, self.y), (self.width, self.height))
        return

    @property
    def rect(self) -> Rect:
        return self._rect

    @property
    def width(self) -> int:
        return self._image.get_width()

    @property
    def height(self) -> int:
        return self._image.get_height()

    @property
    def position(self) -> tuple[int, int]:
        return (int(self._position.x), int(self._position.y))

    @position.setter
    def position(self, new_position: tuple[int | float, int | float]) -> None:
        self._position.x = float(new_position[0])
        self._position.y = float(new_position[1])
        self._rect.x = new_position[0]
        self._rect.y = new_position[1]
        return

    @property
    def x(self) -> int:
        return int(self._position.x)

    @x.setter
    def x(self, new_x: int | float) -> None:
        self.position = (new_x, self.y)
        return

    @property
    def y(self) -> int:
        return int(self._position.y)

    @y.setter
    def y(self, new_y: int | float) -> None:
        self.position = (self.x, new_y)
        return

    @property
    def direction(self) -> float:
        return self._direction_vector.angle_to()

    @direction.setter
    def direction(self, new_direction_angle: float) -> None:
        self._direction_vector.rotate_ip(new_direction_angle)
        return

    @property
    def direction_vector(self) -> Vector2:
        return self._direction_vector.copy()

    @property
    def velocity(self) -> float:
        return self._velocity

    @velocity.setter
    def velocity(self, new_velocity) -> None:
        if new_velocity < self.terminal_velocity:
            self._velocity = new_velocity
        else:
            self._velocity = self.terminal_velocity
        return

    def move(self) -> None:
        self.velocity += self.acceleration
        self.velocity_vector = self._direction_vector * self._velocity
        self.position = self._position + self.velocity_vector
        return

    def update(self) -> None:
        self.move()
        return


class ButtonObject(Object):
    font.init()

    def __init__(
        self,
        name: str,
        width: int,
        height: int,
        text: str = "",
        text_font: Font = SysFont("Aptos", 16),
        text_color: tuple[int, int, int] = (0, 0, 0),
        position: tuple[int, int] = (0, 0),
        border_color: tuple[int, int, int] = (0, 0, 0),
        border_width: int = 1,
        background_color: tuple[int, int, int] = (200, 200, 200),
        direction: float = 0.0,
        velocity: float = 0.0,
        terminal_velocity: float = 10.0,
        acceleration: float = 0.0,
        visible: bool = True,
    ) -> None:
        self._text: str = text
        self._text_color: tuple[int, int, int] = text_color
        self._text_font: Font = text_font
        self._text_surface: Surface = self._text_font.render(
            self._text, 1, self._text_color
        )
        self._border_color: tuple[int, int, int] = border_color
        self._border_width: int = border_width
        self._background_color: tuple[int, int, int] = background_color

        image = Surface((width, height))
        image.fill(background_color)
        image.blit(
            self._text_surface,
            (
                round((width / 2) - (self._text_surface.get_width() / 2)),
                round((height / 2) - (self._text_surface.get_height() / 2)),
            ),
        )
        draw.rect(image, border_color, image.get_rect(), border_width)

        Object.__init__(
            self,
            name,
            image,
            position,
            direction,
            velocity,
            terminal_velocity,
            acceleration,
            visible,
        )
        return

    def _update_image(self) -> None:
        self._text_surface = self._text_font.render(self._text, 1, self._text_color)
        image = Surface((self.width, self.height))
        image.fill(self._background_color)
        image.blit(
            self._text_surface,
            (
                round((self.width / 2) - (self._text_surface.get_width() / 2)),
                round((self.height / 2) - (self._text_surface.get_height() / 2)),
            ),
        )
        draw.rect(image, self._border_color, image.get_rect(), self._border_width)
        self.image = image
        return

    @property
    def text(self) -> str:
        return self._text

    @text.setter
    def text(self, new_text: str) -> None:
        self._text = new_text
        self._update_image()
        return

    @property
    def text_color(self) -> tuple[int, int, int]:
        return self._text_color

    @text.setter
    def text_color(self, new_text_color: tuple[int, int, int]) -> None:
        self._text_color = new_text_color
        self._update_image()
        return

    @property
    def text_font(self) -> Font:
        return self._text_font

    @text_font.setter
    def text_font(self, new_text_font: Font) -> None:
        self._text_font = new_text_font
        self._update_image()
        return

    @property
    def border_color(self) -> tuple[int, int, int]:
        return self._border_color

    @border_color.setter
    def border_color(self, new_border_color: tuple[int, int, int]) -> None:
        self._border_color = new_border_color
        self._update_image()
        return

    @property
    def border_width(self) -> int:
        return self._border_width

    @border_width.setter
    def border_width(self, new_border_width: int) -> None:
        self._border_width = new_border_width
        self._update_image()
        return

    @property
    def background_color(self) -> tuple[int, int, int]:
        return self._background_color

    @background_color.setter
    def background_color(self, new_background_color: tuple[int, int, int]) -> None:
        self._background_color = new_background_color
        self._update_image()
        return

    def move_hover(self) -> bool:
        return self._rect.collidepoint(mouse.get_pos())


class TextObject(Object):
    font.init()

    def __init__(
        self,
        name: str,
        text: str,
        text_font: Font = SysFont("Aptos", 16),
        text_color: tuple[int, int, int] = (0, 0, 0),
        position: tuple[int, int] = (0, 0),
        direction: float = 0.0,
        velocity: float = 0.0,
        terminal_velocity: float = 10.0,
        acceleration: float = 0.0,
        visible: bool = True,
    ) -> None:
        self._text: str = text
        self._text_color: tuple[int, int, int] = text_color
        self._text_font: Font = text_font
        image = self._text_font.render(self._text, 1, self._text_color)
        Object.__init__(
            self,
            name,
            image,
            position,
            direction,
            velocity,
            terminal_velocity,
            acceleration,
            visible,
        )
        return

    @property
    def text(self) -> str:
        return self._text

    @text.setter
    def text(self, new_text: str) -> None:
        self._text = new_text
        self.image = self._text_font.render(self._text, 1, self._text_color)
        return

    @property
    def text_color(self) -> tuple[int, int, int]:
        return self._text_color

    @text.setter
    def text_color(self, new_text_color: tuple[int, int, int]) -> None:
        self._text_color = new_text_color
        self.image = self._text_font.render(self._text, 1, self._text_color)
        return

    @property
    def text_font(self) -> Font:
        return self._text_font

    @text_font.setter
    def text_font(self, new_text_font: Font) -> None:
        self._text_font = new_text_font
        self.image = self._text_font.render(self._text, 1, self._text_color)
        return
