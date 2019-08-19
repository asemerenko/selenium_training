class Product:

    def __init__(self, name=None, regular_price_text=None, regular_price_color=None, regular_price_height=None,
                 regular_price_style=None, campaign_price_text=None, campaign_price_color=None,
                 campaign_price_height=None):
        self.name = name
        self.regular_price_text = regular_price_text
        self.regular_price_color = regular_price_color
        self.regular_price_height = regular_price_height
        self.regular_price_style = regular_price_style
        self.campaign_price_text = campaign_price_text
        self.campaign_price_color = campaign_price_color
        self.campaign_price_height = campaign_price_height

    def __eq__(self, other):
        return self.name == other.name \
               and (self.regular_price_text is None or other.regular_price_text is None
                    or self.regular_price_text == other.regular_price_text) \
               and (self.regular_price_color is None or other.regular_price_color is None
                    or self.regular_price_color == other.regular_price_color) \
               and (self.regular_price_height is None or other.regular_price_height is None
                    or self.regular_price_height == other.regular_price_height) \
               and (self.regular_price_style is None or other.regular_price_style is None
                    or self.regular_price_style == other.regular_price_style) \
               and (self.campaign_price_text is None or other.campaign_price_text is None
                    or self.campaign_price_text == other.campaign_price_text) \
               and (self.campaign_price_color is None or other.campaign_price_color is None
                    or self.campaign_price_color == other.campaign_price_color) \
               and (self.campaign_price_height is None or other.campaign_price_height is None
                    or self.campaign_price_height == other.campaign_price_height)

    def __repr__(self):
        return "Product(%s, %s, %s, %s, %s, %s, %s, %s)" % (self.name, self.regular_price_text,
                                                            self.regular_price_color, self.regular_price_height,
                                                            self.regular_price_style, self.campaign_price_text,
                                                            self.campaign_price_color, self.campaign_price_height)
