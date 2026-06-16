from pydantic import BaseModel
from enum import Enum

class Suit(str, Enum):
    HEARTS = "hearts"
    DIAMONDS = "diamonds"
    CLUBS = "clubs"
    SPADES = "spades"

class Card(BaseModel):
    suit: Suit
    rank: str

class GameState(BaseModel):
    deck: list[Card]
    player_hand: list[Card]
    dealer_hand: list[Card]
    status: str
    result: str | None = None