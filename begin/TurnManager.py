from ActionEnum import ActionEnum
from Position import Position
from Organisms.Organism import Organism # ZMIENIONY IMPORT
from SpeciesGuard import SpeciesGuard

class TurnManager(object):

	def __init__(self, world):
		self.__world = world
		self.__speciesGuard = SpeciesGuard()

	def makeTurn(self):
		self.__processAllOrganismsActions()
		self.__applyPlagueEffects()
		self.__cleanupDeadOrganisms()
		self.__incorporateNewOrganisms()
		self.__speciesGuard.manage_species(self.__world)
		self.__world.turn += 1

	def __processAllOrganismsActions(self):
		for org in self.__world.organisms:
			if self.__world.positionOnBoard(org.position):
				self.__executeActions(org.move())
				if self.__world.positionOnBoard(org.position):
					self.__executeActions(org.action())

	def __executeActions(self, actions):
		for action in actions:
			self.__makeMove(action)

	def __cleanupDeadOrganisms(self):
		self.__world.organisms = [o for o in self.__world.organisms if self.__world.positionOnBoard(o.position)]
		for o in self.__world.organisms:
			o.liveLength -= 1
			o.power += 1
			if o.liveLength < 1:
				print(str(o.__class__.__name__) + ': died of old age at: ' + str(o.position))
		self.__world.organisms = [o for o in self.__world.organisms if o.liveLength > 0]

	def __incorporateNewOrganisms(self):
		self.__world.newOrganisms = [o for o in self.__world.newOrganisms if self.__world.positionOnBoard(o.position)]
		self.__world.organisms.extend(self.__world.newOrganisms)
		self.__world.organisms.sort(key=lambda o: o.initiative, reverse=True)
		self.__world.newOrganisms = []

	def __makeMove(self, action):
		print(action)
		if action.action == ActionEnum.A_ADD:
			self.__world.newOrganisms.append(action.organism)
		elif action.action == ActionEnum.A_INCREASEPOWER:
			action.organism.power += action.value
		elif action.action == ActionEnum.A_MOVE:
			action.organism.position = action.position
		elif action.action == ActionEnum.A_REMOVE:
            # ZMIENIONY SPOSÓB DOSTĘPU DO STAŁYCH
			action.organism.position = Position(xPosition=Organism.GRAVEYARD_POSITION_X, yPosition=Organism.GRAVEYARD_POSITION_Y)

	def __applyPlagueEffects(self):
		if self.__world.plagueTurns > 0:
			for org in self.__world.organisms:
				org.liveLength = org.liveLength // 2
			self.__world.plagueTurns -= 1
