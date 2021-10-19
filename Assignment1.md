# Assignment 1 - Simple Dominion

Your task is to implement a simplified version of board game "Dominion".

For those who know the game these are the rule changes:
- 1 player game
- Only vanilla cards supported
- You have to play your treasures in play phase (of course they don't cost actions).

Full rules:

One player gets a starting deck containing 10 cards (3 Estates and 7 Coppers - see GameCardType class file to see what these cards are). the deck is shuffled and the player draws 5 top cards from deck into his hand.

The game is played in turns. Each turn has Action Phase and Buy Phase. A player starts the turn with 1 Action, 1 Buy, and 0 Coins. In action phase, you can play cards from hand. Playing an action card costs an Action - if the player has no action left, he cannot play further action cards this turn. When card is played its effect is immediately evaluated. The effects include:
- add Actions
- add Buys
- add Cards - the player draws that many cards from the deck immediately (see further rules if deck has fewer cards)
- add Coins
After a player plays a card it goes into Play area, not into Discard Pile.

In Buy Phase the player may buy several cards. Buying cards costs one Buy. If player does not have any Buys left he cannot buy more cards this turn. Besides this, buying a card costs gold (the cost of each card is given). Cards are bought from several piles of cards, Buy Decks, each containing several copies of the cards (see full Dominion rules for details). When a player Buys a card it goes to Discard Pile.

After the end of turn, the cards in Play and Hand are moved into the Discard Pile. And the player draws 5 new cards.

Whenever the player cannot draw as many cards as he has to, he shuffles Discard Pile and puts them into the Deck in such a way that the old cards in Decks are on top of the new ones.

The game ends when there are no more Province cards or at least 3 Buy Decks containing cards to buy are empty.

The winning criteria are up to you :).

Full rules are [here](https://www.riograndegames.com/wp-content/uploads/2016/09/Dominion-2nd-Edition-Rules.pdf)


## Implementation remarks

Implement the game based on my [design](du1.pdf) - and you do not need to do all the stuff, see the comment in the diagram. The design is not complete, e.g. constructors are missing and several necessary interfaces are missing. Complete or even improve it, but try to keep the division of the responsibilities similar. Besides this, there is a good chance I missed something; if this is the case fix it.

You can program in Java or Python. I even started the project for you. Your code should be tested, but the tests need not to be perfect for all classes. You can use solitary or sociable testing for almost all classes but I want you to use strictly solitary tests for Hand class. Also focus on test coverage for this class. Do not forget to do some kind of an integration test. Keep your tests deterministic. Test only classes and methods where it makes sense to test them.

You should use Git and produce a reasonable history of commits. 
