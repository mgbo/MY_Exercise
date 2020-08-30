from phase import Phase
from card import Card
from witch_game import WitchGame, WITCH_CARD

class DiscardWithCard(Phase):
  def __init__(self, player, card):
    self.player = player
    self.card = card
    super(DiscardWithCard, self).__init__()
  def play(self):
    for other in self.player.hand:
      if self.card == other or self.card == WITCH_CARD or other == WITCH_CARD:
        continue
      if self.card.value == other.value:
        print("Player %s discards %s and %s" % (self.player.name, repr(self.card), repr(other)))
        self.player.hand.remove(self.card)
        self.player.hand.remove(other)
        print("Player %s now has %s" % (self.player.name, self.player.hand))
        return

class DiscardPairs(Phase):
  def __init__(self, player):
    self.player = player
    super(DiscardPairs, self).__init__()
  def play(self):
    discard = False
    for card in self.player.hand:
      if card in self.player.hand:
        DiscardWithCard(self.player, card)()

class LeaveGame(Phase):
  def __init__(self, player):
    self.player = player
    super(LeaveGame, self).__init__()
  def play(self):
    if len(self.player.hand) == 0:
      print("Player %s has left the table" % (self.player.name))
      WitchGame().players.remove(self.player)


class StealCard(Phase):
  def __init__(self, thief, victim):
    self.thief = thief
    self.victim = victim
    super(StealCard, self).__init__()
  def play(self):
    card = self.thief.card_from_other_hand(self.victim)
    self.victim.hand.remove(card)
    self.thief.hand.add_card(card)
    print("Player %s stole a card from Player %s" % (self.thief.name, self.victim.name))

class MainPhase(Phase):
  def play(self):
    game = WitchGame()
    StealCard(game.current_player, game.players[1])()
    LeaveGame(game.players[1])()
    DiscardPairs(game.current_player)()
    LeaveGame(game.current_player)()
    if len(game.players) == 1:
      game.loser = game.players[0]
      return


