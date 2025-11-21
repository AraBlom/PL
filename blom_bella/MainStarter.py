"""
:author: Bella Blom
Class: PL Fall 2025
Description:
Station mangement program. Simulates an assembly line
with a user menu to add custom behavior.
Last tier passes: all tiers passes
Checklist:
Grading tags in for all lines marked with * (x8)		__x

1. Initial Show system Got it compiling

2. Handle bad input*

3. Add Package with error handling*				___x

4. Update (one item)						___	x

5. Update (multiple items)					___x

6. Custom System, no packages 					___x

7. Custom System, error handling				___x

8. Fill Behavior (type 2 and 3)*				___x

9. Custom System-Stress Test					___	x

10. Color Behavior (color and compacted)*			___	x

11. Swapping string and error testing 				___x
"""
from ColorText import ColorText
from AssemblyLine import AssemblyLine

SHOW_REDIRECTED_INPUT_COMMENTS = False
LINE_MARKER = " ##############################################################"

"""
Given input function
"""
def cleanInput( prompt ):
  result = input( prompt )
  # strips out blank lines in input
  while result == '' or result[ 0 ] == '#':
    if len( result ) > 0 and result[ 0 ] == '#' and SHOW_REDIRECTED_INPUT_COMMENTS:
      print( ColorText.fg.cyan + result + LINE_MARKER + ColorText.reset )
    result = input()
  
  return result
"""
Main run of program, prints menu and handles IO
"""
def main( ):
    menu = "\n" \
           "1) Add Package\n"\
           "2) Update One Tick\n"\
           "3) Update X Ticks\n"\
           "4) Make New Simulator\n"\
           "5) Set Appearance\n"\
           "0) Quit\n"\

    line = AssemblyLine()
    choice = -1
    while choice != 0:
        line.print_line()
        print( menu )
        try:
            choice = int(cleanInput( "Choice:> " ))

            if choice == 1:
                pkg_type = float (cleanInput("Type:> "))
                capacity = float(cleanInput("Max Units:> "))
                if int(pkg_type) == pkg_type and int(capacity) == capacity:
                    line.add_package(int(pkg_type), int(capacity))
                else:
                    raise ValueError

            elif choice == 2:
                line.tick()

            elif choice == 3:
                ticks = float (cleanInput("How many updates:> "))
                if int(ticks) == ticks:
                    line.tick_x(int(ticks))
                else:
                    raise ValueError


            elif choice == 4:
                line.clear_track()
                exit = 0
                while (exit != "n"):
                    c_type = float(cleanInput("Line (1) or Station (2):> "))
                    if c_type != int(c_type):
                        raise ValueError
                    if c_type <1 or c_type > 2:
                        e = IndexError()
                        e.add_note("1-2")
                        raise e
                    if c_type == 1:
                        num = float (cleanInput("Length:> "))
                        if int(num) != num:
                            raise ValueError
                        line.add_track(int(num))
                    elif c_type == 2:
                        s_fill_type = float( cleanInput("Fill behavior: None (1), Fill (2), Type Fill (3):> "))
                        if int(s_fill_type) != s_fill_type:
                            raise ValueError
                        s_fill_type = int(s_fill_type)
                        if s_fill_type > 3 or s_fill_type < 1:
                            e = IndexError()
                            e.add_note("1-2")
                            raise e
                        if s_fill_type == 3:
                            s_type = float(cleanInput("Type:> "))
                            if s_type != int(s_type):
                                raise ValueError
                        else:
                            s_type = 0
                        if s_fill_type != 1:
                            s_fill_units = float( cleanInput("Fill units:> "))
                            if int(s_fill_units) != s_fill_units:
                                raise ValueError
                            s_pkg_w = float(cleanInput("Package weight:> "))
                            if int(s_pkg_w) != s_pkg_w:
                                raise ValueError
                        else:
                            s_fill_units = 0
                            s_pkg_w = 1
                        line.add_station(int(s_type), int(s_fill_units),int( s_pkg_w), s_fill_type)
                    exit = str (cleanInput("Add another component (n to stop):> "))


            elif choice == 5:
                app = float (cleanInput("Appearance: Default (1), Color (2), Compacted (3):> "))
                if int(app) != app:
                    raise ValueError
                if app >3 or app <1 :
                    e = IndexError()
                    e.add_note("1-3")
                    raise e
                line.set_display(int(app))



            elif choice == 0 or choice == '0':
                choice = 0
            else:
                e = IndexError()
                e.add_note("0-5")
                raise e #GRADING: RAISE
        except ValueError: #GRADING: CATCH
            print("Please, input an integer")
        except IndexError as ie:
            print("Out of " + str(ie.__notes__[0]) +" range")

if __name__ == '__main__':
    main( )
