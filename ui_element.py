class UIElement:
    def __init__(self, element_type, text, color, x, y):
        if element_type == "text":
            self.text_surface = self.font.render(
                text, False, color)
            self.text_rect = self.text_surface.get_rect(
                center=(x, y))

        return self

    def render(self):
        self.surface.blit(self.text_surface, self.text_rect)
