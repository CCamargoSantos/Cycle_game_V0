import constants
import itertools
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point

class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the snake collides
    with the food, or the snake collides with its segments, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            #self._handle_food_collision(cast)
            self._handle_segment_collision(cast)
            self._handle_game_over(cast)

    # def _handle_food_collision(self, cast):
    #     """Updates the score nd moves the food if the snake collides with the food.
        
    #     Args:
    #         cast (Cast): The cast of Actors in the game.
    #     """
    #     score = cast.get_first_actor("scores")
    #     food = cast.get_first_actor("foods")
    #     snake = cast.get_first_actor("snakes")
    #     head = snake.get_head()

    #     if head.get_position().equals(food.get_position()):
    #         points = food.get_points()
    #         snake.grow_tail(points)
    #         score.add_points(points)
    #         food.reset()
    
    def _handle_segment_collision(self, cast):
        """Sets the game over flag if the snake collides with one of its segments.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """

        snake1 = cast.get_first_actor("snakes")
        head1 = snake1.get_segments()[0]
        segments1 = snake1.get_segments()[1:]
        
        snake2 = cast.get_second_actor("snakes")
        head2 = snake2.get_segments()[0]
        segments2 = snake2.get_segments()[1:]
        

        '''i = 0

        while i < len(segments2):
            if head1.get_position().equals(segments2[i].get_position()):
                self._is_game_over = True
            i += 1
        print(i)
        
        j=0
        while j < len(segments1):
            if head2.get_position().equals(segments1[j].get_position()):
                self._is_game_over = True
            j += 1
        print(j)'''#This give me the view that both snakes area same length
        '''
        for seg1,seg2 in itertools.zip_longest(segments1,segments2):
            if head2.get_position() == seg1.get_position():
                h = head2.get_position()
                s = seg1.get_position()
                print(h,s)
                self._is_game_over = True
            elif head1.get_position() == seg2.get_position():
                h = head1.get_position()
                s = seg2.get_position()
                print(h,s)
                self._is_game_over = True
        '''

        for indice in range(0,len(segments1)):
            if segments1[indice] in segments2:
                print('verdadero')
            elif segments2[indice] in segments1:
                print('verdadero')
            else:
                print('falso')
            '''
        for seg1,seg2 in itertools.zip_longest(segments1,segments2):
            print('Entró de nuevo al for')
            print(f'h1x:{head1.get_position().get_x()},h1y:{head1.get_position().get_y()}')
            print(f'h2x:{head2.get_position().get_x()},h2y:{head2.get_position().get_y()}')
            print(f's1x:{seg1.get_position().get_x()},s1y:{seg1.get_position().get_y()}')
            print(f's2x:{seg2.get_position().get_x()},s2y:{seg2.get_position().get_y()}')



              
            if (head1.get_position().get_x() == seg2.get_position().get_x() & head1.get_position().get_y() == seg2.get_position().get_y())|(head2.get_position().get_x() == seg1.get_position().get_x() & head2.get_position().get_y() == seg1.get_position().get_y())|(seg1.get_position().get_x() == seg2.get_position().get_x() & seg1.get_position().get_y() == seg2.get_position().get_y()):
                h = head2.get_position()
                s = seg2.get_position()
                print(h,s)
                self._is_game_over = True
            '''
        #for seg1,seg2 in itertools.zip_longest(segments1,segments2):
            '''if head2.get_position().equals(seg2.get_position())|head1.get_position().equals(seg1.get_position()):
                h = head2.get_position()
                s = seg2.get_position()
                print(h,s)
                self._is_game_over = True'''
            #elif head1.get_position().equals(seg2.get_position()):
                #self._is_game_over = True
        
        #for seg1,seg2 in (segments1,segments2):




        #while self._is_game_over == False:
        
        #for segment in segments1:
            #if head2.get_position().equals(segment.get_position())|head1.get_position().equals(segment.get_position()):
                #self._is_game_over = True
        
        #for segment in segments2:
            #if head1.get_position().equals(segment.get_position()):
                #self._is_game_over = True

        
    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the snake and food white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:
            snake1 = cast.get_first_actor("snakes")
            segments1 = snake1.get_segments()
            #food = cast.get_first_actor("foods")
            
            snake2 = cast.get_second_actor("snakes")
            segments2 = snake2.get_segments()
            
            
            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            message = Actor()
            message.set_text("Game Over!")
            message.set_position(position)
            cast.add_actor("messages", message)

            for segment in segments1:
                segment.set_color(constants.WHITE)
                #food.set_color(constants.WHITE)            
            
            for segment in segments2:
                segment.set_color(constants.WHITE)
                
                
            
            