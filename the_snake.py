# -*- coding: utf-8 -*-

from random import randint

import pygame

# Ðàçìåðû ïîëÿ è ñåòêè:
SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

# Îïðåäåëåíèå íàïðàâëåíèé:
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# ×¸ðíûé ôîí:
BOARD_BACKGROUND_COLOR = (0, 0, 0)

# Áèðþçîâûå ãðàíèöû ÿ÷ååê
BORDER_COLOR = (93, 216, 228)

# Êðàñíûå ÿáëî÷êè
APPLE_COLOR = (255, 0, 0)

# Çåë¸íàÿ çìåÿ
SNAKE_COLOR = (0, 255, 0)

# Ñêîðîñòü çìåè
SPEED = 20

# Íàñòðîéêà èãðîâîãî îêíà
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

# Çàãîëîâîê îêíà
pygame.display.set_caption(
    "Snake"
)  # ñññ

# Íàñòðîéêà âðåìåíè
clock = pygame.time.Clock()


# Ðîäèòåëüñêèé êëàññ äëÿ ÿáëîêà è çìåè
class GameObject:
    """
    Ñàìûé ÷òî íè
    íà åñòü îáûêíîâåííûé
    ðîäèòåëüñêèé
    êëàññ äëÿ áóäóùèõ
    èãðîâûõ
    îáúåêòîâ, òàêèõ
    êàê çìåÿ è ÿáëîêî
    """

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.position = (self.x, self.y)
        self.body_color = None

    def draw(self, screen):
        """
        Ýòî óæå
        âûãëÿäèò ñòðàííî
        ß äîëæåí áûë
        ñíà÷àëà ñäåëàòü
        îáû÷íûå êàâû÷êè,
        ïîòîì ñêàçàëè
        îôîðìèòü òðîéíûå
        """
        pass


