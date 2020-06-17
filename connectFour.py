#!/usr/local/bin/python3
import discord

#Class containing members and functions necessary to play connect four
class connectFour:
    def __init__(self):
        #Stores current game state
        self._gameState = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1]]
        #Emoji assets for connect four
        self._gameEmoji = ("😭","1️⃣","2️⃣","3️⃣","4️⃣","5️⃣","6️⃣","7️⃣","🔴","🔵")
        #Symbols for player one and player two
        self._p1Symbol = ":red_circle:"
        self._p2Symbol = ":yellow_circle:"
        
        #Keeps track of whose turn it is (true = player 1, false = player 2)
        self._turnTracker = True
        #Keeps track of whether the game is in progress (True), or the game is in player select mode (False)
        self._gameInProgress = False
        
    #Returns whether the game is in progress or not
    def inProgress(self):
        return self._gameInProgress
    
    #Player select then starts game
    async def playerSelect(self,message):
        self.botMessage = message.channel.send("Welcome to Connect 4! Those who wish to play please click on one of the coloured tokens below:")
        self.botMessage.add_reaction(self._gameEmoji[8])
        self.botMessage.add_reaction(self._gameEmoji[9])
        
    
    #Returns string containing game board
    async def getBoard(self):
        board = ""
        
        for i in range(5,-1,-1):
            for j in range(7):
                board += "#"
                if self._gameState[j][i] == -1:
                    board += "\t  \t"
                #Prints gamepiece
                else:
                    board += f"  {self._gameState[j][i]}  "
                    
            board += "#"
        
            if i > 0:
                board += "\n#= = =#= = =#= = =#= = =#= = =#= = =#= = =#\n"
        
            #Bottom row of board
            else:
                board += "\n## 1 ### 2 ### 3 ### 4 ### 5 ### 6 ### 7 ##"
        
        return board
        
    async def sendReactions(self):
        await self.botMessage.add_reaction(self._gameEmoji[1])
        await self.botMessage.add_reaction(self._gameEmoji[2])
        await self.botMessage.add_reaction(self._gameEmoji[3])
        await self.botMessage.add_reaction(self._gameEmoji[4])
        await self.botMessage.add_reaction(self._gameEmoji[5])
        await self.botMessage.add_reaction(self._gameEmoji[6])
        await self.botMessage.add_reaction(self._gameEmoji[7])
        await self.botMessage.add_reaction(self._gameEmoji[0])
        
    #Assume col is index
    #Return True if token successfully dropped, return false otherwise
    async def dropToken(self,col):
        for i in range(6):
            if self._gameState[col][i] == -1:
                #Player 1's turn
                if self._turnTracker == True:
                    self._gameState[col][i] = self._p1Symbol
                #Player 2's turn
                else:
                    self._gameState[col][i] = self._p2Symbol
                return True
        return False
    
    async def playerTurn():
        
 
async def run(message,client):

    game = connectFour()
    game.playerSelect(message)
    
    await game.botMessage.channel.edit(content = await game.getBoard())
    await game.sendReactions()

    @client.event
    async def on_reaction_add(reaction,user):
        if user == client.user:
            return
            
        elif game.inProgress() and reaction.message.id == botMessage.id:
            pass
        
        elif not game.inProgress() and reaction.message.id == botMessage.id:
