import random
from typing import override

import pygame

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    @override
    def draw(self, screen: pygame.Surface) -> None:
        _ = pygame.draw.circle(
            screen,
            "white",
            self.position,
            self.radius,
            LINE_WIDTH,
        )

    @override
    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        angle = random.uniform(20, 50)
        a_velocity = self.velocity.rotate(angle)
        b_velocity = self.velocity.rotate(-angle)
        splitted_radius = self.radius - ASTEROID_MIN_RADIUS
        a = Asteroid(*self.position, radius=splitted_radius)
        a.velocity = a_velocity
        b = Asteroid(*self.position, radius=splitted_radius)
        b.velocity = b_velocity