# Êëàññ çìåè
class Snake(GameObject):
    """
    ß äàæå íå çíàþ,
    ÷òî òóò âîîáùå
    ìîæíî íàïèñàòü,
    ÿ óæå òàê óñòàë
    ïåðåïèñûâàòü ýòè
    êîììåíòàðèè
    Äà, òóò êëàññ çìåè
    (êòî áû ìîã ïîäóìàòü)
    """

    def __init__(self, x=0, y=0):
        super().__init__(x, y)
        self.body = [(x, y)]
        self.direction = RIGHT
        self.next_direction = None
        self.positions = self.body
        self.body_color = SNAKE_COLOR

    def move(self):
        """
        Ûûûûû
        Êàê æå ìåíÿ
        êîëáàñèò
        îò ýòèõ êàâû÷åê
        """
        head_x, head_y = self.body[0]
        new_head = (
            head_x + self.direction[0] * GRID_SIZE,
            head_y + self.direction[1] * GRID_SIZE,
        )

        # öèêëè÷åñêèå ãðàíèöû
        new_head_x = new_head[0] % SCREEN_WIDTH
        new_head_y = new_head[1] % SCREEN_HEIGHT

        self.body.insert(0, (new_head_x, new_head_y))
        self.body.pop()

    def grow(self):
        """
        Êîãäà çìåÿ êóøàåò
        îíà ðàñò¸ò íà îäíó êëåòêó
        Êàê áóäòî âìåñòî ÿáëîê
        îíà åñò ðàñòèøêó
        """
        self.body.append(self.body[-1])

    def check_collision(self):
        """
        Çìåÿ ïðÿì òàêàÿ
        ãèáêàÿ, ÷òî ìîæåò
        âðåçàòüñÿ â ñàìó
        ñåáÿ, ÷òî ïëîõî
        â ýòîì ñëó÷àå
        çìåÿ ïîìð¸ò
        """
        for i in range(1, len(self.body)):
            if self.body[0] == self.body[i]:
                return True
        return False

    def draw(self, screen):
        """
        Çìåÿ äîëæíà
        áûòü âèäíà íà
        ýêðàíå ìîíèòîðà
        ïðèêîëüíî, äà?
        """
        for segment in self.body[:-1]:
            rect = pygame.Rect(segment, (GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(screen, SNAKE_COLOR, rect)
            pygame.draw.rect(screen, BORDER_COLOR, rect, 1)

        # Îòðèñîâêà ãîëîâû çìåè
        head_rect = pygame.Rect(self.body[0], (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(screen, SNAKE_COLOR, head_rect)
        pygame.draw.rect(screen, BORDER_COLOR, head_rect, 1)

    def update_direction(self):
        """
        Çìåÿ òèïà
        äâèãàåòñÿ
        ìîùíî
        âî âñå ñòîðîíû
        äëÿ ýòîãî
        ìû îáðàáàòûâàåì
        íàæàòèÿ êëàâèø
        """
        if self.next_direction:
            self.direction = self.next_direction
            self.next_direction = None

    def get_head_position(self):
        """
        ßçü
        Êàðàñü
        Íàëèì
        Ùóêà
        Îêóíü
        Ñåëüäü
        Îñ¸òð
        Êàìáàëà
        """
        return self.body[0]

    def reset(self):
        """
        Õèõè
        Õàõà
        Õåõå
        Õîõî
        Ïî÷åìó âñ¸ òàê êðèâî?
        """
        self.body = [(GRID_WIDTH // 2 * GRID_SIZE,
                      GRID_HEIGHT // 2 * GRID_SIZE)]
        self.direction = RIGHT
        self.next_direction = None
        self.positions = self.body


# Êëàññ ÿáëîêà
class Apple(GameObject):
    """
    ß äàæå íå çíàþ,
    ÷òî òóò âîîáùå
    ìîæíî íàïèñàòü, ÿ
    óæå òàê óñòàë
    ïåðåïèñûâàòü ýòè
    êîììåíòàðèè
    Äà, òóò êëàññ ÿáëîêà
    (êòî áû ìîã ïîäóìàòü)
    """

    def __init__(self, x=0, y=0):
        super().__init__(x, y)
        self.position = (self.x, self.y)
        self.body_color = APPLE_COLOR
        self.randomize_position()

    def randomize_position(self):
        """
        ß óæå òåðìèíàòîð
        ïðÿì êðûøà åäåò îò
        ýòèõ çàìå÷àíèé
        """
        self.x = randint(0, GRID_WIDTH - 1) * GRID_SIZE
        self.y = randint(0, GRID_HEIGHT - 1) * GRID_SIZE
        self.position = (self.x, self.y)

    def draw(self, screen):
        """
        Ê ýòîìó ìîìåíòó
        ó ìåíÿ çàêîí÷èëèñü
        øóòêè, ïîýòîìó
        ñêàæó, ÷òî òóò
        ìåòîä îòðèñîâêè
        ßÁËÎÊÀ
        """
        rect = pygame.Rect(self.x, self.y, GRID_SIZE, GRID_SIZE)
        pygame.draw.rect(screen, APPLE_COLOR, rect)
        pygame.draw.rect(screen, BORDER_COLOR, rect, 1)


def handle_keys(game_object):
    """
    À âîò òóò
    ëåæèò ìåòîä
    îáðàáîòêè íàæàòèÿ
    êëàâèø äëÿ
    óïðàâëåíèÿ çìå¸é
    Ûõûõûõûõõûõûõû
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and game_object.direction != DOWN:
                game_object.next_direction = UP
            elif event.key == pygame.K_DOWN and game_object.direction != UP:
                game_object.next_direction = DOWN
            elif event.key == pygame.K_LEFT and game_object.direction != RIGHT:
                game_object.next_direction = LEFT
            elif event.key == pygame.K_RIGHT and game_object.direction != LEFT:
                game_object.next_direction = RIGHT


def main():
    """
    Ïðåäñòàâëÿåòå,
    ýòî ôóíêöèÿ
    main
    Áåç íå¸ íè÷åãî
    íå áóäåò ðàáîòàòü
    è çìåÿ íå
    ñìîæåò æðàòü ÿáëîêè
    """
    pygame.init()
    snake = Snake(GRID_WIDTH // 2 * GRID_SIZE, GRID_HEIGHT // 2 * GRID_SIZE)
    apple = Apple()

    while True:
        clock.tick(SPEED)
        handle_keys(snake)
        snake.update_direction()

        # Äâèæåíèå çìåéêè
        snake.move()

        # Ïðîâåðêà íà ñòîëêíîâåíèå
        if snake.check_collision():
            break

        # Ïðîâåðêà íà ïîåäàíèå ÿáëîêà
        if snake.body[0] == (apple.x, apple.y):
            snake.grow()
            apple.randomize_position()

        # Îòðèñîâêà
        screen.fill(BOARD_BACKGROUND_COLOR)

        # Îòðèñîâêà ãðàíèö êëåòîê
        for x in range(0, SCREEN_WIDTH, GRID_SIZE):
            pygame.draw.line(screen, BORDER_COLOR, (x, 0), (x, SCREEN_HEIGHT))
        for y in range(0, SCREEN_HEIGHT, GRID_SIZE):
            pygame.draw.line(screen, BORDER_COLOR, (0, y), (SCREEN_WIDTH, y))

        # Îòðèñîâêà ÿáëîêà
        apple.draw(screen)

        # Îòðèñîâêà çìåè
        snake.draw(screen)

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
